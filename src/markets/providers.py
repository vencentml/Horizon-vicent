"""CSV and JSON parsers for market monitoring data providers."""

from __future__ import annotations

import csv
import io
from datetime import datetime, timezone
from typing import Any


def parse_stooq_csv(text: str | None) -> list[dict[str, Any]]:
    """Parse Stooq daily CSV rows into date/close records."""
    rows: list[dict[str, Any]] = []
    if not text:
        return rows
    for row in csv.DictReader(io.StringIO(text)):
        try:
            rows.append({"date": row["Date"], "close": float(row["Close"])})
        except Exception:
            continue
    return sorted(rows, key=lambda item: item["date"])


def parse_fred_csv(text: str | None, series_id: str) -> list[dict[str, Any]]:
    """Parse FRED graph CSV rows into date/value records."""
    rows: list[dict[str, Any]] = []
    if not text:
        return rows
    for row in csv.DictReader(io.StringIO(text)):
        value = row.get(series_id)
        if value in (None, "", "."):
            continue
        try:
            rows.append({"date": row["observation_date"], "value": float(value)})
        except Exception:
            continue
    return sorted(rows, key=lambda item: item["date"])


def parse_yahoo_chart(payload: dict[str, Any] | None) -> list[dict[str, Any]]:
    """Parse Yahoo Finance chart JSON into date/close records."""
    if not payload:
        return []
    try:
        result = payload["chart"]["result"][0]
        timestamps = result.get("timestamp") or []
        closes = result["indicators"]["quote"][0].get("close") or []
    except Exception:
        return []

    rows: list[dict[str, Any]] = []
    for timestamp, close in zip(timestamps, closes):
        if close is None:
            continue
        try:
            date = datetime.fromtimestamp(int(timestamp), tz=timezone.utc).date().isoformat()
            rows.append({"date": date, "close": float(close)})
        except Exception:
            continue
    return sorted(rows, key=lambda item: item["date"])
