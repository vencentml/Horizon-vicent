"""Core calculations for the weekly US index monitor."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .metrics import (
    above_moving_average,
    annualized_volatility,
    change_over_period,
    latest,
    max_drawdown_from_high,
    rebalance_signal,
    trailing_return,
    weight_deviation,
)


def week_id(now: datetime) -> str:
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


def compute_price_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    closes = [row["close"] for row in rows]
    return {
        "date": rows[-1]["date"] if rows else None,
        "last": latest(closes),
        "drawdown": max_drawdown_from_high(closes),
        "above_200dma": above_moving_average(closes, 200),
        "return_1w": trailing_return(closes, 5),
        "return_1m": trailing_return(closes, 21),
        "return_1y": trailing_return(closes, 252),
        "vol_30d": annualized_volatility(closes, 30),
        "vol_90d": annualized_volatility(closes, 90),
    }


def compute_ratio_metrics(numerator_rows: list[dict[str, Any]], denominator_rows: list[dict[str, Any]]) -> dict[str, Any]:
    numerator = {row["date"]: row["close"] for row in numerator_rows}
    denominator = {row["date"]: row["close"] for row in denominator_rows}
    dates = sorted(set(numerator) & set(denominator))
    values = [numerator[d] / denominator[d] for d in dates if denominator[d] != 0]
    return {
        "latest": latest(values),
        "return_1w": trailing_return(values, 5),
        "return_1m": trailing_return(values, 21),
    }


def compute_fred_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    values = [row["value"] for row in rows]
    return {
        "date": rows[-1]["date"] if rows else None,
        "latest": latest(values),
        "weekly_change": change_over_period(values, 5),
        "monthly_change": change_over_period(values, 21),
    }


def compute_portfolio_metrics(config: dict[str, Any]) -> dict[str, Any]:
    portfolio = config.get("portfolio", {})
    current = portfolio.get("current", {})
    targets = portfolio.get("targets", {})
    rules = portfolio.get("rules", {})
    signal = rebalance_signal(
        current,
        targets,
        rules.get("rebalance_band", 0.05),
        rules.get("max_qqq_weight", 0.3),
    )
    return {
        "targets": targets,
        "current": current,
        "deviation": weight_deviation(current, targets),
        "rebalance_signal": signal,
    }


def build_metrics(
    price_rows: dict[str, list[dict[str, Any]]],
    fred_rows: dict[str, list[dict[str, Any]]],
    config: dict[str, Any],
) -> dict[str, Any]:
    return {
        "prices": {symbol: compute_price_metrics(rows) for symbol, rows in price_rows.items()},
        "relative": {
            "QQQ_SPY": compute_ratio_metrics(price_rows.get("QQQ", []), price_rows.get("SPY", [])),
            "RSP_SPY": compute_ratio_metrics(price_rows.get("RSP", []), price_rows.get("SPY", [])),
            "QQEW_QQQ": compute_ratio_metrics(price_rows.get("QQEW", []), price_rows.get("QQQ", [])),
        },
        "macro": {series_id: compute_fred_metrics(rows) for series_id, rows in fred_rows.items()},
        "portfolio": compute_portfolio_metrics(config),
    }


def build_alerts(config: dict[str, Any], metrics: dict[str, Any]) -> list[dict[str, str]]:
    thresholds = config.get("thresholds", {})
    alerts: list[dict[str, str]] = []
    spy = metrics.get("prices", {}).get("SPY", {})
    qqq = metrics.get("prices", {}).get("QQQ", {})
    vix = metrics.get("prices", {}).get("VIX", {})
    rel = metrics.get("relative", {}).get("QQQ_SPY", {})

    spy_dd = spy.get("drawdown")
    if spy_dd is not None and spy_dd <= thresholds.get("spy_drawdown_bear", -0.2):
        alerts.append({"level": "warning", "type": "spy_bear_drawdown", "message": "SPY 回撤进入熊市区间；这不是卖出信号，而是风险状态提示。"})
    elif spy_dd is not None and spy_dd <= thresholds.get("spy_drawdown_warning", -0.1):
        alerts.append({"level": "info", "type": "spy_drawdown", "message": "SPY 回撤进入关注区间；市场下跌本身不是卖出条件。"})

    qqq_dd = qqq.get("drawdown")
    if qqq_dd is not None and qqq_dd <= thresholds.get("qqq_drawdown_severe", -0.3):
        alerts.append({"level": "warning", "type": "qqq_severe_drawdown", "message": "QQQ 出现严重回撤，成长股风险压力显著。"})
    elif qqq_dd is not None and qqq_dd <= thresholds.get("qqq_drawdown_warning", -0.2):
        alerts.append({"level": "info", "type": "qqq_drawdown", "message": "QQQ 进入成长股高压力区间，避免情绪化操作。"})

    vix_last = vix.get("last")
    if vix_last is not None and vix_last >= thresholds.get("vix_extreme", 40):
        alerts.append({"level": "warning", "type": "vix_extreme", "message": "VIX 处于极端恐慌区间；不要用恐慌情绪替代投资政策。"})
    elif vix_last is not None and vix_last >= thresholds.get("vix_stress", 30):
        alerts.append({"level": "warning", "type": "vix_stress", "message": "VIX 显示市场压力显著上升。"})
    elif vix_last is not None and vix_last >= thresholds.get("vix_warning", 20):
        alerts.append({"level": "info", "type": "vix_warning", "message": "VIX 显示风险偏好下降。"})

    rel_1w = rel.get("return_1w")
    if rel_1w is not None and abs(rel_1w) >= thresholds.get("relative_performance_alert", 0.05):
        direction = "跑赢" if rel_1w > 0 else "跑输"
        alerts.append({"level": "info", "type": "qqq_spy_relative_move", "message": f"QQQ/SPY 本周明显{direction}，科技成长暴露的相对表现发生变化。"})

    signal = metrics.get("portfolio", {}).get("rebalance_signal")
    if signal and signal != "within_policy_band":
        alerts.append({"level": "info", "type": signal, "message": "组合权重偏离政策区间；未来新增资金优先修正偏离，而不是追涨。"})

    return alerts
