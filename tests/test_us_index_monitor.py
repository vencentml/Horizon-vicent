"""Tests for the weekly US index monitor core."""

from src.markets.providers import parse_fred_csv, parse_stooq_csv
from src.markets.us_index_core import build_alerts, build_metrics, compute_fred_metrics, compute_price_metrics, compute_ratio_metrics


def _price_rows(values: list[float]) -> list[dict]:
    return [{"date": f"2026-01-{i + 1:02d}", "close": v} for i, v in enumerate(values)]


def test_parse_stooq_csv() -> None:
    text = "Date,Open,High,Low,Close,Volume\n2026-01-01,1,1,1,100,10\n2026-01-02,1,1,1,101,10\n"
    rows = parse_stooq_csv(text)
    assert rows == [{"date": "2026-01-01", "close": 100.0}, {"date": "2026-01-02", "close": 101.0}]


def test_parse_fred_csv() -> None:
    text = "observation_date,DGS10\n2026-01-01,4.2\n2026-01-02,.\n2026-01-03,4.3\n"
    rows = parse_fred_csv(text, "DGS10")
    assert rows == [{"date": "2026-01-01", "value": 4.2}, {"date": "2026-01-03", "value": 4.3}]


def test_compute_price_metrics() -> None:
    rows = _price_rows([100 + i for i in range(260)])
    metrics = compute_price_metrics(rows)
    assert metrics["last"] == 359
    assert metrics["drawdown"] == 0
    assert metrics["above_200dma"] is True
    assert metrics["return_1w"] is not None
    assert metrics["vol_30d"] is not None


def test_compute_ratio_metrics() -> None:
    qqq = _price_rows([200, 202, 204, 206, 208, 210, 212])
    spy = _price_rows([100, 100, 100, 100, 100, 100, 100])
    result = compute_ratio_metrics(qqq, spy)
    assert result["latest"] == 2.12
    assert result["return_1w"] is not None


def test_compute_fred_metrics() -> None:
    rows = [{"date": f"2026-01-{i + 1:02d}", "value": float(i)} for i in range(30)]
    result = compute_fred_metrics(rows)
    assert result["latest"] == 29.0
    assert result["weekly_change"] == 5.0
    assert result["monthly_change"] == 21.0


def test_build_metrics_and_alerts() -> None:
    config = {
        "thresholds": {"spy_drawdown_warning": -0.1, "spy_drawdown_bear": -0.2, "qqq_drawdown_warning": -0.2, "qqq_drawdown_severe": -0.3, "vix_warning": 20, "vix_stress": 30, "vix_extreme": 40, "relative_performance_alert": 0.05},
        "portfolio": {"targets": {"SPY": 0.8, "QQQ": 0.2}, "current": {"SPY": 0.65, "QQQ": 0.35}, "rules": {"rebalance_band": 0.05, "max_qqq_weight": 0.3}},
    }
    price_rows = {
        "SPY": _price_rows([100, 120, 90, 91, 92, 93, 94]),
        "QQQ": _price_rows([100, 100, 70, 71, 72, 73, 74]),
        "VIX": _price_rows([10, 20, 35, 34, 33, 32, 31]),
    }
    metrics = build_metrics(price_rows, {}, config)
    alerts = build_alerts(config, metrics)
    types = {alert["type"] for alert in alerts}
    assert "spy_bear_drawdown" in types
    assert "qqq_severe_drawdown" in types
    assert "vix_stress" in types
    assert "qqq_above_max_weight_future_contributions_to_spy" in types
