'use client';

import React from 'react';
import ThinkingPanel from './ThinkingPanel';

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  thinking?: string;
}

interface MessageItemProps {
  message: Message;
}

export default function MessageItem({ message }: MessageItemProps) {
  const isUser = message.role === 'user';

  return (
    <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'} mb-4`}>
      <div
        className={`max-w-[80%] p-3 rounded-lg ${
          isUser ? 'bg-blue-600 text-white rounded-br-none' : 'bg-gray-200 text-gray-900 rounded-bl-none'
        }`}
      >
        <p className="whitespace-pre-wrap">{message.content}</p>
      </div>
      {!isUser && message.thinking && <ThinkingPanel thinking={message.thinking} />}
    </div>
  );
}
