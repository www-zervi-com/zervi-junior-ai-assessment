# Zervi Junior AI Assessment

A small, self-contained AI-assistant CLI used for the Zervi IT-AI team's junior software engineer on-the-job assessment.

## What this project is

This is a minimal "AI assistant" toolkit with:

- A command-line interface (`ai-assistant`)
- A simple skill/plugin system
- A stubbed LLM client
- A short-term conversation memory module
- A small pytest suite

It is intentionally simpler than production Zervi systems, but it uses similar patterns: CLI tools, modular skills, LLM integrations, and tests.

## Setup

1. Clone or fork this repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package in editable mode with dev dependencies:

   ```bash
   pip install -e ".[dev]"
   ```

4. Run the test suite:

   ```bash
   pytest
   ```

   Some tests will fail on the first run — that is expected. See `docs/TASKS.md`.

## Quick usage

```bash
# List available skills
ai-assistant list

# Run a skill
ai-assistant run --skill echo --input "hello world"
```

## Assessment tasks

See [`docs/TASKS.md`](docs/TASKS.md) for the Day 1 and Day 2 exercises.

## Notes for assessors

- The candidate should read `AGENTS.md` before writing code.
- The repo contains a few deliberate, junior-level bugs.
- Day 2 asks the candidate to extend the skill system with a new feature.
