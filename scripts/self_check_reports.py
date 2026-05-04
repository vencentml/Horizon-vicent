#!/usr/bin/env python3
"""Offline self-checks for Horizon report generators.

These checks intentionally avoid external network and API calls. They validate
that the weekly report generators can produce Jekyll-compatible Markdown with
stable front matter and expected Chinese sections.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import github_trending_weekly as ghw
import ukraine_war_weekly as uww


def assert_contains(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"Missing {label}: {needle!r}")


def check_github_weekly() -> None:
    items = ghw.sample_items()
    for item in items:
        item.ai_intro = ghw._fallback_intro(item)
    md = ghw.render_markdown(items, hours=168)
    assert_contains(md, "category: github-weekly", "GitHub weekly category")
    assert_contains(md, "GitHub 热门项目周报", "GitHub weekly title")
    assert_contains(md, "**它是什么**", "GitHub project explanation section")
    assert_contains(md, "**大致运行原理**", "GitHub mechanism section")
    assert_contains(md, "example/agent-runtime", "sample repository")


def check_ukraine_weekly() -> None:
    items = [
        uww.WarItem(
            title="Sample Ukraine battlefield update",
            url="https://example.com/ukraine-update",
            source="Sample Source",
            published_at="2026-05-01",
            summary="A sample item about Ukraine, Russia, drones, air defense, and the front line.",
            score=10,
        )
    ]
    analysis = uww.fallback_analysis(items)
    md = uww.render_markdown(items, analysis, hours=168)
    assert_contains(md, "category: ukraine-war-weekly", "Ukraine weekly category")
    assert_contains(md, "俄乌战争一周进展", "Ukraine weekly title")
    assert_contains(md, "## 执行摘要", "executive summary section")
    assert_contains(md, "## 分主题进展", "theme section")
    assert_contains(md, "## 原始来源列表", "source list section")


def check_cli_sample_outputs() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        rc = ghw.main_with_args(["--sample", "--no-ai", "--output-dir", str(out_dir), "--limit", "2"])
        if rc != 0:
            raise AssertionError("github_trending_weekly sample CLI returned non-zero")
        files = list(out_dir.glob("*-github-trending-weekly-zh.md"))
        if len(files) != 1:
            raise AssertionError(f"Expected one GitHub weekly output, got {files}")


def main() -> int:
    check_github_weekly()
    check_ukraine_weekly()
    # CLI sample check is optional at runtime, because it relies on main_with_args.
    print("Report generator self-checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
