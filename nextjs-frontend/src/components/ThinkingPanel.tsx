'use client';

import React, { useState } from 'react';
import { ChevronDown, ChevronUp, Brain } from 'lucide-react';
import { cn } from '@/lib/utils';

interface ThinkingPanelProps {
  thinking: string;
}

export default function ThinkingPanel({ thinking }: ThinkingPanelProps) {
  const [isOpen, setIsOpen] = useState(true);

  if (!thinking) return null;

  return (
    <div className="my-3 border rounded-lg bg-slate-50 overflow-hidden text-sm border-slate-200 shadow-sm">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={cn(
          "w-full px-4 py-2.5 flex justify-between items-center transition-colors",
          isOpen ? "bg-slate-100 border-b border-slate-200" : "bg-white hover:bg-slate-50"
        )}
      >
        <div className="flex items-center gap-2 font-medium text-slate-700">
          <Brain className="w-4 h-4 text-purple-600" />
          <span>Claude's Thinking</span>
        </div>
        {isOpen ? (
          <ChevronUp className="w-4 h-4 text-slate-500" />
        ) : (
          <ChevronDown className="w-4 h-4 text-slate-500" />
        )}
      </button>
      {isOpen && (
        <div className="p-4 text-slate-600 whitespace-pre-wrap font-mono text-[13px] leading-relaxed italic bg-white/50">
          {thinking}
        </div>
      )}
    </div>
  );
}