"""FastAPI web application for the AI assistant."""

import os

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .auth import get_api_key
from .chat_session import ChatSession
from .database import add_message, get_recent_messages, init_db
from .llm_client import LLMClient

# Static files and templates
static_dir = os.path.join(os.path.dirname(__file__), "static")
template_dir = os.path.join(os.path.dirname(__file__), "templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Zervi AI Assistant Web", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=template_dir)


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    """Serve the chat UI."""
    return templates.TemplateResponse(request=request, name="chat.html")


@app.post("/chat")
def chat(
    message: str = Form(...),
    api_key: str = Depends(get_api_key),
) -> dict[str, str]:
    """Receive a user message and return the assistant's reply.

    TODO for the candidate:
    - Load the conversation history for this API key.
    - Seed the ChatSession memory with that history before responding.
    - Persist both the user message and the assistant reply to the database.
    """
    client = LLMClient()
    session = ChatSession(client=client)

    reply = session.respond(message)

    return {"reply": reply}


@app.get("/history")
def history(
    api_key: str = Depends(get_api_key),
    limit: int = 10,
) -> dict[str, list]:
    """Return recent messages for the authenticated API key."""
    return {"messages": get_recent_messages(api_key, n=limit)}
