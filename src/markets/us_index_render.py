"""Markdown rendering for the weekly US index monitor."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .us_index_core import week_id


def fmt_pct(value: float | None) -> str:
    return "n/a" if value is None else f"{value * 100:.1f}%"


def fmt_num(value: float | None, decimals: int = 2) -> str:
    return "n/a" if value is None else f"{value:.{decimals}f}"


def fmt_bp(value: float | None) -> str:
    return "n/a" if value is None else f"{value * 100:.0f} bp"


def render_us_index_markdown(report: dict[str, Any]) -> str:
    config = report["config"]
    metrics = report["metrics"]
    alerts = report["alerts"]
    now = datetime.fromisoformat(report["generated_at"])
    today = report["date"]
    wid = report["week_id"]

    spy = metrics.get("prices", {}).get("SPY", {})
    qqq = metrics.get("prices", {}).get("QQQ", {})
    vix = metrics.get("prices", {}).get("VIX", {})
    rel = metrics.get("relative", {}).get("QQQ_SPY", {})
    rsp = metrics.get("relative", {}).get("RSP_SPY", {})
    qqew = metrics.get("relative", {}).get("QQEW_QQQ", {})
    portfolio = metrics.get("portfolio", {})

    lines = [
        "---",
        "layout: default",
        f'title: "S&P 500 + Nasdaq-100 每周监控: {wid}"',
        f"date: {today}",
        "category: us-index-weekly",
        "lang: zh",
        "---",
        "",
        f"# S&P 500 + Nasdaq-100 每周监控: {week_id(now)}",
        "",
        "> 本系统用于长期指数投资风险监控，不构成短线交易建议。",
        "",
        "## 本周结论",
        "",
    ]
    if alerts:
        lines.extend([f"- **{a['level']} / {a['type']}**：{a['message']}" for a in alerts])
    else:
        lines.append("- 当前没有触发策略变更。继续按既定长期投资政策执行。")

    lines.extend([
        f"- SPY 当前回撤：{fmt_pct(spy.get('drawdown'))}；QQQ 当前回撤：{fmt_pct(qqq.get('drawdown'))}。",
        f"- QQQ/SPY 本周变化：{fmt_pct(rel.get('return_1w'))}。",
        f"- VIX 当前值：{fmt_num(vix.get('last'))}。",
        "",
        "## 指数状态",
        "",
        "| 指标 | SPY | QQQ |",
        "|---|---:|---:|",
        f"| 当前价格 | {fmt_num(spy.get('last'))} | {fmt_num(qqq.get('last'))} |",
        f"| 1周收益 | {fmt_pct(spy.get('return_1w'))} | {fmt_pct(qqq.get('return_1w'))} |",
        f"| 1月收益 | {fmt_pct(spy.get('return_1m'))} | {fmt_pct(qqq.get('return_1m'))} |",
        f"| 1年收益 | {fmt_pct(spy.get('return_1y'))} | {fmt_pct(qqq.get('return_1y'))} |",
        f"| 当前回撤 | {fmt_pct(spy.get('drawdown'))} | {fmt_pct(qqq.get('drawdown'))} |",
        f"| 高于200日均线 | {spy.get('above_200dma')} | {qqq.get('above_200dma')} |",
        f"| 30日年化波动率 | {fmt_pct(spy.get('vol_30d'))} | {fmt_pct(qqq.get('vol_30d'))} |",
        f"| 90日年化波动率 | {fmt_pct(spy.get('vol_90d'))} | {fmt_pct(qqq.get('vol_90d'))} |",
        "",
        "## 相对表现与宽度代理",
        "",
        f"- QQQ/SPY 比率：{fmt_num(rel.get('latest'), 4)}；本周变化：{fmt_pct(rel.get('return_1w'))}；1月变化：{fmt_pct(rel.get('return_1m'))}。",
        f"- RSP/SPY 本周变化：{fmt_pct(rsp.get('return_1w'))}；用于观察 S&P 500 是否主要由权重股驱动。",
        f"- QQEW/QQQ 本周变化：{fmt_pct(qqew.get('return_1w'))}；用于观察 Nasdaq-100 内部上涨是否集中。",
        "",
        "## 宏观环境",
        "",
        "| 指标 | 最新值 | 周变化 | 月变化 | 日期 |",
        "|---|---:|---:|---:|---:|",
    ])
    for series_id, label in config.get("fred_series", {}).items():
        macro = metrics.get("macro", {}).get(series_id, {})
        lines.append(
            f"| {label} ({series_id}) | {fmt_num(macro.get('latest'))} | "
            f"{fmt_bp(macro.get('weekly_change'))} | {fmt_bp(macro.get('monthly_change'))} | {macro.get('date') or 'n/a'} |"
        )

    targets = portfolio.get("targets", {})
    current = portfolio.get("current", {})
    deviation = portfolio.get("deviation", {})
    lines.extend([
        "",
        "## 组合纪律检查",
        "",
        f"- 目标配置：SPY {fmt_pct(targets.get('SPY'))}，QQQ {fmt_pct(targets.get('QQQ'))}。",
        f"- 当前配置：SPY {fmt_pct(current.get('SPY'))}，QQQ {fmt_pct(current.get('QQQ'))}，现金 {fmt_pct(current.get('cash'))}。",
        f"- 权重偏离：SPY {fmt_pct(deviation.get('SPY'))}，QQQ {fmt_pct(deviation.get('QQQ'))}。",
        f"- 系统纪律信号：`{portfolio.get('rebalance_signal', 'n/a')}`。",
        "",
        "## 行动建议",
        "",
        "- 本报告不提供短线买卖建议。",
        "- 如果 QQQ 超配，未来新增资金优先补 SPY，避免科技成长股过度集中。",
        "- 如果市场进入大幅回撤区间，继续按投资政策执行，不用情绪替代规则。",
        "",
    ])
    return "\n".join(lines)
