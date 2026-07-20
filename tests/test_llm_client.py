"""Tests for the stub LLM client."""

from ai_assistant.llm_client import LLMClient


def test_chat_returns_stub_reply():
    client = LLMClient()
    messages = [{"role": "user", "content": "Hello"}]
    reply = client.chat(messages)
    assert "Stub reply to: Hello" == reply


def test_system_message_comes_first():
    """System messages should be formatted before user/assistant messages."""
    client = LLMClient()
    messages = [
        {"role": "user", "content": "Hello"},
        {"role": "system", "content": "You are helpful"},
    ]
    formatted = client._format_messages(messages)
    assert formatted[0] == "You are helpful"
    assert formatted[1] == "Hello"


def test_format_messages_preserves_order_without_system():
    client = LLMClient()
    messages = [
        {"role": "user", "content": "First"},
        {"role": "assistant", "content": "Second"},
        {"role": "user", "content": "Third"},
    ]
    formatted = client._format_messages(messages)
    assert formatted == ["First", "Second", "Third"]
