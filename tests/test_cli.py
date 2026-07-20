"""Tests for the CLI."""

from ai_assistant.cli import build_parser, run_command


def test_list_command():
    args = build_parser().parse_args(["list"])
    result = run_command(args)
    assert "echo" in result
    assert "greet" in result


def test_run_echo_skill():
    args = build_parser().parse_args(["run", "--skill", "echo", "--input", "hello"])
    result = run_command(args)
    assert result == "Echo: hello"


def test_run_unknown_skill():
    args = build_parser().parse_args(["run", "--skill", "missing"])
    result = run_command(args)
    assert "Unknown skill" in result


def test_run_skill_is_case_insensitive():
    """The CLI should find skills regardless of casing."""
    args = build_parser().parse_args(["run", "--skill", "ECHO", "--input", "hi"])
    result = run_command(args)
    assert result == "Echo: hi"
