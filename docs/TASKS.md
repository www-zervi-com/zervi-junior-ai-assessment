# Junior Software Engineer — 1–2 Day Assessment Tasks

## Context

This is a minimal AI-assistant CLI. It has a skill system, a stubbed LLM client, and a short-term memory module. The repo currently contains a few deliberate bugs and a missing feature.

Your job over the next one to two days is to:

1. Get the project running.
2. Fix the existing bugs so all tests pass.
3. Add a new skill with tests.
4. Present your work.

Read `README.md` and `AGENTS.md` before you start.

---

## Day 1 — Fix the Foundation

### Morning

#### 1. Setup (30–60 min)

- Clone/fork the repo.
- Create a virtual environment.
- Install the package in editable mode with dev dependencies.
- Run `pytest` and observe the failures.

**Deliverable:** `pytest` runs and you can explain which tests fail and why.

#### 2. Fix skill registry lookup (45–60 min)

The `SkillRegistry.get_skill` method currently only finds skills when the name matches exactly. Users naturally type `ECHO`, `Echo`, or `echo`.

- Make skill lookup case-insensitive.
- Keep `list_skills()` returning lowercase names.
- Run `pytest` — the `test_get_skill_case_insensitive` and `test_run_skill_is_case_insensitive` tests should now pass.

**Deliverable:** All registry-related tests pass.

#### 3. Fix LLM message ordering (45–60 min)

The `LLMClient._format_messages` method appends system messages at the end instead of the beginning.

- System messages should appear before user and assistant messages.
- Preserve the relative order of non-system messages.
- Run `pytest` — `test_system_message_comes_first` should pass.

**Deliverable:** All LLM-client tests pass.

#### 4. Fix conversation memory limit (45–60 min)

`ConversationMemory.get_recent` lets callers request more messages than `max_messages` allows.

- Cap the returned list so it never exceeds `max_messages`, even when `n` is larger.
- Run `pytest` — `test_memory_respects_max_messages` should pass.

**Deliverable:** All memory tests pass.

### Afternoon

#### 5. Run the full suite (15 min)

All tests in `pytest` should now pass.

#### 6. Write a short retro (30 min)

In a file called `notes/day1-retro.md`, write:

- What you changed and why.
- One thing you found confusing.
- One thing you would improve if you had more time.

**Deliverable:** `notes/day1-retro.md` committed.

---

## Day 2 — Add a Feature

### Morning

#### 7. Add a `weather` skill (2–3 hrs)

Create `src/ai_assistant/skills/weather.py`.

Requirements:

- The skill accepts a city name as input.
- It returns a weather string, e.g. `Weather in London: 18°C, cloudy`.
- If the input is empty or only whitespace, default the city to `"Unknown"`.
- Register the skill in `SkillRegistry`.

Optional stretch goals:

- Return different stub weather based on the city name length or first letter.
- Use the `client` argument to generate the response (stub is fine).

**Deliverable:** `weather` skill works from the CLI:

```bash
ai-assistant run --skill weather --input "Paris"
# Weather in Paris: 18°C, cloudy
```

### Afternoon

#### 8. Test the weather skill (45–60 min)

Add tests in `tests/test_skills.py` or a new `tests/test_weather_skill.py`:

- The skill returns a string containing the city name.
- Empty input defaults to `"Unknown"`.
- The skill is registered in `SkillRegistry`.

**Deliverable:** New tests pass and the full suite is green.

#### 9. Refactor or improve one thing (45–60 min)

Pick one:

- Reduce duplication between skills.
- Add input validation to the CLI.
- Add a `--model` flag that flows through to `LLMClient`.
- Improve error messages in the registry or CLI.

**Deliverable:** A small, focused commit with a clear message.

#### 10. Final presentation (30–45 min)

Present to the team:

- Demo the fixed tests and the new skill.
- Explain one bug fix in detail.
- Explain one trade-off you made.
- Share what you would do next if you had another day.

---

## Evaluation Criteria

| Area | What we look for |
|---|---|
| **Problem solving** | Breaks tasks into steps, reads code and tests before guessing. |
| **Code quality** | Clean, readable, minimal changes. Follows existing patterns. |
| **Testing** | Updates and adds tests. Runs the suite before finishing. |
| **Git hygiene** | Small, focused commits with clear messages. |
| **Communication** | Asks clarifying questions, explains reasoning, accepts feedback. |
| **AI/LLM sense** | Understands how the stub LLM client and skill system fit together. |

## Tips

- Do not over-engineer. Keep solutions simple.
- If you are stuck for more than 15 minutes, ask a question.
- Commit frequently.
- Read the tests — they tell you the expected behavior.
