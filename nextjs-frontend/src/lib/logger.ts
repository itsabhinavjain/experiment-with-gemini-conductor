/**
 * Utility for centralized logging with consistent timestamps and log levels.
 */

function getTimestamp(): string {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}-${minutes}-${seconds}`;
}

function formatMessage(level: string, message: string): string {
  return `[${getTimestamp()}] [${level}] ${message}`;
}

export const logger = {
  info: (message: string, ...args: any[]) => {
    console.info(formatMessage('INFO', message), ...args);
  },
  warn: (message: string, ...args: any[]) => {
    console.warn(formatMessage('WARN', message), ...args);
  },
  error: (message: string, ...args: any[]) => {
    console.error(formatMessage('ERROR', message), ...args);
  },
  debug: (message: string, ...args: any[]) => {
    if (process.env.NODE_ENV !== 'production') {
      console.debug(formatMessage('DEBUG', message), ...args);
    }
  },
};
