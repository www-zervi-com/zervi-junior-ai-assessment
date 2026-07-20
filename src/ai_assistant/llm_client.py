"""Stub LLM client for the assessment."""

from typing import Any


class LLMClient:
    """A minimal, stubbed LLM client.

    In a real system this would call an external API. Here it just formats
    messages and returns a canned response so the rest of the assistant can
    be tested without network access.
    """

    def __init__(self, model: str = "stub") -> None:
        self.model = model

    def chat(self, messages: list[dict[str, Any]]) -> str:
        """Return a stub response based on the last message."""
        formatted = self._format_messages(messages)
        last = formatted[-1] if formatted else "..."
        return f"Stub reply to: {last}"

    def _format_messages(self, messages: list[dict[str, Any]]) -> list[str]:
        """Flatten messages to their content strings.

        BUG: system messages should come first, but they are currently appended
        at the end. Fix this so system messages appear before user/assistant
        messages.
        """
        non_system = [m["content"] for m in messages if m["role"] != "system"]
        system = [m["content"] for m in messages if m["role"] == "system"]
        return non_system + system
