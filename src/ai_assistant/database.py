"""SQLite persistence for the web assistant."""

import os
import sqlite3
from typing import Any

def get_db_path() -> str:
    """Return the database path, reading the env var each time."""
    return os.getenv("AI_ASSISTANT_DB", "ai_assistant.db")


def get_db() -> sqlite3.Connection:
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the messages table if it does not exist."""
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_key TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def add_message(api_key: str, role: str, content: str) -> None:
    """Persist a single message."""
    conn = get_db()
    conn.execute(
        "INSERT INTO messages (api_key, role, content) VALUES (?, ?, ?)",
        (api_key, role, content),
    )
    conn.commit()
    conn.close()


def get_recent_messages(api_key: str, n: int = 10) -> list[dict[str, Any]]:
    """Return the most recent n messages for an API key.

    BUG: the rows are returned newest-first instead of oldest-first, so the
    conversation history is out of order when fed back into the chat session.
    Fix the ordering so messages are returned in chronological order.
    """
    conn = get_db()
    rows = conn.execute(
        "SELECT role, content FROM messages WHERE api_key = ? ORDER BY id DESC LIMIT ?",
        (api_key, n),
    ).fetchall()
    conn.close()
    return [{"role": row["role"], "content": row["content"]} for row in rows]
