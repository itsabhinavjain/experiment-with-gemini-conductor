import json
from agent.schemas import ChatResponseChunk

def format_sse(chunk: ChatResponseChunk) -> str:
    """
    Formats a ChatResponseChunk into a JSON string for SSE.
    """
    return json.dumps(chunk.model_dump())
