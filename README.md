# Zervi Junior AI Assessment

A small, self-contained AI-assistant project used for the Zervi IT-AI team's junior software engineer on-the-job assessment.

## What this project is

This is a minimal AI assistant toolkit with:

- A command-line interface (`ai-assistant`)
- A simple skill/plugin system
- A stubbed LLM client
- Conversation memory
- A FastAPI web service with SQLite persistence
- API key authentication
- A small pytest suite

It is intentionally simpler than production Zervi systems, but it uses similar patterns: CLI tools, modular skills, LLM integrations, web APIs, databases, and tests.

---

## Assessment Roadmap

Complete the tasks in order. Push your progress to your fork after each phase.

### Phase 1 — CLI & Skills

1. [ ] **Setup** — Get the project running and run `pytest`.
2. [ ] **Fix skill lookup** — Make skill names case-insensitive.
3. [ ] **Fix LLM message order** — System messages must come first.
4. [ ] **Fix memory limit** — `get_recent` must not exceed `max_messages`.
5. [ ] **Add weather skill** — Build and test a new skill.
6. [ ] **(Bonus) Add chat command** — Multi-turn conversation via CLI.

### Phase 2 — Web API

7. [ ] **Fix database ordering** — Messages returned oldest → newest.
8. [ ] **Implement API key auth** — Validate `Authorization: Bearer <key>`.
9. [ ] **Wire `/chat` endpoint** — Load history, generate reply, persist both sides.
10. [ ] **Wire frontend** — Connect the HTML form to `/chat` and `/history`.
11. [ ] **(Stretch)** Add `DELETE /history`, pagination, or Docker.

Detailed instructions for each phase are in:

- [`docs/TASKS.md`](docs/TASKS.md)
- [`docs/TASKS-chat-bonus.md`](docs/TASKS-chat-bonus.md)
- [`docs/TASKS-web-phase.md`](docs/TASKS-web-phase.md)

---

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

   Some tests will fail on the first run — that is expected. The tasks above tell you how to fix them.

## Quick usage

```bash
# List available skills
ai-assistant list

# Run a skill
ai-assistant run --skill echo --input "hello world"

# Run the web app
uvicorn ai_assistant.web:app --reload
```

## Notes for assessors

- The candidate should read `AGENTS.md` before writing code.
- The repo contains deliberate bugs and incomplete features.
- Assessment criteria: problem solving, code quality, testing, git hygiene, and communication.
