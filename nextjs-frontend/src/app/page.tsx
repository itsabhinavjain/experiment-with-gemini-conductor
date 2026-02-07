'use client';

import React, { useState } from 'react';
import MessageList from '@/components/MessageList';
import ChatInput from '@/components/ChatInput';
import { Message } from '@/components/MessageItem';
import { streamChat } from '@/lib/api';

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [sessionId, setSessionId] = useState<string | undefined>();
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async (content: string) => {
    const userMessage: Message = { role: 'user', content };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    const assistantMessage: Message = { role: 'assistant', content: '', thinking: '' };
    setMessages((prev) => [...prev, assistantMessage]);

    try {
      let currentContent = '';
      let currentThinking = '';

      for await (const chunk of streamChat(content, sessionId)) {
        if (chunk.type === 'session_id') {
          setSessionId(chunk.content);
        } else if (chunk.type === 'thinking') {
          currentThinking += chunk.content;
          updateLastMessage(currentContent, currentThinking);
        } else if (chunk.type === 'text') {
          currentContent += chunk.content;
          updateLastMessage(currentContent, currentThinking);
        } else if (chunk.type === 'error') {
          updateLastMessage(currentContent, currentThinking, chunk.content);
        }
      }
    } catch (error) {
      console.error('Chat error:', error);
      updateLastMessage('', '', 'Failed to connect to backend.');
    } finally {
      setIsLoading(false);
    }
  };

  const updateLastMessage = (content: string, thinking: string, error?: string) => {
    setMessages((prev) => {
      const newMessages = [...prev];
      const last = newMessages[newMessages.length - 1];
      if (last && last.role === 'assistant') {
        last.content = error ? `Error: ${error}` : content;
        last.thinking = thinking;
      }
      return newMessages;
    });
  };

  return (
    <main className="flex flex-col h-screen max-w-4xl mx-auto border-x bg-white">
      <header className="p-4 border-b bg-gray-50 flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-gray-800">Claude Agent SDK</h1>
          <p className="text-xs text-gray-500">Reference Implementation</p>
        </div>
        {sessionId && (
          <span className="text-[10px] bg-gray-200 px-2 py-1 rounded font-mono text-gray-600">
            Session: {sessionId.slice(0, 8)}...
          </span>
        )}
      </header>

      <MessageList messages={messages} />

      <ChatInput onSend={handleSend} disabled={isLoading} />
      
      <footer className="p-2 text-center text-[10px] text-gray-400">
        Built with Next.js and Claude Agent SDK
      </footer>
    </main>
  );
}
