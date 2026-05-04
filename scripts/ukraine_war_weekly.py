#!/usr/bin/env python3
"""Generate a Chinese weekly Russia-Ukraine war progress report.

The script fetches war-related RSS feeds, filters recent items, and asks a
DeepSeek/OpenAI-compatible model to synthesize a Chinese weekly report. It is
self-contained and does not depend on Horizon's daily pipeline, so the weekly
report can still publish when a source returns sparse data or an AI call fails.
"""

from __future__ import annotations

import argparse
import email.utils
import html
import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


DEFAULT_MODEL = "deepseek-v4-flash"
DEFAULT_BASE_URL = "https://api.deepseek.com"

FEEDS = [
    {
        "name": "ISW Ukraine Updates",
        "url": "https://www.understandingwar.org/rss.xml",
        "weight": 3,
    },
    {
        "name": "Kyiv Independent",
        "url": "https://kyivindependent.com/rss/",
        "weight": 2,
    },
    {
        "name": "War on the Rocks",
        "url": "https://warontherocks.com/feed/",
        "weight": 2,
    },
    {
        "name": "Defense One",
        "url": "https://www.defenseone.com/rss/all/",
        "weight": 1,
    },
    {
        "name": "The Guardian Ukraine",
        "url": "https://www.theguardian.com/world/ukraine/rss",
        "weight": 1,
    },
    {
        "name": "BBC Europe News",
        "url": "https://feeds.bbci.co.uk/news/world/europe/rss.xml",
        "weight": 1,
    },
]

KEYWORDS = [
    "ukraine", "ukrainian", "kyiv", "zelensky", "zelenskyy", "russia", "russian",
    "putin", "moscow", "donetsk", "luhansk", "kharkiv", "kherson", "zaporizhzhia",
    "crimea", "drone", "missile", "frontline", "kremlin", "nato", "black sea",
    "kursk", "pokrovsk", "avdiivka", "bakhmut", "odesa", "sumy", "chernihiv",
]


@dataclass
class WarItem:
    title: str
    url: str
    source: str
    published_at: str
    summary: str = ""
    score: int = 0


