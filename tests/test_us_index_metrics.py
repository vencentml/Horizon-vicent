"""Tests for market metric helpers."""

from src.markets.metrics import (
    above_moving_average,
    annualized_volatility,
    max_drawdown_from_high,
    moving_average,
    rebalance_signal,
    trailing_return,
    weight_deviation,
)


def test_max_drawdown_from_high() -> None:
    assert round(max_drawdown_from_high([100, 120, 90, 96]), 4) == -0.2


def test_moving_average() -> None:
    assert moving_average([1, 2, 3, 4], 3) == 3


def test_above_moving_average() -> None:
    assert above_moving_average([1, 2, 3, 4], 3) is True
    assert above_moving_average([4, 3, 2, 1], 3) is False


def test_trailing_return() -> None:
    assert trailing_return([100, 105, 110], 1) == 110 / 105 - 1


def test_annualized_volatility_returns_value() -> None:
    values = [100 + (i % 5) for i in range(40)]
    assert annualized_volatility(values, 30) is not None


def test_weight_deviation() -> None:
    result = weight_deviation({"SPY": 0.7, "QQQ": 0.3}, {"SPY": 0.8, "QQQ": 0.2})
    assert round(result["SPY"], 4) == -0.1
    assert round(result["QQQ"], 4) == 0.1


def test_rebalance_signal_within_band() -> None:
    assert rebalance_signal({"SPY": 0.8, "QQQ": 0.2}, {"SPY": 0.8, "QQQ": 0.2}, 0.05, 0.3) == "within_policy_band"


def test_rebalance_signal_qqq_overweight() -> None:
    assert rebalance_signal({"SPY": 0.73, "QQQ": 0.27}, {"SPY": 0.8, "QQQ": 0.2}, 0.05, 0.3) == "qqq_overweight_future_contributions_to_spy"


def test_rebalance_signal_qqq_above_max_weight() -> None:
    assert rebalance_signal({"SPY": 0.65, "QQQ": 0.35}, {"SPY": 0.8, "QQQ": 0.2}, 0.05, 0.3) == "qqq_above_max_weight_future_contributions_to_spy"
