'use client';

import React, { useState } from 'react';
import MessageList from '@/components/MessageList';
import ChatInput from '@/components/ChatInput';
import { Message } from '@/components/MessageItem';
import { streamChat } from '@/lib/api';
import { Sparkles } from 'lucide-react';
import { logger } from '@/lib/logger';

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [sessionId, setSessionId] = useState<string | undefined>();
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async (content: string) => {
    logger.info(`Sending message: ${content.slice(0, 50)}${content.length > 50 ? '...' : ''}`);
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
          logger.info(`Session established: ${chunk.content}`);
          setSessionId(chunk.content);
        } else if (chunk.type === 'thinking') {
          currentThinking += chunk.content;
          updateLastMessage(currentContent, currentThinking);
        } else if (chunk.type === 'text') {
          currentContent += chunk.content;
          updateLastMessage(currentContent, currentThinking);
        } else if (chunk.type === 'error') {
          logger.error(`Assistant reported error: ${chunk.content}`);
          updateLastMessage(currentContent, currentThinking, chunk.content);
        }
      }
    } catch (error) {
      logger.error(`Chat interaction failed: ${error}`);
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
    <div className="flex flex-col h-screen bg-slate-50 font-sans">
      <header className="shrink-0 border-b bg-white/80 backdrop-blur-md sticky top-0 z-10 shadow-sm">
        <div className="mx-auto flex max-w-4xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-2.5">
            <div className="bg-purple-600 p-1.5 rounded-lg">
              <Sparkles className="h-5 w-5 text-white" />
            </div>
            <div>
              <h1 className="text-lg font-bold tracking-tight text-slate-900 leading-none">Claude Agent</h1>
              <span className="text-[10px] font-medium uppercase tracking-wider text-slate-400">Reference UI</span>
            </div>
          </div>
          {sessionId && (
            <div className="flex items-center gap-2 rounded-full bg-slate-100 px-3 py-1 border border-slate-200">
              <div className="h-1.5 w-1.5 rounded-full bg-green-500 animate-pulse" />
              <span className="text-[11px] font-mono font-medium text-slate-600">
                {sessionId.slice(0, 8)}
              </span>
            </div>
          )}
        </div>
      </header>

      <div className="flex-1 overflow-hidden">
        <div className="h-full mx-auto max-w-4xl bg-transparent">
          <MessageList messages={messages} />
        </div>
      </div>

      <div className="shrink-0">
        <ChatInput onSend={handleSend} disabled={isLoading} />
        <p className="bg-white pb-3 text-center text-[10px] text-slate-400 font-medium">
          Educational reference implementation of the Claude Agent SDK
        </p>
      </div>
    </div>
  );
}