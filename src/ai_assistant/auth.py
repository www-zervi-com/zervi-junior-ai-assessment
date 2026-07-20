"""API key authentication for the web assistant.

TODO for the candidate: implement the `get_api_key` dependency so that:
- The request must include an `Authorization: Bearer <key>` header.
- The key must exist in the comma-separated list in the
  `AI_ASSISTANT_API_KEYS` environment variable.
- If the header is missing, malformed, or the key is invalid, raise an
  HTTP 401 Unauthorized exception.

Return the validated API key string on success.
"""

import os

from fastapi import Header, HTTPException, status

API_KEYS = set(os.getenv("AI_ASSISTANT_API_KEYS", "test-key").split(","))


def get_api_key(authorization: str | None = Header(default=None)) -> str:
    """Validate the Authorization header and return the API key."""
    # TODO: implement me
    raise NotImplementedError("get_api_key is not implemented yet")
