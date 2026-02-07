'use client';

import React, { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { SendHorizontal } from 'lucide-react';

interface ChatInputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

export default function ChatInput({ onSend, disabled }: ChatInputProps) {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim() && !disabled) {
      onSend(input);
      setInput('');
    }
  };

  return (
    <div className="border-t bg-white p-4 shadow-[0_-1px_10px_rgba(0,0,0,0.05)]">
      <form onSubmit={handleSubmit} className="mx-auto flex max-w-4xl gap-3">
        <Input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask Claude anything..."
          disabled={disabled}
          className="h-11 rounded-xl bg-slate-50 border-slate-200 focus-visible:ring-blue-500"
        />
        <Button
          type="submit"
          disabled={disabled || !input.trim()}
          size="icon"
          className="h-11 w-11 shrink-0 rounded-xl bg-blue-600 hover:bg-blue-700 shadow-md transition-all active:scale-95"
        >
          <SendHorizontal className="h-5 w-5" />
        </Button>
      </form>
    </div>
  );
}