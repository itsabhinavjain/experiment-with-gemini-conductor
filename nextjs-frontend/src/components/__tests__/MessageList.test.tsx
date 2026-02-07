import { render, screen } from '@testing-library/react';
import MessageList from '../MessageList';
import { expect, test, vi } from 'vitest';

// Mock scrollIntoView since jsdom doesn't implement it
window.HTMLElement.prototype.scrollIntoView = vi.fn();

test('MessageList has overflow-y-auto class', () => {
  const { container } = render(<MessageList messages={[]} />);
  const scrollContainer = container.firstChild as HTMLElement;
  expect(scrollContainer.className).toContain('overflow-y-auto');
});

test('MessageList root element should have h-full to occupy constrained parent space', () => {
    const { container } = render(<MessageList messages={[]} />);
    const scrollContainer = container.firstChild as HTMLElement;
    expect(scrollContainer.className).toContain('h-full');
});

test('MessageList scrolls to bottom when messages change', () => {
    const scrollSpy = window.HTMLElement.prototype.scrollIntoView;
    const initialMessages = [{ role: 'user', content: 'hello' }] as any;
    const { rerender } = render(<MessageList messages={initialMessages} />);
    
    // Initial render should call scrollIntoView
    expect(scrollSpy).toHaveBeenCalled();
    vi.clearAllMocks();

    const newMessages = [...initialMessages, { role: 'assistant', content: 'hi' }];
    rerender(<MessageList messages={newMessages} />);
    
    // Rerender with new messages should call scrollIntoView again
    expect(scrollSpy).toHaveBeenCalled();
});
