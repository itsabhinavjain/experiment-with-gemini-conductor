'use client';

import React, { useState } from 'react';

interface ThinkingPanelProps {
  thinking: string;
}

export default function ThinkingPanel({ thinking }: ThinkingPanelProps) {
  const [isOpen, setIsOpen] = useState(true);

  if (!thinking) return null;

  return (
    <div className="my-2 border rounded-lg bg-yellow-50 overflow-hidden text-sm">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-4 py-2 flex justify-between items-center bg-yellow-100 font-semibold text-yellow-800"
      >
        <span>Claude's Thinking</span>
        <span>{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="p-4 text-yellow-900 whitespace-pre-wrap font-mono italic">
          {thinking}
        </div>
      )}
    </div>
  );
}
