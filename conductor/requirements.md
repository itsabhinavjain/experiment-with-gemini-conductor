# Product Requirements - Claude Agent SDK Reference Project

This document outlines the detailed functional and non-functional requirements for the Claude Agent SDK reference project, serving as a blueprint for its development.

## 1. User Stories

The primary interactions users will have with the system are captured in the following stories:

*   **As a user, I want to send a text prompt to the Claude Agent and receive its response.**
*   **As a user, I want to see the Claude Agent's "thinking process" (thinking blocks) as it generates a response**, ensuring transparency and educational value.
*   **As a user, I want the conversation with the Claude Agent to be stateful**, allowing for continuity and context across multiple turns.

## 2. Functional Requirements

### 2.1. Overall System Interaction

*   The system must support streaming responses from the Claude Agent to both frontends (CLI and Web) for a real-time, interactive experience.
*   The system must handle input prompts of varying lengths and complexities.

### 2.2. Python Backend

The Python backend, built with FastAPI, must fulfill the following responsibilities:

*   **Initialize Claude Agent:** Properly initialize and configure the Claude Agent SDK.
*   **Manage Sessions:** Implement session management to maintain conversational history and state for each user.
*   **Accept Prompts:** Receive user prompts from the frontends.
*   **Stream Responses:** Stream responses from the Claude Agent back to the frontends, including both final output and intermediate thinking blocks.
*   **Return Thinking Blocks:** Ensure that the agent's internal reasoning (thinking blocks) are captured and returned to the frontends.
*   **Exposed Endpoints:** Provide the following API endpoints:
    *   `POST /chat`: For sending user prompts and receiving agent responses.
    *   `GET /health`: For health checks.
*   **Architecture Expectations:** Include clear modules for agent initialization, routing, schemas/models, a streaming handler, and environment configuration.

### 2.3. Python Terminal Frontend (CLI Client)

The CLI client must interact exclusively with the Python backend and adhere to the following:

*   **Backend Communication Only:** ONLY communicate with the `python-backend`.
*   **No Direct Claude Calls:** NEVER make direct calls to the Claude API.
*   **Streaming Output:** Support streaming output from the backend to provide a dynamic user experience.
*   **Readable Formatting:** Present responses and thinking blocks in a clear, readable, and well-formatted manner, potentially using libraries like `rich`.
*   **UX Example:**
    ```
    User: hello

    A:
      Thinking:
        ...
      Response:
        ...
    ```

### 2.4. Next.js Web Frontend

The Next.js web application must provide a minimal chat UI and interact with the Python backend:

*   **App Router:** Utilize the Next.js App Router for routing and component structure.
*   **Simple Chat UI:** Implement a clean and educational chat user interface.
*   **Calls Backend API:** All agent interactions must be routed through the Python backend API.
*   **Streams Responses:** Implement streaming for responses from the backend, if possible with Next.js capabilities.
*   **Displays Thinking Blocks:** Clearly display thinking blocks within the UI.
*   **UI Layout:**
    ```
    [ Chat History ]

    User message
    Assistant response
    Thinking panel (collapsible)
    ```
*   **Design:** Avoid heavy design frameworks; keep the UI minimal and educational.

## 3. Non-Functional Requirements

### 3.1. Performance

*   **Responsiveness:** The system should provide a responsive user experience, particularly concerning streaming responses.
*   **Efficiency:** The backend should efficiently manage resources, especially for session handling.

### 3.2. Maintainability & Readability

*   **Code Clarity:** Adhere to the "Engineering Principles" outlined in `product-guidelines.md`, prioritizing clarity, modularity, minimalism, and readability.
*   **Documentation:** Comprehensive and beginner-friendly documentation (as detailed in `product.md`) is a critical component of the project.

### 3.3. Security

*   **Environment Variables:** All API keys and sensitive information must be stored securely using `.env` files and never hardcoded.

### 3.4. Scalability

*   The architecture should ideally allow for independent scaling of backend and frontend components, even if not implemented in the initial prototype.

## 4. Global Technical Requirements (from agent_requirement.md)

These are overarching technical mandates for the project:

### Python Package Management

*   **Requirement:** Exclusively use `uv`.
*   **Prohibition:** `pip`, `poetry`, `pipenv` are NOT allowed.

### Environment

*   Use `.env` for configuration.
*   Never hardcode API keys.

### Code Style

*   Heavy inline comments.
*   Beginner-friendly naming.
*   Clear separation of concerns.
*   Async-first design when possible.

### Thinking Blocks Requirement (CRITICAL)

*   All frontends MUST display: User Message, Assistant Response, Thinking Blocks.
*   Thinking blocks must be visible, structured, and clearly separated.
*   If SDK supports streaming, streaming MUST be implemented.

## 5. Architectural Expectations (from agent_requirement.md)

*   Backend should include: agent initialization module, router module, schemas/models, streaming handler, env config. Keep it SIMPLE.
*   Required Folder Structure:
    ```
    project-root/
    │
    ├── python-backend/
    ├── python-frontend/
    ├── nextjs-frontend/
    └── documentation/
    ```
    Do NOT rename folders.

## 6. Development Strategy & Rules (from agent_requirement.md)

### Implementation Strategy (FOLLOW STRICTLY)

1.  Read Claude Agent SDK docs
2.  Design architecture
3.  Initialize python-backend (uv)
4.  Implement agent connection
5.  Add streaming + thinking blocks
6.  Build CLI frontend
7.  Build Next.js frontend
8.  Write documentation LAST

### Autonomous Architect Rules

*   Create a coherent system, not isolated code.
*   Make reasonable engineering decisions yourself.
*   Prefer official SDK patterns.
*   Write production-quality but beginner-readable code.
*   If SDK offers multiple approaches, choose the simplest modern one.

### Strict Prohibitions

*   Do NOT skip reading SDK docs.
*   Do NOT invent APIs not in docs.
*   Do NOT hide reasoning blocks.
*   Do NOT use pip/poetry.

### Behavioral Directive

*   Act like: A calm, precise senior engineer building a teaching-quality reference implementation of the Claude Agent SDK. Your goal is not just to build — but to make the system understandable.
