# Phase 2 — Web Assistant

Now that the CLI assistant works, you will expose it as a web service.

## Setup

Install the new dependencies:

```bash
pip install -e ".[dev]"
```

Run the web app:

```bash
uvicorn ai_assistant.web:app --reload
```

Open http://localhost:8000 in your browser.

---

## Task 1 — Fix message ordering (database)

Run:

```bash
pytest tests/test_database.py -v
```

The test `test_get_recent_messages_returns_chronological_order` fails because `get_recent_messages` returns messages newest-first.

Fix `src/ai_assistant/database.py` so messages are returned oldest → newest.

---

## Task 2 — Implement API key authentication

Run:

```bash
pytest tests/test_auth.py -v
```

All tests fail because `src/ai_assistant/auth.py` is not implemented.

Implement `get_api_key` so that:

- The request must include `Authorization: Bearer <key>`.
- The key must exist in `AI_ASSISTANT_API_KEYS` (comma-separated env var).
- Missing, malformed, or invalid headers raise HTTP 401.

**Hint:** Use `HTTPException(status_code=401, detail="...")` from FastAPI.

---

## Task 3 — Persist chat history

Run:

```bash
pytest tests/test_web.py -v
```

The web endpoints exist, but chat messages are not persisted or loaded.

Update `src/ai_assistant/web.py` so that:

- Before generating a reply, the `/chat` endpoint loads history for the API key and seeds the `ChatSession` memory.
- After generating a reply, the endpoint persists both the user message and assistant reply to the database.

**Hints:**

- Use `get_recent_messages(api_key)` and call `session.memory.add(role, content)` for each message.
- Use `add_message(api_key, role, content)` to persist messages.

---

## Task 4 — Wire up the frontend

The HTML page at `src/ai_assistant/templates/chat.html` has a TODO in the `<script>` tag.

Implement the frontend JavaScript so that:

- Submitting the form POSTs to `/chat` with the message and API key.
- The assistant's reply is appended to `#chat-history`.
- User messages appear on the right; assistant messages appear on the left.
- Errors are shown in `#error`.

**Bonus:** Fetch and display `/history` when the page loads.

---

## Task 5 — Run everything end-to-end

1. Start the server: `uvicorn ai_assistant.web:app --reload`
2. Open http://localhost:8000
3. Enter an API key from `AI_ASSISTANT_API_KEYS`
4. Send messages and verify they persist after a page refresh.

---

## Stretch goals

- Add `DELETE /history` to clear a user's history.
- Add pagination to `/history` using `skip` and `limit` query params.
- Add a Dockerfile for the web app.
- Validate that the `message` field in `/chat` is not empty.

---

## Deliverables

- `pytest` passes for `test_database.py`, `test_auth.py`, and `test_web.py`.
- The web UI can send messages and display replies.
- Messages persist in SQLite and are isolated by API key.
- Clear commits explaining each task.
