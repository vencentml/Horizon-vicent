"""Generate a weekly Russia-Ukraine war summary.

This script is intentionally defensive: it must never publish an empty weekly
report when sources were fetched successfully. If the AI call or JSON parsing
fails, it renders a deterministic fallback summary based on the collected
source items.
"""

from __future__ import annotations

import asyncio
import json
import os
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import feedparser
import httpx

from src.ai.client import create_ai_client
from src.ai.utils import parse_json_response
from src.models import AIConfig


# Strong title-level indicators. A title match here is usually enough to keep.
TITLE_STRONG_KEYWORDS = (
    "ukraine war",
    "ukraine briefing",
    "ukraine war briefing",
    "ukrainian drone",
    "ukrainian drones",
    "ukraine expands oil strikes",
    "ukraine hits",
    "russia strikes",
    "russian strikes",
    "russian oil",
    "russia's oil",
    "moscow victory day",
    "victory day parade",
    "ceasefire",
    "frontline",
    "fortress belt",
    "donetsk",
    "luhansk",
    "kharkiv",
    "crimea",
    "black sea",
    "zelensky",
    "zelenskyy",
    "putin",
    "bucha",
    "chornobyl",
    "nato",
)

# Broader body-level indicators. These only count when paired with a title signal.
BODY_CONTEXT_KEYWORDS = (
    "ukraine",
    "ukrainian",
    "russia",
    "russian",
    "kyiv",
    "moscow",
    "zelensky",
    "zelenskyy",
    "putin",
    "donetsk",
    "luhansk",
    "kharkiv",
    "crimea",
    "black sea",
    "drone",
    "missile",
    "frontline",
    "nato",
    "sanction",
    "oil tanker",
    "shadow fleet",
)

# Terms that often indicate Guardian/BBC live blogs or general Europe stories that
# merely mention Ukraine/Russia in passing.
NOISE_TITLE_KEYWORDS = (
    "uk politics live",
    "politics live",
    "as it happened",
    "venice biennale",
    "art exhibition",
    "wada",
    "doping",
    "hungary",
    "mali",
    "armenia",
    "migrant",
    "reform uk",
    "first kiss",
    "in pictures",
)

# War-on-the-Rocks is a broad strategy feed. Keep only pieces that are directly
# relevant to the Russia-Ukraine war, air/missile/drone warfare, sanctions, or
# Russian defense industry.
WOTR_STRONG_KEYWORDS = (
    "ukraine",
    "russia",
    "russian",
    "drone",
    "drones",
    "missile",
    "missiles",
    "air war",
    "defense industry",
    "defence industry",
    "crowd sourced defense",
    "chornobyl",
)

FEEDS = [
    {
        "name": "The Guardian Ukraine",
        "url": "https://www.theguardian.com/world/ukraine/rss",
    },
    {
        "name": "BBC Europe News",
        "url": "https://feeds.bbci.co.uk/news/world/europe/rss.xml",
    },
    {
        "name": "War on the Rocks",
        "url": "https://warontherocks.com/feed/",
    },
    {
        "name": "ISW Ukraine Updates",
        "url": "https://www.understandingwar.org/rss.xml",
    },
    {
        "name": "Kyiv Independent",
        "url": "https://kyivindependent.com/rss/",
    },
]


@dataclass
class WarItem:
    title: str
    url: str
    source: str
    published: datetime
    summary: str

    def as_prompt_line(self, index: int) -> str:
        date = self.published.strftime("%Y-%m-%d")
        text = self.summary.replace("\n", " ").strip()
        if len(text) > 500:
            text = text[:500] + "..."
        return f"[{index}] {date} | {self.source} | {self.title}\nURL: {self.url}\nSummary: {text}"


