from pydantic import BaseModel
from typing import Optional, Literal

class ChatRequest(BaseModel):
    """
    Schema for the chat request.
    """
    prompt: str
    session_id: Optional[str] = None

class ChatResponseChunk(BaseModel):
    """
    Schema for a single chunk in the SSE stream.
    """
    type: Literal["thinking", "text", "session_id", "error"]
    content: str
