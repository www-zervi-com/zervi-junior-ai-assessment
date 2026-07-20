"""Tests for API key authentication."""

import os

import pytest
from fastapi import HTTPException

from ai_assistant.auth import get_api_key


@pytest.fixture(autouse=True)
def set_test_keys(monkeypatch):
    monkeypatch.setenv("AI_ASSISTANT_API_KEYS", "key-one,key-two")


def test_valid_key_returns_key():
    assert get_api_key("Bearer key-one") == "key-one"
    assert get_api_key("Bearer key-two") == "key-two"


def test_missing_header_raises_401():
    with pytest.raises(HTTPException) as exc:
        get_api_key(None)
    assert exc.value.status_code == 401


def test_malformed_header_raises_401():
    with pytest.raises(HTTPException) as exc:
        get_api_key("Basic key-one")
    assert exc.value.status_code == 401


def test_invalid_key_raises_401():
    with pytest.raises(HTTPException) as exc:
        get_api_key("Bearer wrong-key")
    assert exc.value.status_code == 401
