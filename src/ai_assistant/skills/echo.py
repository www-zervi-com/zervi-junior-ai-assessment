"""Echo skill."""

from typing import Any

from .base import Skill


class EchoSkill(Skill):
    """Repeats the user's input back to them."""

    def run(self, input_text: str, memory: Any | None = None, client: Any | None = None) -> str:
        return f"Echo: {input_text}"
