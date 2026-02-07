# Implementation Plan: log_timestamps_20260207

**Phase 1: Python Backend Logging Enhancement** [checkpoint: a59ea29]
- [x] Task: Configure custom logging format in `python-backend/main.py` e827c35
    - [x] Write a test case in `tests/test_logging_format.py` that intercepts logs and verifies the `[YYYY-MM-DD HH-MM-SS]` format.
    - [x] Update `logging.basicConfig` in `main.py` to use `format='[%(asctime)s] - %(levelname)s - %(message)s'` and `datefmt='%Y-%m-%d %H-%M-%S'`.
    - [x] Verify that all existing tests in `python-backend` still pass.
- [x] Task: Audit and update logging across backend modules e827c35
    - [x] Review `agent/manager.py` and `agent/session.py` to ensure they use the root logger or a child logger that inherits the format.
    - [x] Add log statements to key lifecycle events (session creation, agent query start/end) if missing.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Python Backend' (Protocol in workflow.md)

**Phase 2: Next.js Frontend Logger Utility**
- [x] Task: Implement `src/lib/logger.ts` 742445c
    - [x] Write unit tests in `src/lib/__tests__/logger.test.ts` for the logger utility.
    - [x] Implement `info`, `warn`, `error`, and `debug` methods that prepend `[YYYY-MM-DD HH-MM-SS] [LEVEL]`.
- [x] Task: Integrate logger into application code 742445c
    - [x] Replace `console.log`, `console.warn`, and `console.error` in `src/lib/api.ts` and `src/app/page.tsx` with the new logger.
    - [x] Verify that the application still functions correctly via existing component tests.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Next.js Utility' (Protocol in workflow.md)

**Phase 3: Next.js Dev Server Log Formatting** [checkpoint: ad38d3e]
- [x] Task: Create `scripts/log-formatter.js`
    - [x] Implement a lightweight Node.js script that reads from `stdin` and outputs each line prefixed with the timestamp.
    - [x] Add a simple test script to verify the formatter.
- [x] Task: Update `package.json` to use the formatter c8874c0
    - [x] Modify the `dev` script in `nextjs-frontend/package.json` to pipe output: `next dev | node scripts/log-formatter.js`.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Next.js Dev Server' (Protocol in workflow.md)

**Phase 4: Final Integration & Cleanup**
- [ ] Task: Final end-to-end verification
    - [ ] Start both servers and verify the visual consistency of logs in the terminal.
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Final Integration' (Protocol in workflow.md)
