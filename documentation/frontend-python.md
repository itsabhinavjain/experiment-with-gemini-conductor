# Python CLI Frontend Explained

The `python-frontend` provides a hacker-style, terminal-based interface for interacting with the Agent. It proves that you don't need a complex web browser to have a rich AI experience.

---

## Tech Stack
*   **Language:** Python 3.11+
*   **HTTP Client:** `httpx` (Async capabilities)
*   **UI Library:** `rich` (Beautiful terminal formatting)
*   **Package Manager:** `uv`

---

## Architecture Design

The CLI is designed as a simple infinite loop:
1.  **Prompt:** Ask the user for input.
2.  **Send:** Send input to backend.
3.  **Stream:** Receive and render response chunks in real-time.
4.  **Repeat:** Go back to step 1.

### Why `httpx`?
We use `httpx` because it natively supports **asynchronous streaming**. This is crucial. If we used a standard synchronous library, the UI would freeze until the entire answer was generated. With `httpx`, we can process every character as soon as it arrives.

### Why `rich`?
Standard Python `print()` is boring. `rich` allows us to:
*   Create colorful Panels (Green for Claude, Yellow for Thinking).
*   Use Markdown rendering in the terminal.
*   Update the screen in real-time (using `Live` display) to create the typing effect.

---

## Key Implementation Details

### Handling the Stream
In `main.py`, we use a `Live` context manager from `rich`. This is a powerful feature that allows us to redraw a part of the screen repeatedly.

```python
with Live(console=console, refresh_per_second=4) as live:
    async for chunk in backend_client.stream_chat(user_input):
        # 1. Update our internal state
        if chunk['type'] == 'thinking':
            thinking_buffer += chunk['content']
        elif chunk['type'] == 'text':
            response_buffer += chunk['content']
        
        # 2. Re-draw the screen with new buffers
        live.update(
            Group(
                Panel(thinking_buffer, title="Thinking"),
                Panel(response_buffer, title="Response")
            )
        )
```

### Session Persistence
The CLI automatically handles the `session_id`.
1.  It starts as `None`.
2.  The *first* response from the backend contains a `session_id`.
3.  The CLI saves this variable.
4.  All *future* requests send this `session_id` back to the server, ensuring Claude remembers the context of the conversation.
