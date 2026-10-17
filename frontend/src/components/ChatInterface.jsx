import React, { useState, useRef, useEffect } from 'react';
import { 
  Send, 
  Trash2, 
  ShieldCheck, 
  Sparkles, 
  HelpCircle, 
  Leaf, 
  Calendar, 
  Clock, 
  Beaker,
  AlertTriangle 
} from 'lucide-react';
import MessageBubble from './MessageBubble';

const SUGGESTIONS = [
  { text: "How to plant and care for Pechay from seed to harvest?", icon: "🌱" },
  { text: "What fertilizer schedule should I use for a 50 sqm Ampalaya plot?", icon: "💧" },
  { text: "Explain Kamatis days to first harvest vs days to full maturity", icon: "🍅" },
  { text: "How do I prevent fruit and shoot borers in Talong (Eggplant)?", icon: "🍆" },
  { text: "What are the soil and fertilizer requirements for Yardlong Beans (Sitaw)?", icon: "🌿" },
  { text: "How do I fix a broken car engine and replace spark plugs?", icon: "🛡️", isGuardrail: true }
];

export default function ChatInterface({ 
  messages, 
  setMessages, 
  onAskQuestion, 
  isLoading 
}) {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;
    const query = input.trim();
    setInput('');
    onAskQuestion(query);
  };

  const handleSuggestionClick = (text) => {
    if (isLoading) return;
    onAskQuestion(text);
  };

  const handleClearChat = () => {
    if (window.confirm('Are you sure you want to clear this conversation?')) {
      setMessages([
        {
          role: 'assistant',
          content: 'Hello! I am **Floramind**, an intelligent digital agricultural assistant specializing exclusively in **vegetable gardening, scientific plant characteristics, planting schedules, days to harvest, and fertilizer management**.\n\nHow can I assist your vegetable cultivation today? Ask me about any vegetable variety or request a fertilizer calculation for your plot!',
          model: 'Floramind AI'
        }
      ]);
    }
  };

  return (
    <div className="chat-layout">
      <div className="glass-panel chat-panel">
        {/* Top Control Bar */}
        <div className="chat-header-bar">
          <div className="scope-banner">
            <ShieldCheck size={16} color="var(--emerald-400)" />
            <span>Scope Restriction: <strong>Vegetable Cultivation & Scientific Agronomy Only</strong></span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <button 
              className="btn btn-ghost" 
              onClick={handleClearChat}
              title="Clear conversation"
              style={{ padding: '6px 10px', fontSize: '0.8rem' }}
            >
              <Trash2 size={14} />
              <span>Reset</span>
            </button>
          </div>
        </div>

        {/* Chat Messages */}
        <div className="chat-messages-container">
          {messages.length === 0 ? (
            <div className="chat-welcome animate-fade-in">
              <div className="welcome-icon-box">
                <Leaf size={32} />
              </div>
              <h2>Welcome to Floramind</h2>
              <p>
                Your dependable, science-based companion for vegetable production from seed sowing to harvesting and nutrient management.
              </p>

              {/* Suggestions */}
              <div className="prompt-chips-wrapper">
                <div className="prompt-chips-title">Recommended Vegetable Inquiries:</div>
                <div className="prompt-chips-grid">
                  {SUGGESTIONS.map((s, idx) => (
                    <button
                      key={idx}
                      className={`prompt-chip ${s.isGuardrail ? 'guardrail-chip' : ''}`}
                      onClick={() => handleSuggestionClick(s.text)}
                    >
                      <span>{s.icon}</span>
                      <span>{s.text}</span>
                    </button>
                  ))}
                </div>
              </div>
            </div>
          ) : (
            messages.map((msg, index) => (
              <MessageBubble 
                key={index} 
                message={msg} 
                onAskRelated={handleSuggestionClick} 
              />
            ))
          )}

          {/* Typing Indicator */}
          {isLoading && (
            <div className="message-row assistant animate-fade-in">
              <div className="message-avatar assistant">
                <Leaf size={18} />
              </div>
              <div className="message-bubble-wrapper">
                <div className="message-bubble" style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '14px 20px' }}>
                  <div className="typing-dot" />
                  <div className="typing-dot" />
                  <div className="typing-dot" />
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginLeft: '6px' }}>
                    Consulting vegetable agricultural knowledge base & Gemini...
                  </span>
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Suggestion Chips strip above input when messages exist */}
        {messages.length > 0 && (
          <div style={{ padding: '8px 20px', display: 'flex', gap: '8px', overflowX: 'auto', borderTop: '1px solid var(--border-subtle)' }}>
            {SUGGESTIONS.slice(0, 4).map((s, idx) => (
              <button
                key={idx}
                className="prompt-chip"
                style={{ padding: '4px 10px', fontSize: '0.78rem', whiteSpace: 'nowrap' }}
                onClick={() => handleSuggestionClick(s.text)}
              >
                <span>{s.icon}</span>
                <span>{s.text}</span>
              </button>
            ))}
          </div>
        )}

        {/* Chat Input Bar */}
        <div className="chat-input-bar">
          <form className="chat-input-form" onSubmit={handleSubmit}>
            <input
              ref={inputRef}
              type="text"
              className="chat-input-field"
              placeholder="Ask about any vegetable, planting days, maturity, or fertilizer needs (e.g. How to grow Pechay?)..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              disabled={isLoading}
            />

            <button 
              type="submit" 
              className="send-btn" 
              disabled={!input.trim() || isLoading}
              title="Send vegetable query"
            >
              <Send size={18} />
            </button>
          </form>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '6px', padding: '0 4px', fontSize: '0.725rem', color: 'var(--text-muted)' }}>
            <span>🌱 Floramind strictly addresses vegetable farming questions based on verified agronomy.</span>
            <span>Powered by Gemini 3.6 + Pinecone + Hugging Face</span>
          </div>
        </div>
      </div>
    </div>
  );
}
