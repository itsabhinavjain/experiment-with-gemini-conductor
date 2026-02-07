import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    force=True
)
logger = logging.getLogger(__name__)

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from config import get_settings
from agent.schemas import ChatRequest, ChatResponseChunk
from agent.session import session_manager
from utils.streaming import format_sse
from claude_agent_sdk import ThinkingBlock, TextBlock, AssistantMessage
import asyncio

app = FastAPI(title="Claude Agent SDK Backend")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify the exact frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    logger.info(f"Received chat request for session: {chat_request.session_id}")
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
    
    # Custom log configuration for uvicorn to match our format
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["default"]["fmt"] = "[%(asctime)s] - %(levelname)s - %(message)s"
    log_config["formatters"]["default"]["datefmt"] = "%Y-%m-%d %H-%M-%S"
    log_config["formatters"]["access"]["fmt"] = "[%(asctime)s] - %(levelname)s - %(message)s"
    log_config["formatters"]["access"]["datefmt"] = "%Y-%m-%d %H-%M-%S"
    
    uvicorn.run(
        "main:app", 
        host=settings.host, 
        port=settings.port, 
        reload=settings.debug,
        log_config=log_config
    )
