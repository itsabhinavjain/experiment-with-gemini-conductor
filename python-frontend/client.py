import httpx
import asyncio
import json
from typing import AsyncGenerator, Optional
from config import get_settings

class BackendClient:
    """
    Client for interacting with the FastAPI backend.
    """
    def __init__(self):
        self.settings = get_settings()
        self._httpx_client = httpx.AsyncClient(base_url=self.settings.backend_api_url)

    async def get_health(self) -> dict:
        """
        Calls the /health endpoint of the backend.
        """
        try:
            response = await self._httpx_client.get("/health")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"status": "error", "message": f"HTTP error: {e.response.status_code}"}
        except httpx.RequestError as e:
            return {"status": "error", "message": f"Request error: {e}"}

    async def stream_chat(self, prompt: str, session_id: Optional[str] = None) -> AsyncGenerator[dict, None]:
        """
        Streams chat responses from the /chat endpoint.
        Yields JSON chunks as they are received.
        """
        json_data = {"prompt": prompt}
        if session_id:
            json_data["session_id"] = session_id

        try:
            async with self._httpx_client.stream("POST", "/chat", json=json_data, timeout=None) as response:
                response.raise_for_status()
                async for chunk in response.aiter_bytes():
                    # SSE chunks typically start with "data: "
                    # We expect our backend to send pure JSON strings prefixed with "data: "
                    data_str = chunk.decode("utf-8")
                    if data_str.startswith("data: "):
                        json_str = data_str[len("data: "):].strip()
                        try:
                            yield json.loads(json_str)
                        except json.JSONDecodeError:
                            # Handle cases where a chunk might not be a complete JSON
                            # (e.g., if multiple SSE events are in one TCP packet)
                            # For simplicity, we assume one JSON per "data: " line.
                            # More robust parsing might be needed for production.
                            pass
        except httpx.HTTPStatusError as e:
            yield {"type": "error", "content": f"HTTP error: {e.response.status_code}"}
        except httpx.RequestError as e:
            yield {"type": "error", "content": f"Request error: {e}"}

backend_client = BackendClient()
