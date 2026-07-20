"""Tests for conversation memory."""

from ai_assistant.memory import ConversationMemory


def test_memory_stores_messages():
    memory = ConversationMemory()
    memory.add("user", "hello")
    assert len(memory.messages) == 1
    assert memory.messages[0]["role"] == "user"
    assert memory.messages[0]["content"] == "hello"


def test_memory_respects_max_messages():
    """get_recent should never return more messages than max_messages."""
    memory = ConversationMemory(max_messages=2)
    for i in range(5):
        memory.add("user", str(i))

    recent = memory.get_recent(n=10)
    assert len(recent) == 2
    assert recent[0]["content"] == "3"
    assert recent[-1]["content"] == "4"


def test_memory_default_n_uses_max():
    memory = ConversationMemory(max_messages=3)
    for i in range(10):
        memory.add("user", str(i))

    recent = memory.get_recent()
    assert len(recent) == 3
