# Implementation Plan - Fix Next.js Chat Scrolling and Markdown Overflow

## Phase 1: Chat Container Layout & Vertical Scrolling [checkpoint: 5feecc9]
Goal: Ensure the chat area has a fixed height relative to the viewport and allows vertical scrolling.

- [x] **Task: Write tests for Chat Window scrollability** fc68e31
    - [x] Verify that `MessageList` (or its container) has `overflow-y: auto` or `scroll`.
    - [x] Verify that the container has a constrained height.
- [x] **Task: Implement CSS fixes for Chat Container** fc68e31
    - [x] Update `src/components/MessageList.tsx` or `src/app/page.tsx` to ensure the message area fills available space but remains scrollable.
    - [x] Ensure the input area stays fixed at the bottom.
- [ ] **Task: Conductor - User Manual Verification 'Phase 1: Chat Container Layout' (Protocol in workflow.md)**

## Phase 2: Auto-Scroll to Latest Message [checkpoint: fc1ec19]
Goal: The chat should automatically scroll down whenever new messages or streaming chunks arrive.

- [x] **Task: Write tests for Auto-scroll behavior** 13a973a
- [x] **Task: Implement Auto-scroll logic** 13a973a
- [ ] **Task: Conductor - User Manual Verification 'Phase 2: Auto-Scroll' (Protocol in workflow.md)**

## Phase 3: Markdown Overflow Fixes
Goal: Fix horizontal overflow for long words and ensure code blocks scroll horizontally.

- [x] **Task: Write tests for Markdown Overflow** a5b2123
- [x] **Task: Implement Styling for Overflow** da12a97
- [ ] **Task: Conductor - User Manual Verification 'Phase 3: Markdown Overflow' (Protocol in workflow.md)**
