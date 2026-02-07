import { render, screen } from '@testing-library/react';
import MessageItem from '../MessageItem';
import { expect, test, vi } from 'vitest';

test('MessageItem container has break-words class', () => {
  const message = { role: 'user', content: 'test' } as any;
  const { container } = render(<MessageItem message={message} />);
  const proseContainer = container.querySelector('.prose');
  expect(proseContainer?.className).toContain('break-words');
});

test('MessageItem renders markdown content', () => {
  const message = { role: 'user', content: '**bold text**' } as any;
  render(<MessageItem message={message} />);
  const boldElement = screen.getByText('bold text');
  expect(boldElement.tagName).toBe('STRONG');
});