def _parse_date(entry: Any) -> datetime:
    parsed = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if parsed:
        return datetime(*parsed[:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


def _entry_title(entry: Any) -> str:
    return getattr(entry, "title", "") or ""


def _entry_summary(entry: Any) -> str:
    return getattr(entry, "summary", "") or ""


def _entry_text(entry: Any) -> str:
    return f"{_entry_title(entry)} {_entry_summary(entry)}".lower()


def _contains_any(text: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in text for keyword in keywords)


def _is_relevant(entry: Any, source_name: str) -> bool:
    """Return True only for items directly relevant to the Russia-Ukraine war.

    The previous filter accepted any body mention of Ukraine/Russia, which caused
    broad Europe, art, sports, and UK politics items to leak into the report.
    This filter requires a stronger title-level signal for broad news feeds.
    """
    title = _entry_title(entry).lower()
    summary = _entry_summary(entry).lower()
    text = f"{title} {summary}"

    if _contains_any(title, NOISE_TITLE_KEYWORDS):
        return False

    # RSS feeds explicitly scoped to Ukraine can be more permissive, but still
    # reject known noise/live-blog patterns above.
    if source_name in {"ISW Ukraine Updates", "Kyiv Independent"}:
        return _contains_any(text, BODY_CONTEXT_KEYWORDS)

    if source_name == "War on the Rocks":
        return _contains_any(text, WOTR_STRONG_KEYWORDS)

    # BBC Europe and Guardian Ukraine frequently include broad regional/politics
    # stories. Require direct title relevance, not just body mentions.
    if _contains_any(title, TITLE_STRONG_KEYWORDS):
        return True

    # Keep articles whose title names Ukraine/Russia and body contains a war
    # context term. This captures headlines such as "Germany troop cuts send wrong
    # signal to Russia" while dropping unrelated Russia sports/culture stories.
    title_mentions_actor = any(k in title for k in ("ukraine", "ukrainian", "russia", "russian", "putin", "zelensky", "zelenskyy"))
    body_has_war_context = any(
        k in text
        for k in (
            "war",
            "strike",
            "drone",
            "missile",
            "frontline",
            "ceasefire",
            "troop",
            "nato",
            "sanction",
            "oil",
            "military",
        )
    )
    return title_mentions_actor and body_has_war_context


def _week_id(now: datetime) -> str:
    iso_year, iso_week, _ = now.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


async def fetch_feed(client: httpx.AsyncClient, feed: dict[str, str], since: datetime) -> list[WarItem]:
    try:
        response = await client.get(feed["url"], follow_redirects=True)
        response.raise_for_status()
    except Exception as exc:
        print(f"WARN: failed to fetch {feed['name']}: {exc}")
        return []

    parsed = feedparser.parse(response.content)
    items: list[WarItem] = []
    for entry in parsed.entries:
        published = _parse_date(entry)
        if published < since:
            continue
        if not _is_relevant(entry, feed["name"]):
            continue
        title = _entry_title(entry).strip()
        url = getattr(entry, "link", "").strip()
        if not title or not url:
            continue
        summary = _entry_summary(entry)
        items.append(
            WarItem(
                title=title,
                url=url,
                source=feed["name"],
                published=published,
                summary=summary,
            )
        )
    return items


async def fetch_items(days: int = 7, limit: int = 40) -> list[WarItem]:
    since = datetime.now(timezone.utc) - timedelta(days=days)
    async with httpx.AsyncClient(timeout=30.0, headers={"User-Agent": "Horizon/1.0"}) as client:
        results = await asyncio.gather(*(fetch_feed(client, feed, since) for feed in FEEDS))

    seen: set[str] = set()
    items: list[WarItem] = []
    for batch in results:
        for item in batch:
            key = item.url.rstrip("/")
            if key in seen:
                continue
            seen.add(key)
            items.append(item)

    items.sort(key=lambda item: item.published, reverse=True)
    return items[:limit]


def _load_ai_config() -> AIConfig | None:
    config_path = Path("data/config.json")
    if not config_path.exists():
        return None
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    return AIConfig.model_validate(raw["ai"])


async def summarize_with_ai(items: list[WarItem], week_id: str) -> dict[str, Any] | None:
    ai_config = _load_ai_config()
    if not ai_config:
        return None
    if not os.environ.get(ai_config.api_key_env):
        return None

    source_text = "\n\n".join(item.as_prompt_line(i + 1) for i, item in enumerate(items))
    system = """You are a careful open-source intelligence analyst. Summarize weekly Russia-Ukraine war developments from public reporting only.

Requirements:
- Be cautious and avoid unsupported claims.
- Distinguish battlefield developments, strikes/drones/missiles, military aid, diplomacy/policy, and uncertainty.
- Do not mention events unless they are supported by the provided source items.
- Use Chinese.
- Return valid JSON only.
- Every list must be non-empty if source items are available.
"""
    user = f"""Create a weekly Russia-Ukraine war summary for {week_id} from these source items.

Source items:
{source_text}

Return JSON exactly in this shape:
{{
  "executive_summary": ["3-5 bullet points in Chinese"],
  "themes": [
    {{"title": "战场态势", "bullets": ["1-3 bullets"]}},
    {{"title": "空袭、无人机与导弹", "bullets": ["1-3 bullets"]}},
    {{"title": "防务援助与军工", "bullets": ["1-3 bullets"]}},
    {{"title": "外交、制裁与政策", "bullets": ["1-3 bullets"]}},
    {{"title": "不确定性与观察点", "bullets": ["1-3 bullets"]}}
  ],
  "key_items": [
    {{"title": "item title", "source": "source name", "url": "source url", "why_it_matters": "why it matters in Chinese"}}
  ]
}}
"""
    try:
        client = create_ai_client(ai_config)
        response = await client.complete(system=system, user=user)
        result = parse_json_response(response)
    except Exception as exc:
        print(f"WARN: AI summary failed: {exc}")
        return None

    if not isinstance(result, dict):
        return None
    if not result.get("executive_summary") or not result.get("themes") or not result.get("key_items"):
        return None
    return result


def fallback_summary(items: list[WarItem]) -> dict[str, Any]:
    by_source = Counter(item.source for item in items)
    newest = items[:10]

    executive = [
        f"本期共收集 {len(items)} 条高相关公开报道和分析，来源包括 " + "、".join(f"{k}({v})" for k, v in by_source.most_common()) + "。",
        "由于 AI 结构化摘要不可用，本报告使用保底规则生成：按来源、标题关键词和发布时间整理主要观察点。",
        "请将本报告视为公开来源线索汇总，而不是战场态势的确定性结论。",
    ]

    buckets: dict[str, list[str]] = defaultdict(list)
    for item in items:
        text = f"{item.title} {item.summary}".lower()
        line = f"{item.published.strftime('%m-%d')}｜{item.source}：{item.title}"
        if any(k in text for k in ("drone", "missile", "strike", "air", "attack")):
            buckets["空袭、无人机与导弹"].append(line)
        elif any(k in text for k in ("aid", "nato", "weapon", "defence", "defense", "sanction")):
            buckets["防务援助与军工"].append(line)
        elif any(k in text for k in ("talk", "deal", "trump", "eu", "policy", "diplomacy", "ceasefire")):
            buckets["外交、制裁与政策"].append(line)
        else:
            buckets["战场态势"].append(line)

    themes = []
    for title in ["战场态势", "空袭、无人机与导弹", "防务援助与军工", "外交、制裁与政策"]:
        bullets = buckets.get(title, [])[:4]
        if not bullets:
            bullets = ["本期高相关公开来源中没有足够材料形成该主题的独立判断。"]
        themes.append({"title": title, "bullets": bullets})
    themes.append(
        {
            "title": "不确定性与观察点",
            "bullets": [
                "公开报道通常存在延迟、选择性和来源偏差，具体战果和伤亡数字需要等待多源交叉验证。",
                "后续应重点观察战线变化、远程打击频率、防空消耗、外部军援节奏和谈判信号。",
            ],
        }
    )

    key_items = [
        {
            "title": item.title,
            "source": item.source,
            "url": item.url,
            "why_it_matters": "该条目来自本周高相关公开来源，提供了判断俄乌战争进展的一个观察点。",
        }
        for item in newest
    ]

    return {
        "executive_summary": executive,
        "themes": themes,
        "key_items": key_items,
    }


def render_markdown(summary: dict[str, Any], items: list[WarItem], week_id: str, today: str) -> str:
    by_source = Counter(item.source for item in items)
    source_distribution = "、".join(f"{source}({count})" for source, count in by_source.most_common()) or "无"
    lines = [
        "---",
        "layout: default",
        f'title: "俄乌战争一周进展: {week_id}"',
        f"date: {today}",
        "category: ukraine-war-weekly",
        "lang: zh",
        "---",
        "",
        f"# 俄乌战争一周进展: {week_id}",
        "",
        f"> 本期参考 {len(items)} 条高相关公开报道和分析。",
        "",
        "**来源分布**：" + source_distribution,
        "",
        "## 执行摘要",
        "",
    ]

    for bullet in summary.get("executive_summary", []):
        lines.append(f"- {bullet}")

    lines.extend(["", "## 分主题进展", ""])
    for theme in summary.get("themes", []):
        lines.append(f"### {theme.get('title', '未命名主题')}")
        lines.append("")
        bullets = theme.get("bullets") or ["本主题暂无足够信息。"]
        for bullet in bullets:
            lines.append(f"- {bullet}")
        lines.append("")

    lines.extend(["## 重点条目", ""])
    key_items = summary.get("key_items") or []
    if not key_items and items:
        key_items = fallback_summary(items)["key_items"]
    for item in key_items:
        title = item.get("title", "未命名条目")
        url = item.get("url", "")
        source = item.get("source", "unknown")
        why = item.get("why_it_matters", "该条目值得后续观察。")
        if url:
            lines.append(f"- [{title}]({url}) — {source}：{why}")
        else:
            lines.append(f"- {title} — {source}：{why}")

    lines.extend(["", "## 原始来源列表", ""])
    for item in items:
        date = item.published.strftime("%Y-%m-%d")
        lines.append(f"- {date}｜{item.source}｜[{item.title}]({item.url})")

    lines.append("")
    return "\n".join(lines)


async def main() -> None:
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    week_id = _week_id(now)

    items = await fetch_items(days=7, limit=40)
    if not items:
        # Still publish a clear non-empty diagnostic page instead of a blank report.
        summary = {
            "executive_summary": [
                "本期没有从已配置公开来源中抓取到足够的俄乌战争相关报道。",
                "这可能是上游 RSS 源暂时不可用、关键词过滤过窄或本周报道量较少导致。",
            ],
            "themes": [
                {"title": "采集状态", "bullets": ["未抓取到可用于周报的来源条目。"]},
                {"title": "后续动作", "bullets": ["检查 RSS 源可用性，并评估是否增加更多可靠公开来源。"]},
            ],
            "key_items": [],
        }
    else:
        summary = await summarize_with_ai(items, week_id)
        if summary is None:
            summary = fallback_summary(items)

    markdown = render_markdown(summary, items, week_id, today)
    posts_dir = Path("docs/_posts")
    posts_dir.mkdir(parents=True, exist_ok=True)
    output_path = posts_dir / f"{today}-ukraine-war-weekly-{week_id}.md"
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Wrote {output_path}")

    status_dir = Path("docs/status")
    status_dir.mkdir(parents=True, exist_ok=True)
    status = {
        "report": "ukraine-war-weekly",
        "date": today,
        "week_id": week_id,
        "items": len(items),
        "sources": dict(Counter(item.source for item in items)),
        "output": str(output_path),
        "status": "success",
        "filter_version": "strict-v2",
    }
    (status_dir / "latest-ukraine-war-weekly.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    asyncio.run(main())
