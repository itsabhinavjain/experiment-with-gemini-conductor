'use client';

import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import ThinkingPanel from './ThinkingPanel';
import { cn } from '@/lib/utils';
import { User, Bot } from 'lucide-react';

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
    <div className={cn("flex w-full gap-4 mb-6", isUser ? "flex-row-reverse" : "flex-row")}>
      <div className={cn(
        "flex h-8 w-8 shrink-0 select-none items-center justify-center rounded-md border shadow",
        isUser ? "bg-white" : "bg-purple-600 border-purple-600 text-white"
      )}>
        {isUser ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
      </div>
      
      <div className={cn("flex flex-col gap-2 max-w-[85%]", isUser ? "items-end" : "items-start")}>
        {/* Render Thinking Block BEFORE content for Assistant */}
        {!isUser && message.thinking && (
          <div className="w-full">
            <ThinkingPanel thinking={message.thinking} />
          </div>
        )}
        
        <div className={cn(
          "px-4 py-3 rounded-2xl shadow-sm text-sm leading-relaxed",
          isUser 
            ? "bg-blue-600 text-white rounded-tr-none" 
            : "bg-white border border-slate-200 text-slate-900 rounded-tl-none"
        )}>
          <div className="prose prose-sm max-w-none dark:prose-invert break-words">
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              rehypePlugins={[rehypeRaw]}
              components={{
                code({ node, inline, className, children, ...props }: any) {
                  const match = /language-(\w+)/.exec(className || '');
                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      className="rounded-md my-2"
                      customStyle={{ margin: 0, padding: '1rem', overflowX: 'auto' }}
                      {...props}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={cn("bg-slate-100 px-1.5 py-0.5 rounded text-pink-600 font-mono text-[0.9em]", className)} {...props}>
                      {children}
                    </code>
                  );
                },
                p: ({ children }) => <p className="mb-2 last:mb-0">{children}</p>,
                ul: ({ children }) => <ul className="list-disc ml-4 mb-2">{children}</ul>,
                ol: ({ children }) => <ol className="list-decimal ml-4 mb-2">{children}</ol>,
              }}
            >
              {message.content}
            </ReactMarkdown>
          </div>
        </div>
      </div>
    </div>
  );
}