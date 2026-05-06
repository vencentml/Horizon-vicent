"""CSV parsers for market monitoring data providers."""

from __future__ import annotations

import csv
import io
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
