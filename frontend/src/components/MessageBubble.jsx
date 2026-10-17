import React, { useState } from 'react';
import { 
  Bot, 
  User, 
  Copy, 
  Check, 
  Volume2, 
  VolumeX, 
  Calendar, 
  Clock, 
  Leaf, 
  Beaker, 
  AlertCircle,
  ExternalLink 
} from 'lucide-react';

export default function MessageBubble({ message, onAskRelated }) {
  const [copied, setCopied] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);

  const isAssistant = message.role === 'assistant';

  const handleCopy = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleToggleSpeech = () => {
    if (!('speechSynthesis' in window)) {
      alert('Speech synthesis is not supported in this browser.');
      return;
    }

    if (isSpeaking) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
    } else {
      window.speechSynthesis.cancel(); // Stop any ongoing speech
      const cleanText = message.content
        .replace(/[*_#`[\]()]/g, '')
        .replace(/---/g, '')
        .trim();
        
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.rate = 1.0;
      utterance.pitch = 1.0;
      utterance.onend = () => setIsSpeaking(false);
      utterance.onerror = () => setIsSpeaking(false);
      
      window.speechSynthesis.speak(utterance);
      setIsSpeaking(true);
    }
  };

  // Simple Markdown Parser for tables, bolding, lists, and headings
  const renderFormattedContent = (content) => {
    const lines = content.split('\n');
    const elements = [];
    let inTable = false;
    let tableRows = [];

    const flushTable = () => {
      if (tableRows.length > 0) {
        const header = tableRows[0];
        const bodyRows = tableRows.slice(2); // Skip separator row
        elements.push(
          <div key={`table-${elements.length}`} style={{ overflowX: 'auto', margin: '14px 0' }}>
            <table>
              <thead>
                <tr>
                  {header.map((col, idx) => (
                    <th key={idx}>{col.trim()}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {bodyRows.map((row, rIdx) => (
                  <tr key={rIdx}>
                    {row.map((cell, cIdx) => (
                      <td key={cIdx}>{cell.trim()}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
        tableRows = [];
      }
      inTable = false;
    };

    lines.forEach((line, index) => {
      const trimmed = line.trim();

      // Check for table row
      if (trimmed.startsWith('|') && trimmed.endsWith('|')) {
        inTable = true;
        const cols = trimmed.slice(1, -1).split('|');
        tableRows.push(cols);
        return;
      } else if (inTable) {
        flushTable();
      }

      // Check for horizontal divider
      if (trimmed === '---') {
        elements.push(<hr key={index} style={{ border: 'none', borderTop: '1px solid var(--border-subtle)', margin: '16px 0' }} />);
        return;
      }

      // Check for standard Floramind section headers to style prominently
      if (trimmed.startsWith('Vegetable Name:')) {
        const nameVal = trimmed.replace('Vegetable Name:', '').trim();
        elements.push(
          <div key={index} style={{ display: 'flex', alignItems: 'center', gap: '8px', margin: '10px 0 4px 0' }}>
            <span className="badge badge-emerald"><Leaf size={12} /> Vegetable</span>
            <strong style={{ fontSize: '1.2rem', color: '#ffffff' }}>{nameVal}</strong>
          </div>
        );
        return;
      }

      if (trimmed.startsWith('Scientific Name:')) {
        const sciVal = trimmed.replace('Scientific Name:', '').trim();
        elements.push(
          <div key={index} style={{ fontSize: '0.925rem', color: 'var(--emerald-300)', marginBottom: '4px' }}>
            <strong>Scientific Name:</strong> <em>{sciVal.replace(/[*_]/g, '')}</em>
          </div>
        );
        return;
      }

      if (trimmed.startsWith('Vegetable Family:')) {
        const famVal = trimmed.replace('Vegetable Family:', '').trim();
        elements.push(
          <div key={index} style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', marginBottom: '14px' }}>
            <strong>Vegetable Family:</strong> <span style={{ color: 'var(--text-primary)' }}>{famVal}</span>
          </div>
        );
        return;
      }

      if (trimmed.startsWith('Days to Harvest:')) {
        const harvestVal = trimmed.replace('Days to Harvest:', '').trim();
        elements.push(
          <div key={index} style={{ 
            background: 'rgba(16, 185, 129, 0.1)', 
            border: '1px solid rgba(16, 185, 129, 0.3)',
            borderRadius: 'var(--radius-md)', 
            padding: '10px 14px', 
            margin: '12px 0',
            display: 'flex', 
            alignItems: 'center', 
            gap: '10px' 
          }}>
            <Calendar size={20} color="var(--emerald-400)" />
            <div>
              <div style={{ fontSize: '0.75rem', textTransform: 'uppercase', color: 'var(--emerald-400)', fontWeight: 700 }}>Days to Harvest</div>
              <div style={{ fontSize: '0.95rem', fontWeight: 600, color: '#ffffff' }}>{harvestVal}</div>
            </div>
          </div>
        );
        return;
      }

      if (trimmed.startsWith('Days to Maturity:')) {
        const matVal = trimmed.replace('Days to Maturity:', '').trim();
        elements.push(
          <div key={index} style={{ 
            background: 'rgba(245, 158, 11, 0.1)', 
            border: '1px solid rgba(245, 158, 11, 0.3)',
            borderRadius: 'var(--radius-md)', 
            padding: '10px 14px', 
            margin: '12px 0',
            display: 'flex', 
            alignItems: 'center', 
            gap: '10px' 
          }}>
            <Clock size={20} color="var(--amber-400)" />
            <div>
              <div style={{ fontSize: '0.75rem', textTransform: 'uppercase', color: 'var(--amber-400)', fontWeight: 700 }}>Days to Maturity</div>
              <div style={{ fontSize: '0.95rem', fontWeight: 600, color: '#ffffff' }}>{matVal}</div>
            </div>
          </div>
        );
        return;
      }

      if (trimmed.startsWith('Fertilizer Recommendation:')) {
        elements.push(
          <div key={index} style={{ marginTop: '16px', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span className="badge badge-amber"><Beaker size={12} /> Nutrition</span>
            <strong style={{ fontSize: '1.05rem', color: '#ffffff' }}>Fertilizer Recommendation</strong>
          </div>
        );
        return;
      }

      if (trimmed.startsWith('Planting Information:') || trimmed.startsWith('Harvesting Guide:') || trimmed.startsWith('Additional Growing Tips:')) {
        elements.push(
          <div key={index} style={{ marginTop: '14px', marginBottom: '6px' }}>
            <strong style={{ fontSize: '1.025rem', color: 'var(--emerald-300)' }}>{trimmed}</strong>
          </div>
        );
        return;
      }

      // Unordered list item
      if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
        const bulletText = trimmed.slice(2);
        elements.push(
          <li key={index} style={{ marginLeft: '18px', marginBottom: '4px' }}>
            {parseInlineStyling(bulletText)}
          </li>
        );
        return;
      }

      // Empty line
      if (!trimmed) {
        elements.push(<div key={index} style={{ height: '8px' }} />);
        return;
      }

      // Regular paragraph
      elements.push(
        <p key={index} style={{ marginBottom: '6px' }}>
          {parseInlineStyling(trimmed)}
        </p>
      );
    });

    if (inTable) {
      flushTable();
    }

    return elements;
  };

  // Helper to parse bolding (**text**) and italics (*text*)
  const parseInlineStyling = (text) => {
    const parts = text.split(/(\*\*.*?\*\*|\*.*?\*|`.*?`)/g);
    return parts.map((part, i) => {
      if (part.startsWith('**') && part.endsWith('**')) {
        return <strong key={i} style={{ color: '#ffffff' }}>{part.slice(2, -2)}</strong>;
      }
      if (part.startsWith('*') && part.endsWith('*')) {
        return <em key={i} style={{ color: 'var(--emerald-300)' }}>{part.slice(1, -1)}</em>;
      }
      if (part.startsWith('`') && part.endsWith('`')) {
        return (
          <code key={i} style={{ 
            background: 'rgba(0,0,0,0.3)', 
            padding: '2px 6px', 
            borderRadius: '4px',
            color: 'var(--emerald-400)',
            fontSize: '0.85em'
          }}>
            {part.slice(1, -1)}
          </code>
        );
      }
      return part;
    });
  };

  return (
    <div className={`message-row ${message.role}`}>
      <div className={`message-avatar ${message.role}`}>
        {isAssistant ? <Bot size={20} /> : <User size={20} />}
      </div>

      <div className="message-bubble-wrapper">
        <div className="message-bubble markdown-body">
          {renderFormattedContent(message.content)}
        </div>

        {/* Action Toolbar for Assistant responses */}
        {isAssistant && (
          <div className="message-meta">
            {message.model && (
              <span>Engine: <strong>{message.model}</strong></span>
            )}

            {message.sources && message.sources.length > 0 && (
              <span>Sources: {message.sources.join(', ')}</span>
            )}

            <div style={{ marginLeft: 'auto', display: 'flex', gap: '8px' }}>
              <button 
                className="meta-action-btn" 
                onClick={handleToggleSpeech} 
                title={isSpeaking ? "Stop Speaking" : "Read Aloud"}
              >
                {isSpeaking ? <VolumeX size={14} color="var(--amber-400)" /> : <Volume2 size={14} />}
                <span>{isSpeaking ? 'Stop' : 'Listen'}</span>
              </button>

              <button 
                className="meta-action-btn" 
                onClick={handleCopy} 
                title="Copy response to clipboard"
              >
                {copied ? <Check size={14} color="var(--emerald-400)" /> : <Copy size={14} />}
                <span>{copied ? 'Copied' : 'Copy'}</span>
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
