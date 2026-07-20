"""Greet skill."""

from typing import Any

from .base import Skill


class GreetSkill(Skill):
    """Greets the user by name."""

    def run(self, input_text: str, memory: Any | None = None, client: Any | None = None) -> str:
        name = input_text.strip() or "friend"
        return f"Hello, {name}!"
