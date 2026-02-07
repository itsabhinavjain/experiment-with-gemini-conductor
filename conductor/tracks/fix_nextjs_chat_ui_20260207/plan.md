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

## Phase 2: Auto-Scroll to Latest Message
Goal: The chat should automatically scroll down whenever new messages or streaming chunks arrive.

- [ ] **Task: Write tests for Auto-scroll behavior**
    - [ ] Mock message additions and verify the scroll position moves to the bottom.
- [ ] **Task: Implement Auto-scroll logic**
    - [ ] Use `useRef` and `useEffect` in `MessageList.tsx` to trigger `scrollIntoView` or `scrollTop` updates when messages change.
- [ ] **Task: Conductor - User Manual Verification 'Phase 2: Auto-Scroll' (Protocol in workflow.md)**

## Phase 3: Markdown Overflow Fixes
Goal: Fix horizontal overflow for long words and ensure code blocks scroll horizontally.

- [ ] **Task: Write tests for Markdown Overflow**
    - [ ] Verify message bubbles have `overflow-wrap: break-word` or `word-break: break-all`.
    - [ ] Verify code blocks (`pre`/`code`) have `overflow-x: auto`.
- [ ] **Task: Implement Styling for Overflow**
    - [ ] Update `src/components/MessageItem.tsx` (or the relevant markdown renderer component) to apply word-wrapping styles.
    - [ ] Update global CSS or component styles to ensure code blocks within chat bubbles scroll horizontally.
- [ ] **Task: Conductor - User Manual Verification 'Phase 3: Markdown Overflow' (Protocol in workflow.md)**
