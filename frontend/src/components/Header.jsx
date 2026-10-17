import React from 'react';
import { 
  Sprout, 
  MessageSquare, 
  BookOpen, 
  Calculator, 
  Clock, 
  Settings, 
  Cpu, 
  Database, 
  Sparkles 
} from 'lucide-react';

export default function Header({ 
  activeTab, 
  setActiveTab, 
  systemStatus, 
  onOpenSettings 
}) {
  const geminiReady = systemStatus?.gemini?.configured || systemStatus?.gemini?.has_key;
  const pineconeCloud = systemStatus?.pinecone?.connected;
  
  return (
    <header className="header">
      <div className="header-inner">
        {/* Brand */}
        <div className="brand-wrapper" onClick={() => setActiveTab('chat')}>
          <div className="brand-icon">
            <Sprout size={24} />
          </div>
          <div className="brand-text">
            <h1>
              Floramind <span className="badge badge-emerald">AI Vegetable Assistant</span>
            </h1>
            <p>Dedicated Vegetable Cultivation & Scientific Agronomy Guide</p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="nav-tabs" aria-label="Main Navigation">
          <button 
            className={`nav-tab-btn ${activeTab === 'chat' ? 'active' : ''}`}
            onClick={() => setActiveTab('chat')}
          >
            <MessageSquare size={16} />
            <span>Floramind Chat</span>
          </button>
          
          <button 
            className={`nav-tab-btn ${activeTab === 'catalog' ? 'active' : ''}`}
            onClick={() => setActiveTab('catalog')}
          >
            <BookOpen size={16} />
            <span>Vegetable Catalog</span>
          </button>

          <button 
            className={`nav-tab-btn ${activeTab === 'calculator' ? 'active' : ''}`}
            onClick={() => setActiveTab('calculator')}
          >
            <Calculator size={16} />
            <span>Fertilizer Calculator</span>
          </button>

          <button 
            className={`nav-tab-btn ${activeTab === 'stages' ? 'active' : ''}`}
            onClick={() => setActiveTab('stages')}
          >
            <Clock size={16} />
            <span>Growth Stages Guide</span>
          </button>
        </nav>

        {/* Status Indicators & Settings */}
        <div className="header-actions">
          {/* Tech Stack Indicator */}
          <div className="status-pill" title="Google Gemini, Pinecone Vector DB, and Hugging Face embeddings">
            <div className={`status-dot ${geminiReady ? 'active' : 'in-memory'}`} />
            <span>Gemini + Pinecone + HF</span>
          </div>

          <button 
            className="btn btn-secondary" 
            onClick={onOpenSettings}
            title="Configure API Keys & View System Status"
            style={{ padding: '8px 12px' }}
          >
            <Settings size={16} />
            <span style={{ fontSize: '0.85rem' }}>Settings</span>
          </button>
        </div>
      </div>
    </header>
  );
}
