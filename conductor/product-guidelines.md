# Product Guidelines

## Prose Style

The prose style for all documentation, code comments, and explanatory text within this project will be a blend of informative, beginner-friendly, and concise.

**Key Principles:**

1.  **Beginner-Friendly and Educational (Primary Focus):**
    *   Prioritize clarity, simplicity, and step-by-step explanations.
    *   Break down complex concepts into digestible parts.
    *   Use analogies or common examples where appropriate to aid understanding.
    *   Avoid jargon without clear definitions.
    *   Code comments should explain *why* a particular piece of code is written, not just *what* it does, especially for non-obvious logic.

2.  **Informative and Technical (Supporting Detail):**
    *   Maintain technical accuracy and provide sufficient detail for experienced developers to understand the implementation.
    *   Where necessary, refer to official documentation or specifications.
    *   Ensure all technical terms are used correctly, with explanations provided for the target audience.

3.  **Concise and Reference-Oriented (Navigability):**
    *   Structure documents with clear headings, bullet points, and code blocks for easy scanning and quick lookups.
    *   While explanations should be thorough, avoid unnecessary verbosity. Get straight to the point after an introductory explanation.
    *   Provide runnable code snippets and clear examples wherever applicable.

**In essence, the goal is to create documentation that teaches effectively while serving as a reliable technical reference.**

---

## Engineering Principles

The project's development must adhere to the following principles:

-   **Operating Mode:** Always operate in the order: Architect -> Implement -> Explain.
-   **Teaching Reference:** The implementation should serve as a teaching reference project.
-   **Preferences:** Prefer clarity, modularity, minimalism, and readability in all code and design.
-   **Avoidances:** Avoid unnecessary abstractions, overly complex patterns, and hidden magic.
-   **Decision Making:** Make reasonable engineering decisions autonomously, always preferring official SDK patterns. When multiple approaches are available, choose the simplest modern one.
-   **Coherence:** Create a coherent system, not isolated code.
-   **Quality:** Write production-quality but beginner-readable code.

---

## Global Technical Standards

These standards apply across the entire project:

### Python Package Management

-   **Requirement:** Exclusively use `uv` for Python package management.
-   **Prohibition:** `pip`, `poetry`, and `pipenv` are explicitly NOT allowed.

### Environment Configuration

-   **Sensitive Data:** Use `.env` files for all environment-specific variables and secrets.
-   **Security:** Never hardcode API keys or other sensitive information directly into the codebase.

### Code Style and Readability

-   **Comments:** Utilize heavy inline comments to explain complex logic and design choices, especially for beginners.
-   **Naming:** Employ beginner-friendly, descriptive naming conventions for variables, functions, and classes.
-   **Separation of Concerns:** Ensure a clear and logical separation of concerns across modules and components.
-   **Asynchronous Design:** Where applicable and beneficial, implement an async-first design.

---

## User Experience Guidelines

### Thinking Blocks Requirement (CRITICAL)

-   **Visibility:** All frontends (Python Terminal and Next.js Web) MUST prominently display the following sequence for each interaction:
    ```
    User Message
    Assistant Response
    Thinking Blocks
    ```
-   **Structure:** Thinking blocks must be visible, structured, and clearly separated from other output elements.
-   **Streaming:** If the SDK supports streaming responses and thinking blocks, this functionality MUST be implemented in all frontends.

---

## Development Process Rules

### Mandatory Research

-   **SDK Documentation:** Before any code is written, a mandatory research phase requires reading the latest official Claude Agent SDK documentation (`https://platform.claude.com/docs/en/agent-sdk/overview`).
-   **SDK Patterns:** Adhere strictly to the latest SDK patterns, avoid outdated examples, and utilize native Agent SDK concepts.
-   **Internal Extraction:** Internally extract and understand the Agent lifecycle, streaming responses, thinking blocks/reasoning, sessions, and tool usage (if relevant).
-   **Prohibition:** Do NOT start coding until the SDK structure is thoroughly understood.

### Strict Prohibitions

-   Do NOT skip reading SDK documentation.
-   Do NOT invent APIs not present in the official documentation.
-   Do NOT hide reasoning blocks from the user interface.
-   Do NOT use `pip`, `poetry`, or `pipenv`.

### Behavioral Directive

-   Act like a calm, precise senior engineer building a teaching-quality reference implementation of the Claude Agent SDK. The goal is not just to build, but to make the system understandable.
