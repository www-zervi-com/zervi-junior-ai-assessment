"""Multi-turn chat session manager."""

from typing import Any

from .llm_client import LLMClient
from .memory import ConversationMemory


class ChatSession:
    """Manages a back-and-forth conversation with the assistant.

    This is intentionally incomplete and contains a few bugs for the
    candidate to find and fix.
    """

    def __init__(
        self,
        client: LLMClient | None = None,
        memory: ConversationMemory | None = None,
        system_prompt: str = "You are a helpful assistant.",
    ) -> None:
        self.client = client or LLMClient()
        self.memory = memory or ConversationMemory()
        self.system_prompt = system_prompt

    def start(self, user_input: str) -> str:
        """Begin the conversation with a system prompt and the first user message."""
        self.memory.add("system", self.system_prompt)
        return self._respond(user_input)

    def respond(self, user_input: str) -> str:
        """Continue the conversation with a new user message."""
        return self._respond(user_input)

    def _respond(self, user_input: str) -> str:
        """Generate a reply and store both sides of the exchange.

        BUG: the client is called with an empty list instead of the full
        conversation history. Fix this so the LLM sees the system prompt and
        all prior messages.
        """
        self.memory.add("user", user_input)
        reply = self.client.chat([])
        self.memory.add("assistant", reply)
        return reply

    def is_exit(self, user_input: str) -> bool:
        """Check if the user wants to end the chat.

        BUG: only 'exit' is recognized. Also accept 'quit' (case-insensitive,
        with surrounding whitespace allowed).
        """
        return user_input.strip().lower() == "exit"
