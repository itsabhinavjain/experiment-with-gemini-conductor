import { logger } from './logger';

export interface ChatResponseChunk {
  type: 'session_id' | 'thinking' | 'text' | 'error';
  content: string;
}

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL || 'http://localhost:8000';

/**
 * Streams chat responses from the backend.
 */
export async function* streamChat(prompt: string, sessionId?: string): AsyncGenerator<ChatResponseChunk> {
  logger.info(`Starting chat stream for session: ${sessionId || 'new'}`);
  const response = await fetch(`${BACKEND_URL}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ prompt, session_id: sessionId }),
  });

  if (!response.ok) {
    logger.error(`HTTP error! status: ${response.status}`);
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const reader = response.body?.getReader();
  if (!reader) {
    logger.error('Response body is not readable');
    throw new Error('Response body is not readable');
  }

  const decoder = new TextDecoder();
  let buffer = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      logger.info('Stream completed');
      break;
    }

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split('\n');
    buffer = lines.pop() || '';

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const jsonStr = line.slice(6).trim();
        if (jsonStr) {
          try {
            const chunk: ChatResponseChunk = JSON.parse(jsonStr);
            yield chunk;
          } catch (e) {
            logger.error(`Error parsing SSE chunk: ${e} | Content: ${jsonStr}`);
          }
        }
      }
    }
  }
}
