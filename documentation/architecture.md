# System Architecture

This document provides a high-level overview of the Claude Agent SDK Reference Project. It details the system components, data flow, and the agent lifecycle.

---

## System Overview

The project follows a **Client-Server Architecture**. A central backend service manages the connection to the Claude Agent SDK, while multiple frontend clients (CLI and Web) connect to this backend to interact with the agent.

### Components

1.  **Python Backend (`python-backend/`)**:
    *   **Role:** The core "Brain" of the system.
    *   **Tech:** Python, FastAPI, Claude Agent SDK, `uv`.
    *   **Responsibility:** Initializes the agent, manages user sessions, handles API requests, and streams responses (including thinking blocks) via Server-Sent Events (SSE).

2.  **Python CLI Frontend (`python-frontend/`)**:
    *   **Role:** A lightweight, terminal-based client.
    *   **Tech:** Python, `rich`, `httpx`.
    *   **Responsibility:** Provides a developer-focused, text-based interface to chat with the agent.

3.  **Next.js Web Frontend (`nextjs-frontend/`)**:
    *   **Role:** A modern, visual web client.
    *   **Tech:** Next.js (App Router), React, Tailwind CSS, shadcn/ui.
    *   **Responsibility:** Provides a user-friendly, graphical interface with rich text rendering and visual separation of thinking blocks.

---

## Data Flow Diagram (ASCII)

```ascii
+-----------------+      HTTP POST /chat       +-------------------+
|                 | -------------------------> |                   |
|  User (Frontend)|                            |  Python Backend   |
|   [CLI / Web]   | <------------------------- |     (FastAPI)     |
|                 |      SSE Stream            |                   |
+-----------------+      (JSON Chunks)         +---------+---------+
                                                         |
                                                         | query()
                                                         v
                                               +-------------------+
                                               |                   |
                                               |  Claude Agent SDK |
                                               |                   |
                                               +---------+---------+
                                                         |
                                                         | API Request
                                                         v
                                               +-------------------+
                                               |                   |
                                               |   Anthropic API   |
                                               |   (Claude Model)  |
                                               |                   |
                                               +-------------------+
```

---

## Data Flow Breakdown

1.  **Request:** The user inputs a message in the frontend. The frontend sends a `POST` request to `http://localhost:8000/chat` with the `prompt` and an optional `session_id`.
2.  **Session Management:** The backend checks the `session_id`. If it exists, it retrieves the active agent session; otherwise, it creates a new one.
3.  **Agent Query:** The backend calls `session_client.query(prompt)` using the Claude Agent SDK.
4.  **Streaming:** The backend listens to the `session_client.receive_response()` stream.
5.  **Event Processing:** As the SDK yields events (Thinking Blocks or Text Blocks), the backend formats them into Server-Sent Events (SSE) and yields them to the frontend immediately.
6.  **Rendering:** The frontend receives these events chunk-by-chunk and updates the UI in real-time.

---

## Agent Lifecycle

1.  **Initialization:** When the backend starts, the `agent.manager` module initializes the base Agent configuration (model selection, system prompt).
2.  **Session Creation:** When a user first connects, a `session_client` is spawned. This client holds the conversation history in memory.
3.  **Interaction:** The session remains active, appending new user messages and assistant responses to its history.
4.  **Termination:** Currently, sessions are in-memory and persist until the backend server is restarted.

---

## Why a Separate Backend?

You might ask: *Why not connect the Frontends directly to Claude?*

1.  **Security:** Your API Key (`ANTHROPIC_API_KEY`) is stored securely on the server. If the frontend (especially a web browser) connected directly, you would expose your secret key to the world.
2.  **Centralization:** Logic for agent configuration, tools, and session management is kept in one place. Both frontends benefit from updates to the backend.
3.  **Control:** You can enforce rate limits, logging, and custom logic before the request ever reaches Claude.
