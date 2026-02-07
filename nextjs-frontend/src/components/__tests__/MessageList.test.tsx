import { render, screen } from '@testing-library/react';
import MessageList from '../MessageList';
import { expect, test } from 'vitest';

test('MessageList has overflow-y-auto class', () => {
  const { container } = render(<MessageList messages={[]} />);
  const scrollContainer = container.firstChild as HTMLElement;
  expect(scrollContainer.className).toContain('overflow-y-auto');
});

test('MessageList root element should have h-full to occupy constrained parent space', () => {
    // This is a test that will fail currently because MessageList only has flex-1
    const { container } = render(<MessageList messages={[]} />);
    const scrollContainer = container.firstChild as HTMLElement;
    expect(scrollContainer.className).toContain('h-full');
});
