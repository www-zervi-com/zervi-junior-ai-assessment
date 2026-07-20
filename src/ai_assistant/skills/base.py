"""Base class for all skills."""

from abc import ABC, abstractmethod
from typing import Any


class Skill(ABC):
    """A skill is a small, reusable capability the assistant can invoke."""

    @abstractmethod
    def run(self, input_text: str, memory: Any | None = None, client: Any | None = None) -> str:
        """Execute the skill and return a text response."""
        ...
