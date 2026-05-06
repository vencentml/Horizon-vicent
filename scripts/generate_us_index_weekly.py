"""Generate the weekly S&P 500 + Nasdaq-100 monitoring report."""

from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from src.markets.providers import parse_fred_csv, parse_stooq_csv, parse_yahoo_chart
from src.markets.us_index_core import build_alerts, build_interpretations, build_metrics, week_id
from src.markets.us_index_render import render_us_index_markdown

CONFIG_PATH = Path("data/us_index_monitor.json")
POSTS_DIR = Path("docs/_posts")
STATUS_PATH = Path("docs/status/latest-us-index-weekly.json")
DATA_DIR = Path("docs/_data/market")
YAHOO_SYMBOLS = {"SPY": "SPY", "QQQ": "QQQ", "RSP": "RSP", "QQEW": "QQEW", "VIX": "^VIX"}


async def fetch_text(client: httpx.AsyncClient, url: str) -> str | None:
    try:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        return response.text
    except Exception as exc:
        print(f"WARN: failed to fetch {url}: {exc}")
        return None


async def fetch_json(client: httpx.AsyncClient, url: str) -> dict[str, Any] | None:
    try:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print(f"WARN: failed to fetch {url}: {exc}")
        return None


async def fetch_stooq(client: httpx.AsyncClient, symbol: str) -> list[dict[str, Any]]:
    return parse_stooq_csv(await fetch_text(client, f"https://stooq.com/q/d/l/?s={symbol}&i=d"))


async def fetch_yahoo_chart(client: httpx.AsyncClient, symbol: str) -> list[dict[str, Any]]:
    return parse_yahoo_chart(await fetch_json(client, f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=10y&interval=1d"))


async def fetch_price_rows(client: httpx.AsyncClient, symbol: str, stooq_symbol: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = await fetch_stooq(client, stooq_symbol)
    if rows:
        return rows, {"source": "stooq", "rows": len(rows), "status": "ok"}
    rows = await fetch_yahoo_chart(client, YAHOO_SYMBOLS.get(symbol, symbol))
    if rows:
        return rows, {"source": "yahoo_fallback", "rows": len(rows), "status": "ok"}
    return [], {"source": "none", "rows": 0, "status": "empty"}


async def fetch_fred(client: httpx.AsyncClient, series_id: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = parse_fred_csv(await fetch_text(client, f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"), series_id)
    return rows, {"source": "fred", "rows": len(rows), "status": "ok" if rows else "empty"}


async def main() -> None:
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    wid = week_id(now)
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    symbols: dict[str, Any] = {}
    for group in ("core", "breadth_proxies", "volatility"):
        symbols.update(config.get("symbols", {}).get(group, {}))

    async with httpx.AsyncClient(timeout=30.0, headers={"User-Agent": "Horizon/1.0"}) as client:
        price_results = {s: await fetch_price_rows(client, s, m["stooq_symbol"]) for s, m in symbols.items()}
        fred_results = {sid: await fetch_fred(client, sid) for sid in config.get("fred_series", {})}

    price_rows = {s: result[0] for s, result in price_results.items()}
    fred_rows = {sid: result[0] for sid, result in fred_results.items()}
    data_health = {
        "prices": {s: result[1] for s, result in price_results.items()},
        "macro": {sid: result[1] for sid, result in fred_results.items()},
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
        "data_health": data_health,
        "metrics": metrics,
        "alerts": alerts,
        "interpretations": build_interpretations(metrics),
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
