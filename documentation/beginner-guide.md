# Beginner's Guide: Understanding the Claude Agent SDK Project

Welcome! This guide is designed to explain **what** this project is, **why** it exists, and **how** its pieces fit together. We'll explore the core concepts of AI Agents and the Claude Agent SDK in simple terms.

---

## 1. What is an AI Agent?

Think of a standard AI (like ChatGPT or Claude on the web) as a **chatbot**. You talk to it, and it talks back.

An **AI Agent** is more like an **employee** or a **digital assistant**.
*   It doesn't just talk; it can **do things** (like search the web, run code, or save files).
*   It has **memory** (it remembers your conversation).
*   It can **think** and **plan** before it answers.

In this project, we are building a simple Agent that can hold a conversation and "think" out loud.

---

## 2. What is the Claude Agent SDK?

The **Claude Agent SDK** is a toolkit provided by Anthropic (the makers of Claude) to help developers build these Agents easily.

Instead of writing complex code to manage memory, connect to the AI model, and handle tools, the SDK gives us ready-made blocks.

**Key Features we use:**
*   **Agent Lifecycle:** Starting up an agent and keeping it running.
*   **Sessions:** Remembering who is talking (so you don't have to re-introduce yourself every message).
*   **Thinking Blocks:** Allowing the model to show its reasoning process before giving a final answer.

---

## 3. What are "Thinking Blocks"?

Have you ever asked a hard question and needed a moment to think? AI models are the same.

**Thinking Blocks** are a special feature where the AI "thinks out loud" in a hidden scratchpad before showing you the final result.

*   **Why is this good?** It makes the AI smarter and less likely to make mistakes on complex tasks.
*   **In our project:** We explicitly **show** you these blocks (in yellow panels) so you can see *how* the AI arrived at its answer. It's great for learning!

---

## 4. Why `uv`?

You might notice we use a tool called `uv` instead of the standard `pip`.

*   **Python Package Management:** Python code uses libraries (like Lego bricks) made by others. We need a tool to download and manage them.
*   **Speed:** `uv` is incredibly fast. It installs libraries in milliseconds instead of minutes.
*   **Modern Standard:** It represents the new, better way to manage Python projects.

---

## 5. How Everything Connects

This project is a **Full-Stack Application**. That means it has three main parts:

1.  **The Backend (Python):**
    *   This is the "Brain".
    *   It runs on your computer and talks directly to Claude.
    *   It uses **FastAPI** to create a web server.

2.  **The CLI Frontend (Python):**
    *   This is a "Terminal Interface".
    *   It looks like a hacker movie screen.
    *   It talks to the Backend to send your messages and show responses.

3.  **The Web Frontend (Next.js):**
    *   This is a "Website Interface".
    *   It looks like a modern chat app (like WhatsApp or Discord).
    *   It *also* talks to the same Backend.

**The Flow of a Message:**
1.  **You** type "Hello" in the Web UI.
2.  The **Web UI** sends "Hello" to the **Backend**.
3.  The **Backend** sends "Hello" to **Claude**.
4.  **Claude** thinks ("Thinking Block") and then replies ("Response").
5.  The **Backend** streams this data back to the **Web UI**.
6.  The **Web UI** updates your screen in real-time!

---

## Next Steps

Now that you understand the high-level concepts, check out the other guides for technical details:

*   [System Architecture](./architecture.md)
*   [Backend Explained](./backend-explained.md)
*   [Python CLI Frontend](./frontend-python.md)
*   [Next.js Web Frontend](./frontend-nextjs.md)
