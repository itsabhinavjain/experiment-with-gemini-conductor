# Specification: Track 01 - Research and Python Backend Core

## Goal
Establish the backend foundation for the Claude Agent SDK reference project. This includes thorough research of the SDK and implementation of a FastAPI-based server.

## Requirements
- **Research:**
  - Read `https://platform.claude.com/docs/en/agent-sdk/overview`.
  - Extract: Agent lifecycle, streaming responses, thinking blocks/reasoning, sessions, and tools.
- **Backend Stack:**
  - Python (Async)
  - FastAPI
  - Claude Agent SDK
  - `uv` for package management (MANDATORY)
- **Features:**
  - Initialize Claude Agent.
  - Manage in-memory sessions.
  - `POST /chat`: Accept prompts, stream responses, return thinking blocks.
  - `GET /health`: Health check endpoint.
  - Error handling and logging.
- **Folder Structure:**
  - `python-backend/` (MANDATORY NAME)
- **Code Style:**
  - Heavy inline comments.
  - Beginner-friendly naming.
  - Async-first design.

## Output Format
- `message`: Assistant response.
- `thinking`: Thinking/reasoning block.
- `session_id`: Session identifier.
