"""User-friendly markdown renderer for the weekly US index monitor."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .us_index_core import week_id

LABELS = {
    "DGS10": "10年期美债利率",
    "DFII10": "10年期实际利率",
    "FEDFUNDS": "联邦基金利率",
    "CPIAUCSL": "CPI 通胀指数",
    "CPILFESL": "核心 CPI 通胀指数",
    "UNRATE": "失业率",
    "BAMLH0A0HYM2": "高收益债信用利差",
}
RATE_SERIES = {"DGS10", "DFII10", "FEDFUNDS", "BAMLH0A0HYM2"}
PP_SERIES = {"UNRATE"}
INDEX_SERIES = {"CPIAUCSL", "CPILFESL"}


def pct(v: float | None) -> str:
    return "n/a" if v is None else f"{v * 100:.1f}%"


def num(v: float | None) -> str:
    return "n/a" if v is None else f"{v:.2f}"


def yn(v: bool | None) -> str:
    return "是" if v is True else "否" if v is False else "n/a"


def macro_delta(sid: str, v: float | None) -> str:
    if v is None:
        return "n/a"
    if sid in RATE_SERIES:
        return f"{v * 100:.0f} 基点"
    if sid in PP_SERIES:
        return f"{v:.2f} 个百分点"
    if sid in INDEX_SERIES:
        return f"{v:.2f} 点"
    return num(v)


def pressure(vix: float | None) -> str:
    if vix is None:
        return "数据不足"
    if vix < 20:
        return "低"
    if vix < 30:
        return "中"
    return "高"


def todo(signal: str | None, alerts: list[dict[str, str]]) -> str:
    if signal and signal != "within_policy_band":
        return "未来新增资金优先修正配置偏离"
    if any(a.get("level") == "warning" for a in alerts):
        return "不做情绪化交易，按投资纪律观察风险"
    return "无需额外操作，继续按原计划执行"


def render_us_index_markdown(report: dict[str, Any]) -> str:
    cfg = report["config"]
    m = report["metrics"]
    alerts = report.get("alerts", [])
    notes = report.get("interpretations", [])
    now = datetime.fromisoformat(report["generated_at"])
    today, wid = report["date"], report["week_id"]
    prices, rels, macro = m.get("prices", {}), m.get("relative", {}), m.get("macro", {})
    port = m.get("portfolio", {})
    spy, qqq, vix = prices.get("SPY", {}), prices.get("QQQ", {}), prices.get("VIX", {})
    rel = rels.get("QQQ_SPY", {})
    rsp, qqew = rels.get("RSP_SPY", {}), rels.get("QQEW_QQQ", {})
    targets, current, dev = port.get("targets", {}), port.get("current", {}), port.get("deviation", {})
    signal = port.get("rebalance_signal", "n/a")
    p = pressure(vix.get("last"))
    status = "正常" if not alerts and signal == "within_policy_band" else "需要关注"

    lines = [
        "---",
        "layout: default",
        f'title: "美股指数每周监控: {wid}"',
        f"date: {today}",
        "category: us-index-weekly",
        "lang: zh",
        "---",
        "",
        f"# 美股指数每周监控: {week_id(now)}",
        "",
        "> 用于长期投资纪律：看风险、看配置偏离、看未来新增资金方向；不做短线择时。",
        "",
        "## 1. 本周你需要知道什么",
        "",
        "| 项目 | 本周状态 | 怎么理解 |",
        "|---|---|---|",
        f"| 总体状态 | **{status}** | 不是买卖信号，只是风险和纪律状态。 |",
        f"| 是否需要操作 | **{todo(signal, alerts)}** | 没有配置偏离时，继续按原计划执行。 |",
        f"| 市场压力 | **{p}** | 来自 VIX。低于 20 通常代表市场没有明显恐慌。 |",
        f"| 标普500 ETF（SPY） | 回撤 {pct(spy.get('drawdown'))} | 离高点跌了多少。 |",
        f"| 纳指100 ETF（QQQ） | 回撤 {pct(qqq.get('drawdown'))} | 科技成长股通常波动更大。 |",
        f"| 组合纪律 | `{signal}` | `within_policy_band` 表示配置仍在目标区间内。 |",
        "",
        "## 2. 本周结论",
        "",
    ]
    lines += [f"- **{a['level']} / {a['type']}**：{a['message']}" for a in alerts] if alerts else ["- 当前没有触发策略变更。继续按既定长期投资政策执行。"]
    lines += [
        f"- SPY 当前回撤：{pct(spy.get('drawdown'))}；QQQ 当前回撤：{pct(qqq.get('drawdown'))}。",
        f"- 科技成长股相对大盘本周变化：{pct(rel.get('return_1w'))}。",
        f"- VIX 当前值：{num(vix.get('last'))}，市场压力：{p}。",
        "",
        "## 3. 用人话解释",
        "",
    ]
    lines += [f"- {n}" for n in notes] if notes else ["- 本期没有生成额外解释。"]
    lines += [
        "",
        "## 4. 组合纪律",
        "",
        f"- 目标配置：SPY {pct(targets.get('SPY'))}，QQQ {pct(targets.get('QQQ'))}。",
        f"- 当前配置：SPY {pct(current.get('SPY'))}，QQQ {pct(current.get('QQQ'))}。",
        f"- 权重偏离：SPY {pct(dev.get('SPY'))}，QQQ {pct(dev.get('QQQ'))}。",
        "- 如果 QQQ 明显超配，未来新增资金优先补 SPY。",
        "",
        "## 5. 为什么这些指标存在",
        "",
        "| 指标 | 它回答的问题 |",
        "|---|---|",
        "| 回撤 | 现在离高点跌了多少？ |",
        "| 200日均线 | 长期趋势有没有转弱？ |",
        "| VIX | 市场是否恐慌？ |",
        "| 市场宽度 | 上涨是否只靠少数大公司？ |",
        "| 利率和通胀 | 宏观环境是否压制估值？ |",
        "",
        "<details>",
        "<summary>技术附录</summary>",
        "",
        "### 核心数据",
        "| 指标 | SPY | QQQ |",
        "|---|---:|---:|",
        f"| 当前价格 | {num(spy.get('last'))} | {num(qqq.get('last'))} |",
        f"| 1周收益 | {pct(spy.get('return_1w'))} | {pct(qqq.get('return_1w'))} |",
        f"| 1月收益 | {pct(spy.get('return_1m'))} | {pct(qqq.get('return_1m'))} |",
        f"| 1年收益 | {pct(spy.get('return_1y'))} | {pct(qqq.get('return_1y'))} |",
        f"| 高于200日均线 | {yn(spy.get('above_200dma'))} | {yn(qqq.get('above_200dma'))} |",
        f"| 30日年化波动率 | {pct(spy.get('vol_30d'))} | {pct(qqq.get('vol_30d'))} |",
        "",
        "### 相对表现",
        f"- QQQ/SPY：本周 {pct(rel.get('return_1w'))}，1月 {pct(rel.get('return_1m'))}。",
        f"- RSP/SPY：本周 {pct(rsp.get('return_1w'))}，1月 {pct(rsp.get('return_1m'))}。",
        f"- QQEW/QQQ：本周 {pct(qqew.get('return_1w'))}，1月 {pct(qqew.get('return_1m'))}。",
        "",
        "### 宏观数据",
        "| 指标 | 最新值 | 周变化 | 月变化 | 日期 |",
        "|---|---:|---:|---:|---:|",
    ]
    for sid, label in cfg.get("fred_series", {}).items():
        x = macro.get(sid, {})
        lines.append(f"| {LABELS.get(sid, label)} | {num(x.get('latest'))} | {macro_delta(sid, x.get('weekly_change'))} | {macro_delta(sid, x.get('monthly_change'))} | {x.get('date') or 'n/a'} |")
    lines += [
        "",
        "</details>",
        "",
        "## 6. 行动建议",
        "",
        "- 本报告不提供短线买卖建议。",
        "- 如果 QQQ 超配，未来新增资金优先补 SPY，避免科技成长股过度集中。",
        "- 如果市场进入大幅回撤区间，继续按投资政策执行，不用情绪替代规则。",
        "",
    ]
    return "\n".join(lines)
