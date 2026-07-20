"""Tests for the multi-turn chat session."""

from ai_assistant.chat_session import ChatSession
from ai_assistant.llm_client import LLMClient


class FakeLLMClient:
    """A test double that records the messages it receives."""

    def __init__(self) -> None:
        self.last_messages: list[dict[str, str]] = []

    def chat(self, messages: list[dict[str, str]]) -> str:
        self.last_messages = messages
        return f"Reply to: {messages[-1]['content'] if messages else '...'}"


def test_start_adds_system_message():
    client = FakeLLMClient()
    session = ChatSession(client=client)
    session.start("Hello")

    assert session.memory.messages[0]["role"] == "system"
    assert session.memory.messages[0]["content"] == "You are a helpful assistant."


def test_respond_passes_full_history_to_client():
    client = FakeLLMClient()
    session = ChatSession(client=client)

    session.start("Hello")
    assert len(client.last_messages) == 2  # system + user
    assert client.last_messages[0]["role"] == "system"
    assert client.last_messages[-1]["content"] == "Hello"

    session.respond("How are you?")
    assert len(client.last_messages) == 4  # system + 2 user + 1 assistant
    assert client.last_messages[-1]["content"] == "How are you?"


def test_replies_are_stored_in_memory():
    client = FakeLLMClient()
    session = ChatSession(client=client)

    session.start("Hello")
    assert session.memory.messages[-1]["role"] == "assistant"


def test_is_exit_recognizes_quit_and_exit():
    session = ChatSession()
    assert session.is_exit("exit")
    assert session.is_exit("EXIT")
    assert session.is_exit("  exit  ")
    assert session.is_exit("quit")
    assert session.is_exit("QUIT")
    assert session.is_exit("  quit  ")
    assert not session.is_exit("no thanks")
    assert not session.is_exit("")


def test_custom_system_prompt():
    client = FakeLLMClient()
    session = ChatSession(client=client, system_prompt="You are a coding coach.")
    session.start("Help")

    assert session.memory.messages[0]["content"] == "You are a coding coach."
    assert client.last_messages[0]["content"] == "You are a coding coach."
