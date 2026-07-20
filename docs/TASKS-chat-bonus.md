# Bonus Task — Multi-Turn Chat System

## Context

The assistant currently runs one-off skills. Your bonus task is to add a multi-turn chat session that remembers context across exchanges.

A starter module has been added:

- `src/ai_assistant/chat_session.py`
- `tests/test_chat_session.py`

The module has a few bugs. The tests will guide you to the correct behavior.

---

## Task 1: Fix the chat session bugs

Run:

```bash
pytest tests/test_chat_session.py -v
```

You will see failures. Fix the bugs in `chat_session.py` so all tests pass.

**Hints:**

- The LLM client should receive the full conversation history, not an empty list.
- The exit check should accept both `exit` and `quit`, case-insensitively.

---

## Task 2: Add a `chat` CLI command

Extend the CLI so the user can run:

```bash
ai-assistant chat
```

Requirements:

- Start a chat session with the default system prompt.
- Read user input in a loop.
- Print the assistant's reply each turn.
- Exit when the user types `exit` or `quit`.
- Handle empty input gracefully (skip the turn or print a friendly message).

**Hint:** Use `input()` to read from the terminal. Make sure the command is testable without blocking forever.

---

## Task 3: Test the CLI command

Add tests for the `chat` command in `tests/test_cli.py`.

Since `input()` blocks in normal use, you may need to refactor the command so it accepts an input iterator for testing.

Example test approach:

```python
def test_chat_command_exits_on_quit():
    # Provide a sequence of inputs and check the output
    ...
```

---

## Stretch goal

Allow the user to set a custom system prompt via a CLI flag:

```bash
ai-assistant chat --system-prompt "You are a strict code reviewer."
```

---

## Deliverables

- All `test_chat_session.py` tests pass.
- `ai-assistant chat` works interactively.
- New CLI tests pass.
- Clear commits explaining each change.
