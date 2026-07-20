# Assessment Roadmap

Use this as your progress checklist. Each item links to the detailed task document.

---

## Phase 1 — CLI & Skills

See [`TASKS.md`](TASKS.md) for details.

- [ ] **Environment setup**
  - Fork the repo, create a virtual environment, install dependencies.
  - Run `pytest` and observe the failing tests.

- [ ] **Fix skill registry lookup**
  - Make `SkillRegistry.get_skill` case-insensitive.
  - Run `pytest tests/test_skills.py tests/test_cli.py`.

- [ ] **Fix LLM message ordering**
  - System messages should appear before user/assistant messages.
  - Run `pytest tests/test_llm_client.py`.

- [ ] **Fix conversation memory limit**
  - `ConversationMemory.get_recent` must respect `max_messages`.
  - Run `pytest tests/test_memory.py`.

- [ ] **Add weather skill**
  - Create `src/ai_assistant/skills/weather.py`.
  - Register it, test it, make sure the CLI can run it.
  - Run `pytest`.

- [ ] **(Bonus) Add chat command**
  - See [`TASKS-chat-bonus.md`](TASKS-chat-bonus.md).
  - Fix the `ChatSession` bugs and add an `ai-assistant chat` command.

---

## Phase 2 — Web API

See [`TASKS-web-phase.md`](TASKS-web-phase.md) for details.

- [ ] **Fix database message ordering**
  - `get_recent_messages` should return oldest → newest.
  - Run `pytest tests/test_database.py`.

- [ ] **Implement API key authentication**
  - Validate `Authorization: Bearer <key>` against `AI_ASSISTANT_API_KEYS`.
  - Run `pytest tests/test_auth.py`.

- [ ] **Wire the `/chat` endpoint**
  - Load history for the API key.
  - Seed the `ChatSession` memory.
  - Persist user and assistant messages.
  - Run `pytest tests/test_web.py`.

- [ ] **Wire the frontend**
  - Implement the JavaScript in `templates/chat.html`.
  - Send messages to `/chat`, display replies, handle errors.

- [ ] **(Stretch) Extras**
  - Add `DELETE /history`.
  - Add pagination to `/history`.
  - Add a Dockerfile.

---

## Deliverables

- All tests pass.
- Clear, focused commits.
- A short final write-up of what you learned and what you would improve.
