import pytest
from fastapi.testclient import TestClient
from main import app
from httpx_sse import connect_sse
import json

client = TestClient(app)

@pytest.mark.asyncio
async def test_chat_streaming_structure():
    """
    Verifies that the /chat endpoint returns a valid SSE stream with the expected structure.
    Note: This test uses a mock/client but doesn't necessarily call the real Anthropic API 
    if the key is missing. We are testing the structure of the response generator.
    """
    # Use a dummy prompt
    payload = {"prompt": "Hello", "session_id": "test-session"}
    
    # We use TestClient as a context manager for SSE
    with client.stream("POST", "/chat", json=payload) as response:
        assert response.status_code == 200
        assert response.headers["content-type"] == "text/event-stream; charset=utf-8"
        
        # Check the first event (should be the session_id)
        # We'll just read a few lines to verify the format
        lines = []
        for line in response.iter_lines():
            if line:
                lines.append(line)
                if len(lines) > 2: # Get at least one data event
                    break
        
        assert any("session_id" in l for l in lines)
