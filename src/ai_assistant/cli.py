"""Command-line interface for the AI assistant."""

import argparse
import sys

from .llm_client import LLMClient
from .memory import ConversationMemory
from .skills.registry import SkillRegistry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Zervi AI Assistant")
    parser.add_argument(
        "command",
        choices=["run", "list"],
        help="Command to run",
    )
    parser.add_argument(
        "--skill",
        default="echo",
        help="Skill to use with the run command",
    )
    parser.add_argument(
        "--input",
        default="Hello",
        help="Input passed to the skill",
    )
    return parser


def run_command(args: argparse.Namespace) -> str:
    """Execute the requested command and return a string result."""
    registry = SkillRegistry()
    memory = ConversationMemory()
    client = LLMClient()

    if args.command == "list":
        return "Available skills: " + ", ".join(registry.list_skills())

    if args.command == "run":
        skill = registry.get_skill(args.skill)
        if skill is None:
            return f"Unknown skill: {args.skill}"
        return skill.run(args.input, memory=memory, client=client)

    return f"Unhandled command: {args.command}"


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = run_command(args)
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
