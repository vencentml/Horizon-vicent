"""Generate the weekly S&P 500 + Nasdaq-100 monitoring report."""

from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from src.markets.providers import parse_fred_csv, parse_stooq_csv
from src.markets.us_index_core import build_alerts, build_metrics, week_id
from src.markets.us_index_render import render_us_index_markdown

CONFIG_PATH = Path("data/us_index_monitor.json")
POSTS_DIR = Path("docs/_posts")
STATUS_PATH = Path("docs/status/latest-us-index-weekly.json")
DATA_DIR = Path("docs/_data/market")


async def fetch_text(client: httpx.AsyncClient, url: str) -> str | None:
    try:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        return response.text
    except Exception as exc:
        print(f"WARN: failed to fetch {url}: {exc}")
        return None


async def fetch_stooq(client: httpx.AsyncClient, symbol: str) -> list[dict[str, Any]]:
    url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
    return parse_stooq_csv(await fetch_text(client, url))


async def fetch_fred(client: httpx.AsyncClient, series_id: str) -> list[dict[str, Any]]:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    return parse_fred_csv(await fetch_text(client, url), series_id)


async def main() -> None:
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    wid = week_id(now)
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    symbols: dict[str, Any] = {}
    for group in ("core", "breadth_proxies", "volatility"):
        symbols.update(config.get("symbols", {}).get(group, {}))

    async with httpx.AsyncClient(timeout=30.0, headers={"User-Agent": "Horizon/1.0"}) as client:
        price_rows = {
            symbol: await fetch_stooq(client, meta["stooq_symbol"])
            for symbol, meta in symbols.items()
        }
        fred_rows = {
            series_id: await fetch_fred(client, series_id)
            for series_id in config.get("fred_series", {})
        }

    metrics = build_metrics(price_rows, fred_rows, config)
    alerts = build_alerts(config, metrics)
    report = {
        "report": "us-index-weekly",
        "date": today,
        "week_id": wid,
        "generated_at": now.isoformat(),
        "status": "success",
        "config": config,
        "metrics": metrics,
        "alerts": alerts,
    }

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    post_path = POSTS_DIR / f"{today}-us-index-weekly-{wid}.md"
    post_path.write_text(render_us_index_markdown(report), encoding="utf-8")
    report["output"] = str(post_path)

    STATUS_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    data_path = DATA_DIR / f"us_index_weekly_{today.replace('-', '')}.json"
    data_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote {post_path}")
    print(f"Wrote {STATUS_PATH}")
    print(f"Wrote {data_path}")


if __name__ == "__main__":
    asyncio.run(main())
