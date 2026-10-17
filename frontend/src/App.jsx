import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import ChatInterface from './components/ChatInterface';
import VegetableCatalog from './components/VegetableCatalog';
import FertilizerCalculator from './components/FertilizerCalculator';
import GrowthStagesGuide from './components/GrowthStagesGuide';
import SettingsModal from './components/SettingsModal';
import './styles/components.css';

const INITIAL_MESSAGE = {
  role: 'assistant',
  content: `Hello! I am **Floramind**, an intelligent and reliable digital agricultural assistant specializing exclusively in **vegetable gardening, scientific plant characteristics, planting schedules, days to harvest, maturity periods, and fertilizer management**.

I am here to guide farmers, home gardeners, students, and commercial growers with accurate, science-based agricultural guidance from seed sowing to harvest.

**How to get started:**
- Ask about any vegetable (e.g., *"How do I grow Pechay in the Philippines?"*)
- Ask about fertilizer timing & dosage (e.g., *"What fertilizer should I use for a 50 sqm Ampalaya plot?"*)
- Explore the **Vegetable Catalog** tab for scientific profiles and days to harvest.
- Use the **Fertilizer Calculator** tab to compute exact N-P-K and compost dosages.

What vegetable crop are you planning or currently growing?`,
  model: 'Floramind AI Engine'
};

export default function App() {
  const [activeTab, setActiveTab] = useState('chat');
  const [messages, setMessages] = useState([INITIAL_MESSAGE]);
  const [systemStatus, setSystemStatus] = useState(null);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    fetchSystemStatus();
  }, []);

  const fetchSystemStatus = async () => {
    try {
      const res = await fetch('/api/admin/status');
      if (res.ok) {
        const data = await res.json();
        setSystemStatus(data);
      }
    } catch (e) {
      console.warn('Backend status check pending:', e);
    }
  };

  const handleAskQuestion = async (userQuery) => {
    if (!userQuery.trim() || isLoading) return;

    // 1. Add user message
    const newMessages = [
      ...messages,
      { role: 'user', content: userQuery }
    ];
    setMessages(newMessages);
    setIsLoading(true);

    try {
      // 2. Query chat endpoint
      const historyPayload = newMessages.slice(-6).map(m => ({
        role: m.role,
        content: m.content
      }));

      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userQuery,
          history: historyPayload,
          stream: false
        })
      });

      if (!res.ok) {
        throw new Error(`Server returned HTTP ${res.status}`);
      }

      const data = await res.json();

      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          content: data.reply,
          sources: data.sources,
          model: data.model,
          is_out_of_scope: data.is_out_of_scope
        }
      ]);
    } catch (error) {
      console.error('Chat error:', error);
      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          content: `I encountered an unexpected issue while retrieving agricultural data: ${error.message}. Please verify the Python backend is running or check your connection in Settings.`,
          model: 'System Error Handler'
        }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectVegetableForChat = (promptText) => {
    setActiveTab('chat');
    handleAskQuestion(promptText);
  };

  return (
    <div className="app-container">
      {/* Top Header & Navigation */}
      <Header
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        systemStatus={systemStatus}
        onOpenSettings={() => setIsSettingsOpen(true)}
      />

      {/* Main Tab Content */}
      <main className="main-content">
        {activeTab === 'chat' && (
          <ChatInterface
            messages={messages}
            setMessages={setMessages}
            onAskQuestion={handleAskQuestion}
            isLoading={isLoading}
          />
        )}

        {activeTab === 'catalog' && (
          <VegetableCatalog
            onSelectVegetableForChat={handleSelectVegetableForChat}
          />
        )}

        {activeTab === 'calculator' && (
          <FertilizerCalculator
            onAskInChat={handleSelectVegetableForChat}
          />
        )}

        {activeTab === 'stages' && (
          <GrowthStagesGuide
            onAskInChat={handleSelectVegetableForChat}
          />
        )}
      </main>

      {/* Settings & Credentials Modal */}
      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
        systemStatus={systemStatus}
        onRefreshStatus={fetchSystemStatus}
      />
    </div>
  );
}
