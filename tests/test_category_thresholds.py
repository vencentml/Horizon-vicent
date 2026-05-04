"""Tests for category-specific filtering thresholds."""

from datetime import datetime, timezone

from src.models import Config, ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


class DummyStorage:
    """Minimal storage stub for constructing the orchestrator in unit tests."""

    pass


def _config_with_thresholds() -> Config:
    return Config.model_validate(
        {
            "version": "1.0",
            "ai": {
                "provider": "openai",
                "model": "gpt-4",
                "api_key_env": "OPENAI_API_KEY",
            },
            "sources": {},
            "filtering": {
                "ai_score_threshold": 7.0,
                "time_window_hours": 24,
                "category_thresholds": {
                    "paper-ai": 8.5,
                    "risk-health": 8.5,
                    "ai-research": 7.5,
                },
            },
        }
    )


def _item(category: str | None = None, score: float | None = None) -> ContentItem:
    metadata = {}
    if category is not None:
        metadata["category"] = category
    return ContentItem(
        id="test:item:1",
        source_type=SourceType.RSS,
        title="Test item",
        url="https://example.com/test",
        content="Test content",
        published_at=datetime.now(timezone.utc),
        metadata=metadata,
        ai_score=score,
    )


def test_filtering_config_accepts_category_thresholds() -> None:
    config = _config_with_thresholds()

    assert config.filtering.ai_score_threshold == 7.0
    assert config.filtering.category_thresholds["paper-ai"] == 8.5
    assert config.filtering.category_thresholds["ai-research"] == 7.5


def test_threshold_for_item_uses_category_threshold() -> None:
    orchestrator = HorizonOrchestrator(_config_with_thresholds(), DummyStorage())

    assert orchestrator._threshold_for_item(_item("paper-ai")) == 8.5
    assert orchestrator._threshold_for_item(_item("ai-research")) == 7.5


def test_threshold_for_item_falls_back_to_global_threshold() -> None:
    orchestrator = HorizonOrchestrator(_config_with_thresholds(), DummyStorage())

    assert orchestrator._threshold_for_item(_item()) == 7.0
    assert orchestrator._threshold_for_item(_item("unknown-category")) == 7.0


def test_category_threshold_changes_selection_decision() -> None:
    orchestrator = HorizonOrchestrator(_config_with_thresholds(), DummyStorage())

    paper_item = _item("paper-ai", score=8.0)
    general_item = _item(None, score=8.0)

    assert paper_item.ai_score < orchestrator._threshold_for_item(paper_item)
    assert general_item.ai_score >= orchestrator._threshold_for_item(general_item)