def fetch_url(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Horizon-Ukraine-War-Weekly"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def post_json(url: str, payload: dict, headers: dict[str, str], timeout: int = 120) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Horizon-Ukraine-War-Weekly",
            **headers,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def strip_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def parse_date(value: str) -> datetime | None:
    if not value:
        return None
    try:
        dt = email.utils.parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(value, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            continue
    return None


def keyword_score(text: str) -> int:
    lower = text.lower()
    return sum(1 for keyword in KEYWORDS if keyword in lower)


def fetch_feed(feed: dict, since: datetime, per_feed_limit: int) -> list[WarItem]:
    try:
        raw = fetch_url(feed["url"])
        root = ET.fromstring(raw)
    except Exception as exc:
        print(f"Feed failed: {feed['name']}: {exc}", file=sys.stderr)
        return []

    items: list[WarItem] = []
    for node in root.findall(".//item"):
        title = strip_html(node.findtext("title") or "")
        link = (node.findtext("link") or "").strip()
        summary = strip_html(
            node.findtext("description")
            or node.findtext("summary")
            or node.findtext("content")
            or ""
        )
        published_raw = node.findtext("pubDate") or node.findtext("published") or node.findtext("updated") or ""
        published = parse_date(published_raw) or datetime.now(timezone.utc)
        combined = f"{title} {summary}"
        score = keyword_score(combined) + int(feed.get("weight", 1))

        if published < since and score < 4:
            continue
        if score <= 1:
            continue
        if not title or not link:
            continue

        items.append(
            WarItem(
                title=title,
                url=link,
                source=feed["name"],
                published_at=published.strftime("%Y-%m-%d"),
                summary=summary[:700],
                score=score,
            )
        )

    items.sort(key=lambda item: (item.score, item.published_at), reverse=True)
    return items[:per_feed_limit]


def collect_items(hours: int, limit: int, per_feed_limit: int) -> list[WarItem]:
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    collected: list[WarItem] = []
    for feed in FEEDS:
        collected.extend(fetch_feed(feed, since=since, per_feed_limit=per_feed_limit))

    seen: set[str] = set()
    unique: list[WarItem] = []
    for item in sorted(collected, key=lambda item: (item.score, item.published_at), reverse=True):
        key = item.url.split("?")[0].rstrip("/")
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique[:limit]


def extract_json_object(text: str) -> dict | None:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def fallback_analysis(items: list[WarItem]) -> dict:
    source_counts = Counter(item.source for item in items)
    highlights = [
        {
            "title": item.title,
            "summary": item.summary or "暂无摘要。",
            "source": item.source,
            "url": item.url,
        }
        for item in items[:12]
    ]
    return {
        "executive_summary": "本周抓取到多条与俄乌战争相关的公开报道和分析。由于 AI 综述不可用，下列内容按来源权重和关键词相关性排序，供进一步阅读。",
        "battlefield": "需结合 ISW、乌克兰媒体和主流国际媒体逐条核对战场态势。",
        "air_and_missile": "本周相关报道中包含无人机、导弹、防空或远程打击关键词的内容会在重点条目中体现。",
        "diplomacy_and_aid": "外交、援助和制裁相关内容来自所列公开来源，需要结合官方声明验证。",
        "risks": "公开报道存在延迟、宣传和不完整性；前线态势尤其需要交叉验证。",
        "source_note": "、".join(f"{source}({count})" for source, count in source_counts.most_common()),
        "highlights": highlights,
    }


def ai_analyze(items: list[WarItem], model: str, api_key_env: str, base_url: str) -> dict:
    api_key = os.environ.get(api_key_env)
    if not api_key or not items:
        return fallback_analysis(items)

    source_payload = [item.__dict__ for item in items]
    system = (
        "你是一个严谨的军事与国际关系分析员。请基于给定新闻条目生成中文俄乌战争周报。"
        "必须区分事实、分析和不确定性。不要编造未出现在条目中的具体战果、地点或数字。"
        "输出 JSON，不要 Markdown。"
    )
    user = {
        "task": "生成最近一周俄乌战争进展周报。",
        "requirements": [
            "用中文。",
            "先给执行摘要。",
            "分别总结：战场态势、空袭/无人机/导弹、防务援助与外交、风险和不确定性。",
            "挑选 8-15 条重点新闻，每条说明为什么重要。",
            "所有结论必须能从给定条目中推导；不确定就写不确定。",
        ],
        "items": source_payload,
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
        ],
        "temperature": 0.2,
        "max_tokens": 5000,
        "response_format": {"type": "json_object"},
    }
    try:
        resp = post_json(
            base_url.rstrip("/") + "/chat/completions",
            payload,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        content = resp["choices"][0]["message"]["content"]
        parsed = extract_json_object(content)
        return parsed or fallback_analysis(items)
    except Exception as exc:
        print(f"AI analysis failed: {exc}", file=sys.stderr)
        return fallback_analysis(items)


def as_text(value) -> str:
    if isinstance(value, list):
        return "；".join(str(v) for v in value if v)
    return str(value or "").strip()


def render_markdown(items: list[WarItem], analysis: dict, hours: int) -> str:
    now = datetime.now(timezone.utc)
    date = now.strftime("%Y-%m-%d")
    week = now.strftime("%G-W%V")
    since = (now - timedelta(hours=hours)).strftime("%Y-%m-%d")
    sources = Counter(item.source for item in items)
    source_line = "、".join(f"{source}({count})" for source, count in sources.most_common()) or "无"

    lines = [
        "---",
        "layout: default",
        f"title: \"俄乌战争一周进展: {week}\"",
        f"date: {date}",
        "lang: zh",
        "category: ukraine-war-weekly",
        f"period: {week}",
        "---",
        "",
        f"> 俄乌战争周报（{week}）：统计窗口约为最近 {hours} 小时，自 {since} 起。",
        "",
        f"本期参考 {len(items)} 条公开报道和分析。来源分布：{source_line}。",
        "",
        "## 执行摘要",
        "",
        as_text(analysis.get("executive_summary")) or "本期暂无足够信息生成执行摘要。",
        "",
        "## 分主题进展",
        "",
        f"**战场态势**：{as_text(analysis.get('battlefield'))}",
        "",
        f"**空袭、无人机与导弹**：{as_text(analysis.get('air_and_missile'))}",
        "",
        f"**防务援助与外交**：{as_text(analysis.get('diplomacy_and_aid'))}",
        "",
        f"**风险与不确定性**：{as_text(analysis.get('risks'))}",
        "",
        "---",
        "",
        "## 重点条目",
        "",
    ]

    highlights = analysis.get("highlights") or []
    if not isinstance(highlights, list):
        highlights = []

    if highlights:
        for idx, item in enumerate(highlights, start=1):
            if not isinstance(item, dict):
                continue
            title = item.get("title") or f"重点 {idx}"
            url = item.get("url") or ""
            source = item.get("source") or "未标注来源"
            summary = item.get("summary") or item.get("why_important") or "暂无说明。"
            if url:
                lines += [f"### {idx}. [{title}]({url})"]
            else:
                lines += [f"### {idx}. {title}"]
            lines += ["", summary, "", f"**来源**：{source}", ""]
    else:
        lines += ["本期没有足够条目进入重点列表。", ""]

    lines += ["---", "", "## 原始来源列表", ""]
    for idx, item in enumerate(items, start=1):
        lines.append(f"{idx}. [{item.title}]({item.url}) — {item.source}，{item.published_at}")
    lines += ["", "## 说明", "", "本周报基于公开 RSS 来源自动生成，适合作为态势跟踪入口，不应替代官方通报、军事地图或多源情报核验。"]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours", type=int, default=168)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--per-feed-limit", type=int, default=12)
    parser.add_argument("--output-dir", default="docs/_posts")
    parser.add_argument("--model", default=os.environ.get("HORIZON_UKRAINE_WEEKLY_MODEL", DEFAULT_MODEL))
    parser.add_argument("--base-url", default=os.environ.get("HORIZON_UKRAINE_WEEKLY_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--no-ai", action="store_true")
    args = parser.parse_args()

    items = collect_items(hours=args.hours, limit=args.limit, per_feed_limit=args.per_feed_limit)
    print(f"Collected {len(items)} Russia-Ukraine war items.")
    if args.no_ai:
        analysis = fallback_analysis(items)
    else:
        analysis = ai_analyze(items, model=args.model, api_key_env=args.api_key_env, base_url=args.base_url)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = out_dir / f"{today}-ukraine-war-weekly-zh.md"
    out_path.write_text(render_markdown(items, analysis, args.hours), encoding="utf-8")
    print(f"Wrote {out_path}")
    time.sleep(0.1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
