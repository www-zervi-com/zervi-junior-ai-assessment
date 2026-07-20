"""Tests for the FastAPI web application."""

import pytest
from fastapi.testclient import TestClient

from ai_assistant.database import init_db
from ai_assistant.web import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Create a test client with a fresh temporary database."""
    db_path = tmp_path / "web_test.db"
    monkeypatch.setenv("AI_ASSISTANT_DB", str(db_path))
    monkeypatch.setenv("AI_ASSISTANT_API_KEYS", "test-key")
    init_db()
    return TestClient(app)


def test_index_returns_html(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_chat_without_auth_returns_401(client):
    response = client.post("/chat", data={"message": "hello"})
    assert response.status_code == 401


def test_chat_with_auth_returns_reply(client):
    response = client.post(
        "/chat",
        data={"message": "hello"},
        headers={"Authorization": "Bearer test-key"},
    )
    assert response.status_code == 200
    assert "reply" in response.json()


def test_chat_persists_messages(client):
    client.post(
        "/chat",
        data={"message": "hello"},
        headers={"Authorization": "Bearer test-key"},
    )

    response = client.get("/history", headers={"Authorization": "Bearer test-key"})
    assert response.status_code == 200
    messages = response.json()["messages"]
    assert len(messages) == 2
    assert messages[0]["role"] == "user"
    assert messages[0]["content"] == "hello"
    assert messages[1]["role"] == "assistant"



