"""Tests for the SQLite database layer."""

import os

import pytest

from ai_assistant.database import add_message, get_recent_messages, init_db


@pytest.fixture(autouse=True)
def use_temp_db(tmp_path, monkeypatch):
    """Use a fresh temporary database for every test."""
    db_path = tmp_path / "test.db"
    monkeypatch.setenv("AI_ASSISTANT_DB", str(db_path))
    init_db()


def test_get_recent_messages_returns_chronological_order():
    """Messages should be returned oldest -> newest, not newest -> oldest."""
    add_message("key-1", "user", "first")
    add_message("key-1", "assistant", "reply-1")
    add_message("key-1", "user", "second")

    messages = get_recent_messages("key-1", n=10)
    contents = [m["content"] for m in messages]

    assert contents == ["first", "reply-1", "second"]


def test_get_recent_messages_respects_limit():
    for i in range(5):
        add_message("key-1", "user", str(i))

    messages = get_recent_messages("key-1", n=3)
    assert len(messages) == 3
    assert messages[-1]["content"] == "4"


def test_messages_are_isolated_by_api_key():
    add_message("key-a", "user", "message-a")
    add_message("key-b", "user", "message-b")

    assert [m["content"] for m in get_recent_messages("key-a")] == ["message-a"]
    assert [m["content"] for m in get_recent_messages("key-b")] == ["message-b"]
