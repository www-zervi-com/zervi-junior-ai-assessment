"""Tests for the skill system."""

from ai_assistant.skills.echo import EchoSkill
from ai_assistant.skills.greet import GreetSkill
from ai_assistant.skills.registry import SkillRegistry


def test_registry_lists_all_skills():
    registry = SkillRegistry()
    assert set(registry.list_skills()) == {"echo", "greet"}


def test_get_skill_case_insensitive():
    """Skill lookup should be case-insensitive."""
    registry = SkillRegistry()
    assert registry.get_skill("ECHO") is not None
    assert registry.get_skill("Echo") is not None
    assert registry.get_skill("gREET") is not None


def test_echo_skill():
    skill = EchoSkill()
    assert skill.run("hello") == "Echo: hello"


def test_greet_skill_uses_name():
    skill = GreetSkill()
    assert skill.run("Alice") == "Hello, Alice!"


def test_greet_skill_defaults_to_friend():
    skill = GreetSkill()
    assert skill.run("   ") == "Hello, friend!"
