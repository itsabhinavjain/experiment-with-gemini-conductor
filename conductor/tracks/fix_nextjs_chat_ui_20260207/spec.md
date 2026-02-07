# Specification - Fix Next.js Chat Scrolling and Markdown Overflow

## Overview
This track addresses two primary UI/UX issues in the Next.js chat interface:
1.  **Scrolling Failures:** The chat window is currently non-scrollable, prevents access to older messages, and does not automatically scroll to the latest message.
2.  **Markdown Overflow:** Long words/URLs and code blocks extend horizontally beyond the message bubble's boundaries.

## Functional Requirements

### 1. Chat Scrolling Implementation
-   **Scrollable Container:** The chat history area must be contained within a fixed-height or flex-growing area that allows vertical scrolling when content exceeds the viewport.
-   **Auto-Scroll to Bottom:** When a new message (or a new chunk of a streaming message) is added, the chat window must automatically scroll to the bottom.
-   **Reachability:** Users must be able to scroll up to view the entire chat history.

### 2. Markdown Overflow Fixes
-   **Word Wrapping:** Long strings, such as URLs or long technical terms, must wrap within the message bubble instead of overflowing.
-   **Code Block Scrolling:** Markdown code blocks (`<pre>` or `<code>` tags) must support internal horizontal scrolling if the code lines are wider than the message bubble.

## Non-Functional Requirements
-   **Responsive Design:** The fixes must work correctly across different screen sizes (desktop and mobile).
-   **Performance:** Scrolling should be smooth even with a large number of messages.

## Acceptance Criteria
-   [ ] Chat window displays a vertical scrollbar when message history is long.
-   [ ] Chat window automatically scrolls to the most recent message upon receiving new content.
-   [ ] Older messages are accessible by scrolling up.
-   [ ] Long URLs and words wrap within the chat bubble width.
-   [ ] Code blocks show a horizontal scrollbar if content is too wide, without breaking the chat bubble layout.

## Out of Scope
-   Adding new chat features (e.g., message editing, deletion).
-   Changes to the Python backend or CLI frontend.
