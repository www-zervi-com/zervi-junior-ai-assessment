"""Configuration constants."""

import os

DEFAULT_MODEL = os.getenv("AI_ASSISTANT_MODEL", "stub")
MAX_MEMORY_MESSAGES = int(os.getenv("AI_ASSISTANT_MAX_MEMORY", "10"))
