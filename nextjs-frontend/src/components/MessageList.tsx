'use client';

import React, { useEffect, useRef } from 'react';
import MessageItem, { Message } from './MessageItem';

interface MessageListProps {
  messages: Message[];
}

export default function MessageList({ messages }: MessageListProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="flex-1 h-full overflow-y-auto p-4 space-y-4">
      {messages.length === 0 ? (
        <div className="text-center text-gray-500 mt-10 italic">
          No messages yet. Start a conversation!
        </div>
      ) : (
        messages.map((msg, index) => (
          <MessageItem key={index} message={msg} />
        ))
      )}
      <div ref={messagesEndRef} />
    </div>
  );
}
