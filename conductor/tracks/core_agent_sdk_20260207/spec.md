# Track: core_agent_sdk_20260207 - Core Claude Agent SDK Functionality with Python Backend and CLI

## 1. Overview

This track focuses on building the foundational components for demonstrating the Claude Agent SDK. It encompasses the development of a Python-based backend that interacts with the Claude Agent SDK, manages sessions, and exposes chat functionalities. Concurrently, a basic Python Command Line Interface (CLI) frontend will be developed to communicate with this backend, allowing users to send prompts and view the agent's responses, including its "thinking blocks," in real-time.

## 2. Goals

*   Establish a functional Python backend for Claude Agent SDK interaction.
*   Implement core agent functionalities: initialization, session management, prompt handling, streaming responses, and thinking block exposure.
*   Develop a basic CLI frontend capable of communicating with the backend and displaying agent output.
*   Adhere to project guidelines regarding code style, package management (`uv`), and environmental configuration (`.env`).
*   Ensure all interactions prioritize clarity and educational value, especially for beginners.

## 3. Scope

### In Scope:
*   Python FastAPI backend for Claude Agent SDK integration.
*   Claude Agent initialization and configuration within the backend.
*   Session management for maintaining conversational context.
*   `POST /chat` endpoint to handle user prompts, stream responses, and return thinking blocks.
*   `GET /health` endpoint for backend status checks.
*   Basic Python CLI frontend (using `rich`) to send prompts to the backend.
*   CLI display of streaming agent responses and thinking blocks.
*   Use of `uv` for Python package management across both Python components.
*   Configuration via `.env` files for sensitive information.

### Out of Scope for this Track:
*   Next.js web frontend development.
*   Advanced Claude Agent SDK features (e.g., tool integration beyond basic agent functionality).
*   Robust error handling beyond basic operational requirements.
*   Deployment automation beyond local development setup.
*   Comprehensive UI/UX design for the CLI (beyond basic readability and formatting).
*   Persistent storage for sessions (in-memory sessions are sufficient for this track).

## 4. Technical Details

### 4.1. Python Backend (`python-backend/`)
*   **Framework:** FastAPI
*   **Agent SDK:** Claude Agent SDK
*   **Responsibilities:**
    *   Initialize Claude Agent.
    *   Manage in-memory sessions (identified by `session_id`).
    *   Accept `POST /chat` requests containing user prompts.
    *   Process prompts using the Claude Agent SDK.
    *   Stream Assistant's `message` and `thinking` blocks in the response.
    *   Provide a `/health` endpoint.
*   **Response Structure (example for `POST /chat`):**
    ```json
    {
      "message": "...",
      "thinking": "...",
      "session_id": "..."
    }
    ```

### 4.2. Python Terminal Frontend (`python-frontend/`)
*   **Library:** `rich`
*   **Interaction:** Communicates ONLY with the `python-backend` via its API endpoints.
*   **Features:**
    *   Sends user prompts to `python-backend/chat`.
    *   Receives and displays streaming responses from the backend.
    *   Clearly displays `User Message`, `Assistant Response`, and `Thinking Blocks` in a structured format.
    *   Manages `session_id` to maintain conversation continuity with the backend.

### 4.3. Development Environment
*   **Python Version:** Compatible with Claude Agent SDK requirements (to be determined during research phase).
*   **Package Manager:** `uv` will be used exclusively for both `python-backend` and `python-frontend`.
*   **Environment Variables:** All API keys and sensitive configurations will be managed via `.env` files.

## 5. Deliverables

Upon completion, this track will deliver:
*   A fully functional `python-backend` service.
*   A functional `python-frontend` CLI application.
*   Code that adheres to the established prose style, code style, and engineering principles.
*   Initial setup of project structure (`python-backend/`, `python-frontend/`).
*   The system should allow for starting the backend and chatting from the terminal, with thinking blocks visible.
