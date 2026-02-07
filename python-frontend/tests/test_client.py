import pytest
import httpx
from client import BackendClient
from config import Settings
from unittest.mock import patch

@pytest.fixture
def mock_settings():
    """Fixture to mock settings for testing, assuming backend is running at 0.0.0.0:8000."""
    settings = Settings(backend_api_url="http://0.0.0.0:8000")
    return settings

@pytest.fixture
def client_for_backend(mock_settings, mocker):
    """Fixture to provide a BackendClient configured for the running backend."""
    mocker.patch('config.get_settings', return_value=mock_settings)
    client = BackendClient()
    yield client

@pytest.mark.asyncio
async def test_get_health_success(client_for_backend):
    """
    Tests successful health check against the running backend.
    """
    response = await client_for_backend.get_health()
    assert response == {"status": "ok", "message": "Claude Agent SDK Backend is running"}

@pytest.mark.asyncio
async def test_stream_chat_basic(client_for_backend):
    """
    Tests basic streaming chat against the running backend.
    This test assumes a successful response from Claude.
    """
    # Note: This test requires a valid Claude API key or working local Claude CLI setup
    # to get a meaningful response from the backend.
    # If the backend is not properly configured with Claude, this test might fail
    # or return an error message from the backend.
    prompt = "Tell me a very short story."
    session_id = None
    
    chunks = []
    try:
        async for chunk in client_for_backend.stream_chat(prompt, session_id):
            chunks.append(chunk)
            if chunk.get("type") == "session_id":
                session_id = chunk.get("content")
            print(f"Received chunk: {chunk}") # For debugging during development

        assert any(c.get("type") == "session_id" for c in chunks)
        # Expect at least one 'text' chunk or a 'thinking' chunk
        assert any(c.get("type") in ["text", "thinking"] for c in chunks)
        assert session_id is not None
    except httpx.ConnectError as e:
        pytest.fail(f"Could not connect to backend server at http://0.0.0.0:8000. "
                    f"Please ensure the python_backend server is running before executing tests. Error: {e}")
