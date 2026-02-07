from fastapi import FastAPI, Request, HTTPException
from sse_starlette.sse import EventSourceResponse
from config import get_settings
from agent.schemas import ChatRequest, ChatResponseChunk
from agent.session import session_manager
from utils.streaming import format_sse
from claude_agent_sdk import ThinkingBlock, TextBlock, AssistantMessage
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Claude Agent SDK Backend")

@app.get("/health")
async def health_check():
    """
    Simple health check endpoint to verify the service is up.
    """
    settings = get_settings()
    return {
        "status": "ok", 
        "message": f"{settings.app_name} is running"
    }

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    """
    Main chat endpoint that streams responses from the Claude Agent SDK.
    """
    session_id, client = session_manager.get_or_create_session(chat_request.session_id)

    async def event_generator():
        # First, send back the session ID so the client can reuse it
        yield {
            "data": format_sse(ChatResponseChunk(type="session_id", content=session_id))
        }

        try:
            # Execute the query using the SDK client
            # The SDK returns an AsyncIterator of messages/events
            async with client as session_client:
                await session_client.query(chat_request.prompt)
                
                async for message in session_client.receive_response():
                    if isinstance(message, AssistantMessage):
                        for block in message.content:
                            if isinstance(block, ThinkingBlock):
                                yield {
                                    "data": format_sse(ChatResponseChunk(type="thinking", content=block.thinking))
                                }
                            elif isinstance(block, TextBlock):
                                yield {
                                    "data": format_sse(ChatResponseChunk(type="text", content=block.text))
                                }
        except Exception as e:
            logger.error(f"Error during agent query: {str(e)}")
            yield {
                "data": format_sse(ChatResponseChunk(type="error", content=str(e)))
            }

    return EventSourceResponse(event_generator())

if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=settings.debug)
