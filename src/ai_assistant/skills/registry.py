"""Skill registry and loader."""

from .base import Skill
from .echo import EchoSkill
from .greet import GreetSkill


class SkillRegistry:
    """Discovers and returns skills by name."""

    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {
            "echo": EchoSkill(),
            "greet": GreetSkill(),
        }

    def list_skills(self) -> list[str]:
        """Return the names of all registered skills."""
        return list(self._skills.keys())

    def get_skill(self, name: str) -> Skill | None:
        """Return a skill by name.

        BUG: skill lookup is case-sensitive, so "ECHO" or "Echo" returns None
        even though "echo" is registered. Make the lookup case-insensitive.
        """
        return self._skills.get(name)
