"""Market metric calculations used by weekly index monitoring."""

from __future__ import annotations

from math import sqrt
from statistics import stdev


def pct_change(start: float | None, end: float | None) -> float | None:
    """Return percentage change from start to end as a decimal."""
    if start is None or end is None or start == 0:
        return None
    return end / start - 1


def max_drawdown_from_high(values: list[float]) -> float | None:
    """Return current drawdown from the historical high as a decimal."""
    clean = [v for v in values if v is not None and v > 0]
    if not clean:
        return None
    high = max(clean)
    latest = clean[-1]
    return latest / high - 1


def moving_average(values: list[float], window: int) -> float | None:
    """Return trailing moving average."""
    clean = [v for v in values if v is not None]
    if len(clean) < window:
        return None
    return sum(clean[-window:]) / window


def above_moving_average(values: list[float], window: int) -> bool | None:
    """Return whether latest value is above trailing moving average."""
    ma = moving_average(values, window)
    clean = [v for v in values if v is not None]
    if ma is None or not clean:
        return None
    return clean[-1] >= ma


def trailing_return(values: list[float], periods: int) -> float | None:
    """Return trailing return over a number of observations."""
    clean = [v for v in values if v is not None and v > 0]
    if len(clean) <= periods:
        return None
    return pct_change(clean[-periods - 1], clean[-1])


def annualized_volatility(values: list[float], periods: int, trading_days: int = 252) -> float | None:
    """Return trailing annualized volatility from daily closes."""
    clean = [v for v in values if v is not None and v > 0]
    if len(clean) <= periods:
        return None
    window = clean[-periods - 1:]
    returns = [window[i] / window[i - 1] - 1 for i in range(1, len(window)) if window[i - 1] != 0]
    if len(returns) < 2:
        return None
    return stdev(returns) * sqrt(trading_days)


def latest(values: list[float]) -> float | None:
    clean = [v for v in values if v is not None]
    return clean[-1] if clean else None


def change_over_period(values: list[float], periods: int) -> float | None:
    """Return absolute change over a number of observations."""
    clean = [v for v in values if v is not None]
    if len(clean) <= periods:
        return None
    return clean[-1] - clean[-periods - 1]


def weight_deviation(current: dict[str, float], target: dict[str, float]) -> dict[str, float]:
    """Return current-minus-target weight deviation by symbol."""
    symbols = set(current) | set(target)
    return {symbol: current.get(symbol, 0.0) - target.get(symbol, 0.0) for symbol in symbols}


def rebalance_signal(
    current: dict[str, float],
    target: dict[str, float],
    rebalance_band: float,
    max_qqq_weight: float,
) -> str:
    """Return a discipline-oriented portfolio signal."""
    qqq_weight = current.get("QQQ", 0.0)
    qqq_target = target.get("QQQ", 0.0)
    if qqq_weight > max_qqq_weight:
        return "qqq_above_max_weight_future_contributions_to_spy"
    if qqq_weight - qqq_target > rebalance_band:
        return "qqq_overweight_future_contributions_to_spy"
    if target.get("SPY", 0.0) - current.get("SPY", 0.0) > rebalance_band:
        return "spy_underweight_future_contributions_to_spy"
    return "within_policy_band"
