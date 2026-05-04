"""
Minimal MVP scraper for macro/regulatory signals: FRED + Federal Register.

FRED: Only fetch key series (CPI, Unemployment, Fed Funds Rate, Term Spread)
Federal Register: Only capture entries containing keywords such as AI, semiconductor, export control, antitrust, cybersecurity, critical minerals.
"""

import asyncio
import httpx
import feedparser
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

OUTPUT_DIR = Path("docs/_signals")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FRED_SERIES = {
    "CPI": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL",
    "Unemployment": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE",
    "Fed Funds Rate": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS",
    "10Y-2Y Spread": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y2Y",
}

FEDERAL_REGISTER_RSS = [
    {
        "name": "Federal Register",
        "url": "https://www.federalregister.gov/documents.rss",
        "keywords": ["AI", "semiconductor", "export control", "antitrust", "cybersecurity", "critical minerals"],
    }
]

async def fetch_fred_series(name, url):
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        # Minimal: return last 7 days of lines
        lines = resp.text.strip().split('\n')
        header = lines[0]
        data = lines[-7:] if len(lines) > 7 else lines[1:]
        return {"series": name, "data": data}

async def fetch_federal_register(feed):
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(feed['url'])
        resp.raise_for_status()
        parsed = feedparser.parse(resp.content)

    items = []
    since = datetime.now(timezone.utc) - timedelta(days=7)
    for entry in parsed.entries:
        pub = getattr(entry, 'published_parsed', None)
        pub_dt = datetime(*pub[:6], tzinfo=timezone.utc) if pub else datetime.now(timezone.utc)
        if pub_dt < since:
            continue
        text = (getattr(entry, 'title', '') + ' ' + getattr(entry, 'summary', '')).lower()
        if any(kw.lower() in text for kw in feed['keywords']):
            items.append({
                "title": entry.title,
                "url": entry.link,
                "published": pub_dt.isoformat(),
                "summary": getattr(entry, 'summary', ''),
            })
    return items

async def main():
    fred_results = await asyncio.gather(*(fetch_fred_series(name, url) for name, url in FRED_SERIES.items()))
    fr_results = await asyncio.gather(*(fetch_federal_register(feed) for feed in FEDERAL_REGISTER_RSS))

    signals = {
        "fred": fred_results,
        "federal_register": [item for sublist in fr_results for item in sublist],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    out_file = OUTPUT_DIR / f"signals_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    with out_file.open('w', encoding='utf-8') as f:
        json.dump(signals, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(signals['federal_register'])} federal register items and {len(signals['fred'])} FRED series to {out_file}")

if __name__ == '__main__':
    asyncio.run(main())
