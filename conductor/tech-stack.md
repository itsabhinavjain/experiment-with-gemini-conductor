# Tech Stack

This document outlines the core technologies and frameworks chosen for the Claude Agent SDK reference project.

## 1. Programming Languages

### Python
- **Role:** Primary language for the backend services and the terminal-based frontend.
- **Rationale:** Chosen for its extensive libraries, readability, strong community support, and direct compatibility with the Claude Agent SDK. Its asynchronous capabilities (asyncio) are critical for building a responsive backend.

### JavaScript/TypeScript
- **Role:** Primary language for the web frontend development.
- **Rationale:** Essential for modern web development, providing interactive user interfaces. TypeScript is preferred for enhanced code quality and maintainability through static typing.

## 2. Backend Technologies (Python)

### FastAPI
- **Type:** Web Framework
- **Role:** Used for building the RESTful API for the Python backend.
- **Rationale:** Selected for its high performance, asynchronous capabilities (ASGI), automatic OpenAPI (Swagger UI) documentation generation, and excellent developer experience. It aligns well with the async-first design principle.

#### `sse-starlette`
- **Role:** Provides Server-Sent Events (SSE) support for FastAPI.
- **Rationale:** Necessary for implementing the real-time streaming requirement for chat responses.

### Claude Agent SDK
- **Type:** AI Agent Integration
- **Role:** The core library for interacting with Claude AI agents, enabling the backend to manage sessions, process prompts, and retrieve responses including thinking blocks.
- **Rationale:** This is the foundational technology the entire project aims to demonstrate, ensuring direct integration with Claude's advanced AI capabilities.

## 3. Frontend Technologies

### Python Terminal Frontend (CLI)

#### `rich`
- **Type:** Terminal UI Library
- **Role:** Used for creating a rich and visually appealing command-line interface.
- **Rationale:** Provides advanced features for beautiful formatting, syntax highlighting, progress bars, tables, and more, significantly enhancing the user experience of the CLI client while making output readable and structured.

#### `httpx`
- **Type:** Async HTTP Client
- **Role:** Used for making asynchronous requests to the Python backend.
- **Rationale:** Chosen for its async support, which aligns with the project's async-first design principle, and its compatibility with Server-Sent Events (SSE).

### Next.js Frontend (Web)

#### Next.js
- **Type:** React Framework for Web
- **Role:** Powers the web-based chat interface.
- **Rationale:** Chosen for its support for React's App Router, server-side rendering (SSR), static site generation (SSG), and API routes, providing a robust and performant foundation for a modern web application. It simplifies development of a full-stack web application.

## 4. Development Tools & Standards

### `uv`
- **Type:** Python Package Manager
- **Role:** Exclusive tool for managing Python project dependencies and virtual environments.
- **Rationale:** Mandated for its speed and efficiency in dependency resolution and package installation, ensuring a consistent and rapid development workflow.

### `.env`
- **Type:** Environment Variable Management
- **Role:** Used for securely storing and managing environment-specific configurations and sensitive information (e.g., API keys).
- **Rationale:** Promotes best practices for security by never hardcoding sensitive data and allows for easy configuration across different environments.

## 5. Architectural Style

-   **Asynchronous First:** Design principle applied throughout the Python backend and wherever applicable in frontends to ensure responsiveness and efficient handling of I/O operations, particularly with streaming responses from the Claude Agent SDK.
-   **Modular Microservices (Conceptual):** While a small project, components are separated into distinct services (Python Backend, Python Frontend, Next.js Frontend) to demonstrate clear separation of concerns and potential for scaling.

## 6. Assumptions

-   **Backend Connectivity:** For development and testing of the `python-frontend`, it is assumed that the `python-backend` is implemented and running on `http://0.0.0.0:8000`.
-   **Backend Connectivity:** For development and testing of the `nextjs-frontend`, it is assumed that the `python-backend` is implemented and running on `http://0.0.0.0:8000`.
