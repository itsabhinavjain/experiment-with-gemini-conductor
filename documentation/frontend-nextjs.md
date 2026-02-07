# Next.js Web Frontend Explained

The `nextjs-frontend` is a modern, responsive web application. It demonstrates how to integrate the Claude Agent SDK into a real-world product environment.

---

## Tech Stack
*   **Framework:** Next.js 14+ (App Router)
*   **Language:** TypeScript
*   **Styling:** Tailwind CSS + shadcn/ui
*   **Icons:** Lucide React
*   **Markdown:** `react-markdown` + `react-syntax-highlighter`

---

## Architecture: The "Chat Loop"

The core logic lives in `src/app/page.tsx` and `src/lib/api.ts`.

### 1. The API Layer (`api.ts`)
We use the native `fetch` API, but with a twist: **Streams**.

The `streamChat` function is an **Async Generator**. It connects to the backend and "yields" chunks of data one by one as they arrive over the network.

```typescript
// Simplified Concept
export async function* streamChat(prompt) {
  const response = await fetch('/chat', ...);
  const reader = response.body.getReader();

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    // Decode raw bytes to text
    const text = decoder.decode(value);
    // Parse SSE format ("data: {...}")
    const json = parseSSE(text); 
    yield json; // Hand off to the UI component
  }
}
```

### 2. The UI Layer (`page.tsx`)
The main component manages three pieces of state:
1.  `messages`: An array of all chat messages (User + Assistant).
2.  `sessionId`: To keep the conversation alive.
3.  `isLoading`: To disable the input box while waiting.

When you hit send:
1.  We append your message to the list immediately (Optimistic UI).
2.  We append a blank "Assistant" message placeholder.
3.  We start the `streamChat` loop.
4.  As chunks arrive, we **update that specific placeholder message** in real-time.

---

## Visualizing "Thinking"

One of the project's main goals is to make the AI's reasoning visible but unobtrusive.

*   **Component:** `ThinkingPanel.tsx`
*   **Design:** A collapsible accordion.
*   **Behavior:**
    *   It receives the `thinking` string.
    *   It renders it in a monospaced font within a yellow/gray container.
    *   It sits *above* the final answer, mirroring the actual order of generation (Thinking -> Speaking).

## Markdown & Code Highlighting

We use `react-markdown` to render the Assistant's response. This means:
*   **Bold** and *Italic* text works.
*   Lists are properly formatted.
*   **Code Blocks** are detected and passed to `react-syntax-highlighter`, giving them nice colors and formatting (like VS Code), which is essential for a coding assistant.
