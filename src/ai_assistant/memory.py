"""Short-term conversation memory."""

from typing import Any


class ConversationMemory:
    """Stores the recent conversation history."""

    def __init__(self, max_messages: int = 10) -> None:
        self.max_messages = max_messages
        self.messages: list[dict[str, Any]] = []

    def add(self, role: str, content: str) -> None:
        """Append a message to memory."""
        self.messages.append({"role": role, "content": content})

    def get_recent(self, n: int | None = None) -> list[dict[str, Any]]:
        """Return the most recent n messages.

        BUG: this does not enforce max_messages when n is larger than the
        configured limit. The caller can request more messages than should be
        retained.
        """
        if n is None:
            n = self.max_messages
        return self.messages[-n:]
