# Track Specification: log_timestamps_20260207

**Overview**
Ensure that all server logs for both `python-backend` and `nextjs-frontend` include a timestamp in the format `[YYYY-MM-DD HH-MM-SS]` and the log level.

**Functional Requirements**
1.  **Python Backend:**
    *   Update the logging configuration in `python-backend/main.py` (and any other relevant files) to use the format: `[YYYY-MM-DD HH-MM-SS] - LEVEL - MESSAGE`.
    *   Ensure all application logs (info, error, etc.) follow this format.
2.  **Next.js Frontend:**
    *   Create a centralized logger utility (e.g., `src/lib/logger.ts`) that handles `info`, `warn`, `error`, and `debug` levels.
    *   The utility must prefix every log message with `[YYYY-MM-DD HH-MM-SS] [LEVEL]`.
    *   Replace existing `console.log/warn/error` calls in the application code with this new logger utility where appropriate.
    *   Modify the `dev` script in `package.json` to pipe the Next.js process output through a simple formatter script (to be created in `scripts/log-formatter.js`) that adds `[YYYY-MM-DD HH-MM-SS] [INFO]` (or appropriate level) to every line of output from the Next.js dev server.

**Non-Functional Requirements**
*   **Consistency:** The timestamp format `[YYYY-MM-DD HH-MM-SS]` must be strictly identical across both projects.
*   **Performance:** The logging wrapper in Next.js and the pipe script should be lightweight.

**Acceptance Criteria**
*   [ ] Starting `python-backend` shows logs like: `[2026-02-07 14-30-05] - INFO - Application startup...`
*   [ ] Starting `nextjs-frontend` (via `npm run dev`) shows logs like: `[2026-02-07 14-30-10] [INFO] next dev started...`
*   [ ] Application-level logs in both frontends and backends include the timestamp and level.

**Out of Scope**
*   Modifying logs for external third-party libraries unless they utilize the standard Python `logging` or can be easily intercepted.
