"""
Lightweight arXiv fetcher for high-value papers only.

Only fetch papers matching selected keywords in title or abstract.
"""

import asyncio
import feedparser
from datetime import datetime, timedelta, timezone
from pathlib import Path
import httpx
import json

ARXIV_RSS_URLS = [
    "https://export.arxiv.org/rss/cs.AI",
    "https://export.arxiv.org/rss/cs.LG",
    "https://export.arxiv.org/rss/cs.CL",
    "https://export.arxiv.org/rss/cs.CV",
]

KEYWORDS = [
    "benchmark",
    "evaluation",
    "agent",
    "long context",
    "serving",
    "distillation",
    "cost",
    "performance",
    "open-source",
    "code",
    "reproducible",
    "deep learning",
    "transformer",
]

OUTPUT_DIR = Path("docs/_papers/arxiv")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

async def fetch_feed(url: str, days_back: int = 7):
    async with httpx.AsyncClient(timeout=30.0, headers={"User-Agent": "Horizon/1.0"}) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)

    since = datetime.now(timezone.utc) - timedelta(days=days_back)
    papers = []
    for entry in feed.entries:
        pub = getattr(entry, "published_parsed", None)
        if pub:
            pub_dt = datetime(*pub[:6], tzinfo=timezone.utc)
        else:
            pub_dt = datetime.now(timezone.utc)
        if pub_dt < since:
            continue

        text = (entry.title + ' ' + getattr(entry, 'summary', '')).lower()
        if any(k.lower() in text for k in KEYWORDS):
            papers.append({
                "title": entry.title,
                "url": entry.link,
                "published": pub_dt.isoformat(),
                "summary": getattr(entry, 'summary', '')
            })
    return papers

async def main():
    all_papers = []
    for url in ARXIV_RSS_URLS:
        try:
            papers = await fetch_feed(url)
            all_papers.extend(papers)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_file = OUTPUT_DIR / f"arxiv_light_{timestamp}.json"
    with out_file.open('w', encoding='utf-8') as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(all_papers)} papers to {out_file}")

if __name__ == "__main__":
    asyncio.run(main())
