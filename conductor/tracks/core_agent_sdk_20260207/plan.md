# Plan for Track: core_agent_sdk_20260207

## Track Description
Build the core functionality for the Claude Agent SDK with Python backend, including agent initialization, session management, and basic chat endpoints with streaming responses and thinking blocks, and also implement a basic Python CLI to interact with it.

---

## Phase 1: Python Backend Core Setup and Agent Integration

This phase focuses on setting up the basic Python backend project structure, integrating the Claude Agent SDK, and implementing core chat functionalities including streaming and thinking blocks.

- [ ] Task: Research Claude Agent SDK Documentation
    - [ ] Research: Read the latest official Claude Agent SDK documentation (https://platform.claude.com/docs/en/agent-sdk/overview).
    - [ ] Research: Internally extract agent lifecycle, streaming responses, thinking blocks/reasoning, sessions, and tools (if relevant).
    - [ ] Research: Understand latest SDK patterns and avoid outdated examples.
- [ ] Task: Set up `python-backend` Project Structure
    - [ ] Action: Create the `python-backend/` directory.
    - [ ] Action: Initialize `uv` project within `python-backend/`.
    - [ ] Action: Create basic FastAPI application structure (main.py, config.py, etc.).
    - [ ] Action: Configure `.env` for environment variables.
- [ ] Task: Implement Basic FastAPI Application
    - [ ] Write Tests: Create initial tests for FastAPI app health check.
    - [ ] Implement Feature: Create a `GET /health` endpoint that returns a simple status.
- [ ] Task: Integrate Claude Agent SDK
    - [ ] Write Tests: Create tests for agent initialization and basic interaction (non-streaming).
    - [ ] Implement Feature: Implement agent initialization module in backend.
    - [ ] Implement Feature: Add basic Claude Agent interaction logic.
- [ ] Task: Implement Session Management
    - [ ] Write Tests: Create tests for session creation, retrieval, and conversation history management.
    - [ ] Implement Feature: Implement in-memory session management for users.
    - [ ] Implement Feature: Associate agent interactions with user sessions.
- [ ] Task: Implement `POST /chat` Endpoint (Basic)
    - [ ] Write Tests: Create tests for sending prompts and receiving non-streaming responses.
    - [ ] Implement Feature: Create a `POST /chat` endpoint that accepts user prompts and uses the Claude Agent.
    - [ ] Implement Feature: Return basic agent response and session ID.
- [ ] Task: Implement Streaming Responses and Thinking Blocks in Backend
    - [ ] Write Tests: Create tests for the streaming output of agent responses and thinking blocks.
    - [ ] Implement Feature: Modify `POST /chat` to stream responses from the Claude Agent SDK.
    - [ ] Implement Feature: Parse and return thinking blocks from the agent's response in the stream.
- [ ] Task: Conductor - User Manual Verification 'Python Backend Core Setup and Agent Integration' (Protocol in workflow.md)

## Phase 2: Python CLI Frontend Development

This phase focuses on developing the Python CLI frontend to interact with the backend, displaying responses and thinking blocks.

- [ ] Task: Set up `python-frontend` Project Structure
    - [ ] Action: Create the `python-frontend/` directory.
    - [ ] Action: Initialize `uv` project within `python-frontend/`.
    - [ ] Action: Add `rich` as a dependency.
    - [ ] Action: Configure basic CLI script structure.
- [ ] Task: Implement CLI to Connect to Backend
    - [ ] Write Tests: Create tests for sending prompts to the backend `POST /chat` endpoint.
    - [ ] Implement Feature: Implement HTTP client in CLI to send prompts to `python-backend/chat`.
    - [ ] Implement Feature: Handle session ID for continuous conversation.
- [ ] Task: Display Streaming Responses and Thinking Blocks in CLI
    - [ ] Write Tests: Create tests for parsing and displaying streaming responses and thinking blocks from the backend.
    - [ ] Implement Feature: Implement logic to process the streamed output from the backend.
    - [ ] Implement Feature: Use `rich` to format and display `User Message`, `Assistant Response`, and `Thinking Blocks` clearly.
    - [ ] Implement Feature: Ensure streaming output is readable and structured.
- [ ] Task: Conductor - User Manual Verification 'Python CLI Frontend Development' (Protocol in workflow.md)
