#!/usr/bin/env python3
"""Generate a GitHub trending weekly Jekyll post.

This script first tries the GitHubTrendingRSS weekly feed. If that feed is
unavailable or empty, it falls back to GitHub Search API for repositories
created within the selected time window, sorted by stars.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
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


@dataclass
class RepoItem:
    name: str
    url: str
    description: str = ""
    language: str = ""
    stars: int | None = None
    forks: int | None = None
    source: str = ""


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


def _strip_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


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

        # Feed titles are typically owner/repo or include the repo name.
        name = title.replace("GitHub Trending - ", "").strip()
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
                source=f"GitHub Search: {query}",
            )
        )
    return items[:limit]


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


def render_markdown(items: list[RepoItem], hours: int, limit: int) -> str:
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
        f"本期收录 {len(items)} 个项目。主要语言分布：{lang_line}。",
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
        meta = " · ".join(part for part in [language, stars, forks] if part)
        description = item.description.strip() or "暂无描述。"
        source = item.source or "GitHub Trending"

        lines += [
            f'<a id="item-{idx}"></a>',
            f"## {idx}. [{item.name}]({item.url})",
            "",
            description,
            "",
            f"**元信息**：{meta}" if meta else "**元信息**：暂无",
            "",
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
    args = parser.parse_args()

    rss_items = fetch_from_rss(args.limit)
    search_items = []
    if not rss_items:
        search_items = fetch_from_github_search(args.hours, args.limit)

    items = dedupe(rss_items or search_items)[: args.limit]
    print(f"Generated GitHub weekly report from {len(rss_items)} RSS items and {len(search_items)} search fallback items.")
    print(f"Final item count: {len(items)}")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = out_dir / f"{today}-github-trending-weekly-zh.md"
    out_path.write_text(render_markdown(items, args.hours, args.limit), encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
