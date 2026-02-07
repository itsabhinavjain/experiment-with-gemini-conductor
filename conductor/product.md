# Product Definition - Claude Agent SDK Reference Project

## Initial Concept

Build a full-stack system demonstrating the Claude Agent SDK with a Python FastAPI backend, a Python CLI frontend, and a Next.js web frontend, using 'uv' for Python package management and displaying 'Thinking Blocks'.

## Primary Objective

Build a small full-stack system demonstrating the Claude Agent SDK with:
1.  Python backend connected to Claude Agent SDK
2.  Python terminal frontend (CLI client)
3.  Next.js frontend (web client)
4.  Documentation folder with beginner-friendly explanations

## Mandatory Research Phase (DO THIS FIRST)

Before writing any code:
Read the latest official documentation: `https://platform.claude.com/docs/en/agent-sdk/overview`

You MUST:
-   Follow latest SDK patterns
-   Avoid outdated examples
-   Use native Agent SDK concepts

Internally extract:
-   Agent lifecycle
-   Streaming responses
-   Thinking blocks / reasoning
-   Sessions
-   Tools (if relevant)

Do NOT start coding until you understand the SDK structure.

## Engineering Mode (IMPORTANT)

You are NOT just a coder.
You must operate in this order:
1.  Architect
2.  Implement
3.  Explain

Your implementation should feel like a teaching reference project.

**Prefer:**
-   clarity
-   modularity
-   minimalism
-   readability

**Avoid:**
-   unnecessary abstractions
-   overly complex patterns
-   hidden magic

## Required Folder Structure

Create EXACTLY this structure:

```
project-root/
│
├── python-backend/
├── python-frontend/
├── nextjs-frontend/
└── documentation/
```

Do NOT rename folders.

## Global Technical Requirements

### Python Package Management

You MUST use:
```bash
uv
```
NOT allowed: pip, poetry, pipenv

### Environment

-   Use `.env`
-   Never hardcode API keys

### Code Style

-   Heavy inline comments
-   Beginner-friendly naming
-   Clear separation of concerns
-   Async-first design when possible

## Thinking Blocks Requirement (CRITICAL)

All frontends MUST display:
```
User Message
Assistant Response
Thinking Blocks
```

Thinking blocks must be:
-   Visible
-   Structured
-   Clearly separated

If SDK supports streaming:
👉 Implement streaming.

## PART 1 — Python Backend

Create a lightweight backend.

### Preferred Stack

-   FastAPI
-   Async Python
-   Claude Agent SDK
-   uv project

### Responsibilities

Backend must:
-   Initialize Claude Agent
-   Manage sessions
-   Accept prompts
-   Stream responses
-   Return thinking blocks

### Suggested Endpoints

```
POST /chat
GET /health
```

Example response structure:
```json
{
  "message": "...",
  "thinking": "...",
  "session_id": "..."
}
```

### Architecture Expectations

Backend should include:
-   agent initialization module
-   router module
-   schemas/models
-   streaming handler
-   env config

Keep it SIMPLE.

## PART 2 — Python Terminal Frontend

Create a CLI client that:
-   ONLY talks to python-backend
-   NEVER calls Claude directly

Suggested libraries:
-   `rich`
-   `prompt_toolkit`
-   `textual`

### CLI UX Example

```
User: hello

A:
  Thinking:
    ...
  Response:
    ...
```

Must support:
-   streaming output
-   readable formatting

## PART 3 — Next.js Frontend

Create a minimal Next.js app.

### Requirements

-   App Router
-   Simple chat UI
-   Calls backend API
-   Streams responses (if possible)
-   Displays thinking blocks

### UI Layout

```
[ Chat History ]

User message
Assistant response
Thinking panel (collapsible)
```

Avoid heavy design frameworks.

Keep UI minimal and educational.

## PART 4 — Documentation Folder (VERY IMPORTANT)

Create:
```
documentation/
```
Write for beginners.

### Required Files

#### `architecture.md`

Explain:
-   System overview
-   Data flow
-   Agent lifecycle
-   Why backend exists

Include a simple ASCII diagram.

#### `backend-explained.md`

Explain:
-   How agent SDK works
-   Sessions
-   Streaming
-   Thinking blocks

#### `frontend-python.md`

Explain:
-   CLI design
-   Streaming handling
-   Rendering thinking

#### `frontend-nextjs.md`

Explain:
-   API integration
-   UI rendering
-   State handling

#### `beginner-guide.md`

Explain VERY SIMPLY:
-   What is an AI agent?
-   What is Claude Agent SDK?
-   What are thinking blocks?
-   Why uv?
-   How everything connects

Pretend teaching someone new to AI.

## Implementation Strategy (FOLLOW STRICTLY)

1.  Read Claude Agent SDK docs
2.  Design architecture
3.  Initialize python-backend (uv)
4.  Implement agent connection
5.  Add streaming + thinking blocks
6.  Build CLI frontend
7.  Build Next.js frontend
8.  Write documentation LAST

## Autonomous Architect Rules

You MUST:
-   Create a coherent system, not isolated code
-   Make reasonable engineering decisions yourself
-   Prefer official SDK patterns
-   Write production-quality but beginner-readable code

If SDK offers multiple approaches:
👉 Choose the simplest modern one.

## Deliverable Expectations

Final project must allow me to:
-   ✅ Start backend
-   ✅ Chat from terminal
-   ✅ Chat from Next.js UI
-   ✅ View thinking blocks everywhere
-   ✅ Read clear beginner docs

## Strict Prohibitions

-   Do NOT skip reading SDK docs
-   Do NOT invent APIs not in docs
-   Do NOT hide reasoning blocks
-   Do NOT use pip/poetry

## Behavioral Directive

Act like:
A calm, precise senior engineer building a teaching-quality reference implementation of the Claude Agent SDK.

Your goal is not just to build — but to make the system understandable.
