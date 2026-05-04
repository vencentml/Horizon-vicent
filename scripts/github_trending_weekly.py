#!/usr/bin/env python3
"""Generate a Chinese GitHub trending weekly Jekyll post.

The script fetches GitHub trending repositories, enriches repository metadata
with GitHub API data, and optionally asks a DeepSeek/OpenAI-compatible model to
explain each project in Chinese.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable


RSS_URL = "https://mshibanami.github.io/GitHubTrendingRSS/weekly/all.xml"
GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
DEFAULT_MODEL = "deepseek-v4-flash"


@dataclass
class RepoItem:
    name: str
    url: str
    description: str = ""
    language: str = ""
    stars: int | None = None
    forks: int | None = None
    topics: list[str] | None = None
    homepage: str = ""
    source: str = ""
    ai_intro: dict[str, str] | None = None


def _fetch_url(url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Horizon-GitHub-Trending-Weekly",
            **(headers or {}),
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _post_json(url: str, payload: dict, headers: dict[str, str], timeout: int = 60) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Horizon-GitHub-Trending-Weekly",
            **headers,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _strip_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def _full_name_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    parts = [p for p in parsed.path.strip("/").split("/") if p]
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return ""


def sample_items() -> list[RepoItem]:
    return [
        RepoItem(
            name="example/agent-runtime",
            url="https://github.com/example/agent-runtime",
            description="A runtime for tool-using AI agents with sandboxed execution.",
            language="Python",
            stars=12345,
            forks=678,
            topics=["agents", "sandbox", "llm", "automation"],
            homepage="https://example.com/agent-runtime",
            source="sample data",
        ),
        RepoItem(
            name="example/cuda-kernels",
            url="https://github.com/example/cuda-kernels",
            description="High-performance CUDA kernels for LLM inference and attention operators.",
            language="CUDA",
            stars=9876,
            forks=432,
            topics=["cuda", "llm", "inference", "gpu"],
            source="sample data",
        ),
    ]


def fetch_from_rss(limit: int) -> list[RepoItem]:
    try:
        raw = _fetch_url(RSS_URL)
    except Exception as exc:
        print(f"RSS fetch failed: {exc}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        print(f"RSS parse failed: {exc}", file=sys.stderr)
        return []

    items: list[RepoItem] = []
    for node in root.findall(".//item"):
        title = (node.findtext("title") or "").strip()
        link = (node.findtext("link") or "").strip()
        description = _strip_html(node.findtext("description") or "")
        if not title or not link:
            continue

        full_name = _full_name_from_url(link)
        name = full_name or title.replace("GitHub Trending - ", "").strip()
        items.append(
            RepoItem(
                name=name,
                url=link,
                description=description,
                source="GitHubTrendingRSS weekly feed",
            )
        )

    return items[:limit]


def fetch_from_github_search(hours: int, limit: int) -> list[RepoItem]:
    since = (datetime.now(timezone.utc) - timedelta(hours=hours)).date().isoformat()
    query = f"created:>={since} stars:>=20"
    params = urllib.parse.urlencode({
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": min(limit, 50),
    })
    url = f"{GITHUB_SEARCH_URL}?{params}"

    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        raw = _fetch_url(url, headers=headers)
        payload = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        print(f"GitHub Search fallback failed: {exc}", file=sys.stderr)
        return []

    items: list[RepoItem] = []
    for repo in payload.get("items", []):
        items.append(
            RepoItem(
                name=repo.get("full_name") or repo.get("name") or "unknown",
                url=repo.get("html_url") or "",
                description=repo.get("description") or "",
                language=repo.get("language") or "",
                stars=repo.get("stargazers_count"),
                forks=repo.get("forks_count"),
                topics=repo.get("topics") or [],
                homepage=repo.get("homepage") or "",
                source=f"GitHub Search: {query}",
            )
        )
    return items[:limit]


def enrich_from_github_api(items: list[RepoItem]) -> None:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    for item in items:
        full_name = item.name if "/" in item.name else _full_name_from_url(item.url)
        if not full_name or full_name.count("/") != 1:
            continue
        api_url = f"https://api.github.com/repos/{full_name}"
        try:
            payload = json.loads(_fetch_url(api_url, headers=headers).decode("utf-8"))
        except Exception as exc:
            print(f"Repo metadata fetch failed for {full_name}: {exc}", file=sys.stderr)
            continue

        item.name = payload.get("full_name") or item.name
        item.url = payload.get("html_url") or item.url
        item.description = payload.get("description") or item.description
        item.language = payload.get("language") or item.language
        item.stars = payload.get("stargazers_count", item.stars)
        item.forks = payload.get("forks_count", item.forks)
        item.topics = payload.get("topics") or item.topics or []
        item.homepage = payload.get("homepage") or item.homepage


def dedupe(items: Iterable[RepoItem]) -> list[RepoItem]:
    seen: set[str] = set()
    result: list[RepoItem] = []
    for item in items:
        key = item.url.rstrip("/") or item.name.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


def _extract_json_object(text: str) -> dict | None:
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


def _fallback_intro(item: RepoItem) -> dict[str, str]:
    desc = item.description.strip() or "该仓库暂无明确描述。"
    topics = "、".join(item.topics or []) or "未标注"
    return {
        "what_it_is": f"这是一个 GitHub 热门项目。仓库描述为：{desc}",
        "problem": "从仓库元数据看，它本周获得了较高关注，可能代表某个开发者工具、框架、库或应用方向正在升温。",
        "how_it_works": f"主要实现语言为 {item.language or '未标注'}，主题标签包括：{topics}。更准确的运行机制需要结合 README 和源码进一步分析。",
        "why_watch": "建议关注其 README、示例、issue 和 release，判断是否适合纳入自己的工具链或技术观察列表。",
    }


def ai_explain_items(items: list[RepoItem], model: str, api_key_env: str, base_url: str, sleep_sec: float) -> None:
    api_key = os.environ.get(api_key_env)
    if not api_key:
        print(f"{api_key_env} is not set; using fallback Chinese summaries.", file=sys.stderr)
        for item in items:
            item.ai_intro = _fallback_intro(item)
        return

    url = base_url.rstrip("/") + "/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    system = (
        "你是一个资深开源技术分析师。请把 GitHub 仓库信息转成准确、简洁、中文的项目解读。"
        "只根据给定元数据推断，不要编造不存在的功能；不确定时要明确说可能。"
        "输出必须是 JSON 对象，不要 Markdown。"
    )

    for idx, item in enumerate(items, start=1):
        user = {
            "repo": item.name,
            "url": item.url,
            "description": item.description,
            "language": item.language,
            "stars": item.stars,
            "forks": item.forks,
            "topics": item.topics or [],
            "homepage": item.homepage,
            "task": (
                "请用中文解释这个项目。返回字段："
                "what_it_is（一句话说明它是什么），"
                "problem（它解决什么问题或服务什么场景），"
                "how_it_works（从语言、仓库描述和 topic 推断其大致运行原理/技术机制；不确定就写基于元数据推测），"
                "why_watch（为什么本周值得关注或谁应该关注）。"
                "每个字段 1-3 句话。"
            ),
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
            ],
            "temperature": 0.2,
            "max_tokens": 1200,
            "response_format": {"type": "json_object"},
        }

        try:
            resp = _post_json(url, payload, headers=headers)
            content = resp["choices"][0]["message"]["content"]
            parsed = _extract_json_object(content)
            item.ai_intro = parsed or _fallback_intro(item)
            print(f"AI explained {idx}/{len(items)}: {item.name}")
        except Exception as exc:
            print(f"AI explanation failed for {item.name}: {exc}", file=sys.stderr)
            item.ai_intro = _fallback_intro(item)

        if sleep_sec > 0:
            time.sleep(sleep_sec)


def render_markdown(items: list[RepoItem], hours: int) -> str:
    now = datetime.now(timezone.utc)
    date = now.strftime("%Y-%m-%d")
    week = now.strftime("%G-W%V")
    since = (now - timedelta(hours=hours)).strftime("%Y-%m-%d")

    languages = Counter(item.language for item in items if item.language)
    lang_line = "、".join(f"{lang}({count})" for lang, count in languages.most_common(8)) or "未标注"

    lines = [
        "---",
        "layout: default",
        f"title: \"GitHub 热门项目周报: {week}\"",
        f"date: {date}",
        "lang: zh",
        "category: github-weekly",
        f"period: {week}",
        "---",
        "",
        f"> GitHub 热门项目周报（{week}）：统计窗口约为最近 {hours} 小时，自 {since} 起。",
        "",
        f"本期收录 {len(items)} 个项目。主要语言分布：{lang_line}。每个项目均包含中文解释、适用场景和基于仓库元数据推断的运行原理。",
        "",
        "---",
        "",
    ]

    if not items:
        lines += [
            "本期没有抓取到足够的 GitHub 热门项目。可能原因是 RSS 源暂时不可用，或 GitHub Search API 没有返回符合条件的结果。",
            "",
        ]
        return "\n".join(lines)

    lines += ["## 快速目录", ""]
    for idx, item in enumerate(items, start=1):
        stars = f" ⭐ {item.stars}" if item.stars is not None else ""
        language = f" · {item.language}" if item.language else ""
        lines.append(f"{idx}. [{item.name}](#item-{idx}){stars}{language}")
    lines += ["", "---", ""]

    for idx, item in enumerate(items, start=1):
        stars = f"⭐ {item.stars}" if item.stars is not None else ""
        forks = f"Forks {item.forks}" if item.forks is not None else ""
        language = item.language or "未标注语言"
        topics = "、".join(item.topics or []) or "未标注"
        meta = " · ".join(part for part in [language, stars, forks] if part)
        intro = item.ai_intro or _fallback_intro(item)
        source = item.source or "GitHub Trending"

        lines += [
            f'<a id="item-{idx}"></a>',
            f"## {idx}. [{item.name}]({item.url})",
            "",
            f"**它是什么**：{intro.get('what_it_is', '').strip()}",
            "",
            f"**解决什么问题**：{intro.get('problem', '').strip()}",
            "",
            f"**大致运行原理**：{intro.get('how_it_works', '').strip()}",
            "",
            f"**为什么值得关注**：{intro.get('why_watch', '').strip()}",
            "",
            f"**元信息**：{meta}" if meta else "**元信息**：暂无",
            "",
            f"**Topics**：{topics}",
            "",
        ]
        if item.homepage:
            lines += [f"**项目主页**：{item.homepage}", ""]
        lines += [
            f"**来源**：{source}",
            "",
            "---",
            "",
        ]

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours", type=int, default=168)
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--output-dir", default="docs/_posts")
    parser.add_argument("--model", default=os.environ.get("HORIZON_GITHUB_WEEKLY_MODEL", DEFAULT_MODEL))
    parser.add_argument("--base-url", default=os.environ.get("HORIZON_GITHUB_WEEKLY_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--ai-sleep-sec", type=float, default=0.0)
    parser.add_argument("--no-ai", action="store_true")
    parser.add_argument("--sample", action="store_true", help="Use built-in sample data for offline CI/self-checks.")
    args = parser.parse_args()

    if args.sample:
        items = sample_items()[: args.limit]
        print(f"Using {len(items)} built-in sample GitHub items.")
    else:
        rss_items = fetch_from_rss(args.limit)
        search_items = []
        if not rss_items:
            search_items = fetch_from_github_search(args.hours, args.limit)
        items = dedupe(rss_items or search_items)[: args.limit]
        enrich_from_github_api(items)
        print(f"Generated GitHub weekly report from {len(rss_items)} RSS items and {len(search_items)} search fallback items.")
        print(f"Final item count: {len(items)}")

    if args.no_ai:
        for item in items:
            item.ai_intro = _fallback_intro(item)
    else:
        ai_explain_items(
            items,
            model=args.model,
            api_key_env=args.api_key_env,
            base_url=args.base_url,
            sleep_sec=args.ai_sleep_sec,
        )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = out_dir / f"{today}-github-trending-weekly-zh.md"
    out_path.write_text(render_markdown(items, args.hours), encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
