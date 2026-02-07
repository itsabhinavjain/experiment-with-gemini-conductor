# Backend Explained

The `python-backend` is the heart of our application. It bridges the gap between our user interfaces and the intelligent capabilities of the Claude Agent SDK.

---

## Tech Stack
*   **Framework:** `FastAPI` (High-performance web framework)
*   **Runtime:** Python 3.11+
*   **AI SDK:** `claude-agent-sdk` (Official Anthropic SDK)
*   **Package Manager:** `uv`
*   **Streaming:** `sse-starlette` (Server-Sent Events)

---

## Key Modules

### 1. `main.py` - The Entry Point
This file sets up the FastAPI application and defines the API routes.

*   `GET /health`: A simple check to ensure the server is running.
*   `POST /chat`: The main endpoint. It accepts a JSON body with a `prompt` and `session_id`, and returns a `EventSourceResponse` (a stream).

### 2. `agent/session.py` - Session Management
The SDK requires us to manage "Sessions". A session represents a continuous conversation.

*   **`SessionManager` Class:** We implemented a simple in-memory dictionary `self.sessions = {}`.
*   **Logic:**
    *   If a client sends a `session_id`, look it up.
    *   If not found (or no ID provided), generate a new UUID and create a new SDK `client`.
    *   Return the `client` to be used for the query.

### 3. `agent/manager.py` - Agent Initialization
This is where the Agent itself is configured. We define:
*   The Model (e.g., `claude-3-5-sonnet-20241022`).
*   The System Prompt ("You are a helpful assistant...").
*   Tools (if we were using them).

---

## Understanding Streaming & Thinking Blocks

The most complex part of the backend is handling the real-time stream from Claude.

### The Problem
Claude doesn't just return a text string. It returns a stream of *events*. Some events are pieces of the final answer ("Text Blocks"), and some are pieces of its internal reasoning ("Thinking Blocks").

### The Solution: Server-Sent Events (SSE)

We use SSE to forward these events to the frontend as they happen.

**The Loop (Simplified Code):**
```python
async def event_generator():
    # 1. Send the Session ID first so the client knows it
    yield format_sse("session_id", session_id)

    # 2. Query the Agent
    async with client:
        await client.query(prompt)

        # 3. Listen to the Agent's response stream
        async for message in client.receive_response():
            if is_thinking_block(message):
                # It's a thought! Send it as 'thinking' type.
                yield format_sse("thinking", message.content)
            elif is_text_block(message):
                # It's the answer! Send it as 'text' type.
                yield format_sse("text", message.content)
```

### Response Format
The frontend receives a stream of JSON objects like this:

**Thinking Chunk:**
```json
{"type": "thinking", "content": "The user asked for..."}
```

**Text Chunk:**
```json
{"type": "text", "content": "Hello! "}
```

This clear separation allows the frontend to render the "Thinking" logic in a separate, yellow panel, distinct from the final green response.
