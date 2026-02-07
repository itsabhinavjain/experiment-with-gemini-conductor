# Specification: Track 02 - Python CLI Frontend

## Goal
Create a lightweight, terminal-based chat interface that interacts exclusively with the `python-backend`.

## Requirements
- **Stack:**
  - Python
  - `uv` for package management (MANDATORY)
  - `rich` for terminal UI (MANDATORY)
  - `httpx` or `requests` for API calls
- **Features:**
  - Connect to `python-backend` (NOT Claude directly).
  - Support streaming responses.
  - Display "User Message", "Assistant Response", and "Thinking Blocks".
  - Maintain session state (conversation continuity).
  - Clear and readable formatting using `rich`.
- **Folder Structure:**
  - `python-frontend/` (MANDATORY NAME)
- **Code Style:**
  - Heavy inline comments.
  - Beginner-friendly naming.

## UX Example
```
User: hello

A:
  Thinking:
    ...
  Response:
    ...
```
