import React, { useState } from 'react';
import { 
  X, 
  Settings, 
  Check, 
  Cpu, 
  Database, 
  Sparkles, 
  Key, 
  ExternalLink, 
  RefreshCw,
  AlertCircle
} from 'lucide-react';

export default function SettingsModal({ 
  isOpen, 
  onClose, 
  systemStatus, 
  onRefreshStatus 
}) {
  const [geminiKey, setGeminiKey] = useState('');
  const [geminiModel, setGeminiModel] = useState(systemStatus?.gemini?.model || 'gemini-2.5-flash');
  const [pineconeKey, setPineconeKey] = useState('');
  const [pineconeIndex, setPineconeIndex] = useState(systemStatus?.pinecone?.index_name || 'floramind-vegetables');
  const [hfKey, setHfKey] = useState('');
  const [showKeys, setShowKeys] = useState(false);
  
  const [saving, setSaving] = useState(false);
  const [indexing, setIndexing] = useState(false);
  const [notification, setNotification] = useState(null);

  if (!isOpen) return null;

  const handleSave = async (e) => {
    e.preventDefault();
    setSaving(true);
    setNotification(null);
    try {
      const payload = {};
      if (geminiKey.trim()) payload.gemini_api_key = geminiKey.trim();
      if (geminiModel.trim()) payload.gemini_model = geminiModel.trim();
      if (pineconeKey.trim()) payload.pinecone_api_key = pineconeKey.trim();
      if (pineconeIndex.trim()) payload.pinecone_index = pineconeIndex.trim();
      if (hfKey.trim()) payload.huggingface_api_key = hfKey.trim();

      const res = await fetch('/api/admin/settings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (res.ok) {
        setNotification({ type: 'success', text: 'Settings updated successfully!' });
        onRefreshStatus();
      } else {
        setNotification({ type: 'error', text: 'Failed to update settings.' });
      }
    } catch (err) {
      setNotification({ type: 'error', text: `Error: ${err.message}` });
    } finally {
      setSaving(false);
    }
  };

  const handleTriggerIndex = async () => {
    setIndexing(true);
    setNotification(null);
    try {
      const res = await fetch('/api/admin/index-pinecone', { method: 'POST' });
      if (res.ok) {
        const data = await res.json();
        setNotification({ 
          type: 'success', 
          text: `Indexed ${data.indexed_count} vegetable profiles into ${data.mode}!` 
        });
        onRefreshStatus();
      }
    } catch (err) {
      setNotification({ type: 'error', text: `Indexing failed: ${err.message}` });
    } finally {
      setIndexing(false);
    }
  };

  return (
    <div className="modal-overlay animate-fade-in" onClick={onClose}>
      <div className="glass-panel modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>
            <Settings size={22} color="var(--emerald-400)" />
            <span>AI Stack & Connection Settings</span>
          </h2>
          <button className="close-btn" onClick={onClose}>
            <X size={20} />
          </button>
        </div>

        {/* Real-time Status Overview */}
        <div className="settings-section">
          <div className="settings-section-title">
            <Cpu size={16} />
            <span>Active Service Status</span>
          </div>
          <div className="status-indicator-box">
            <div className="service-card">
              <span className="service-card-name">Google Gemini</span>
              <span className="service-card-state" style={{ color: systemStatus?.gemini?.configured ? 'var(--emerald-400)' : 'var(--amber-400)' }}>
                {systemStatus?.gemini?.configured ? 'Connected' : 'Pending API Key'}
              </span>
              <span style={{ fontSize: '0.68rem', color: 'var(--text-muted)' }}>
                Model: {systemStatus?.gemini?.model || 'gemini-2.5-flash'}
              </span>
            </div>

            <div className="service-card">
              <span className="service-card-name">Pinecone Vector DB</span>
              <span className="service-card-state" style={{ color: systemStatus?.pinecone?.connected ? 'var(--emerald-400)' : 'var(--amber-400)' }}>
                {systemStatus?.pinecone?.mode || 'In-Memory Ready'}
              </span>
              <span style={{ fontSize: '0.68rem', color: 'var(--text-muted)' }}>
                Docs: {systemStatus?.pinecone?.vector_count || 14} indexed
              </span>
            </div>

            <div className="service-card">
              <span className="service-card-name">Hugging Face</span>
              <span className="service-card-state" style={{ color: 'var(--emerald-400)' }}>
                Active (Local Torch)
              </span>
              <span style={{ fontSize: '0.68rem', color: 'var(--text-muted)' }}>
                all-MiniLM-L6-v2 (384d)
              </span>
            </div>
          </div>
        </div>

        {notification && (
          <div style={{
            padding: '10px 14px',
            borderRadius: 'var(--radius-md)',
            background: notification.type === 'success' ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
            border: `1px solid ${notification.type === 'success' ? 'var(--emerald-500)' : '#ef4444'}`,
            color: notification.type === 'success' ? 'var(--emerald-300)' : '#fca5a5',
            fontSize: '0.85rem'
          }}>
            {notification.text}
          </div>
        )}

        {/* Settings Form */}
        <form onSubmit={handleSave} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {/* Gemini Settings */}
          <div className="settings-section">
            <div className="settings-section-title">
              <Sparkles size={16} />
              <span>Google Gemini API Configuration</span>
              <a 
                href="https://aistudio.google.com/app/apikey" 
                target="_blank" 
                rel="noreferrer"
                style={{ marginLeft: 'auto', fontSize: '0.75rem', color: 'var(--emerald-400)', display: 'flex', alignItems: 'center', gap: '3px' }}
              >
                Get Free API Key <ExternalLink size={12} />
              </a>
            </div>

            <div className="form-group">
              <label>Gemini API Key:</label>
              <input
                type={showKeys ? 'text' : 'password'}
                className="form-control"
                placeholder={systemStatus?.gemini?.has_key ? '•••••••••••••••••••••••• (Key Configured)' : 'AIzaSy...'}
                value={geminiKey}
                onChange={(e) => setGeminiKey(e.target.value)}
              />
            </div>

            <div className="form-group">
              <label>Gemini Model Version:</label>
              <select
                className="form-control"
                value={geminiModel}
                onChange={(e) => setGeminiModel(e.target.value)}
              >
                <option value="gemini-2.5-flash">gemini-2.5-flash (Fast & Accurate, Recommended)</option>
                <option value="gemini-2.0-flash">gemini-2.0-flash</option>
                <option value="gemini-1.5-flash">gemini-1.5-flash</option>
                <option value="gemini-1.5-pro">gemini-1.5-pro</option>
              </select>
            </div>
          </div>

          {/* Pinecone Settings */}
          <div className="settings-section">
            <div className="settings-section-title">
              <Database size={16} />
              <span>Pinecone Vector Database Configuration</span>
              <a 
                href="https://app.pinecone.io/" 
                target="_blank" 
                rel="noreferrer"
                style={{ marginLeft: 'auto', fontSize: '0.75rem', color: 'var(--emerald-400)', display: 'flex', alignItems: 'center', gap: '3px' }}
              >
                Get Free Pinecone Key <ExternalLink size={12} />
              </a>
            </div>

            <div className="form-group">
              <label>Pinecone API Key (Optional for cloud sync):</label>
              <input
                type={showKeys ? 'text' : 'password'}
                className="form-control"
                placeholder={systemStatus?.pinecone?.connected ? '•••••••••••••••••••••••• (Cloud Connected)' : 'pcsk_... (Leave blank for In-Memory Vector Store)'}
                value={pineconeKey}
                onChange={(e) => setPineconeKey(e.target.value)}
              />
            </div>

            <div className="form-group">
              <label>Index Name:</label>
              <input
                type="text"
                className="form-control"
                value={pineconeIndex}
                onChange={(e) => setPineconeIndex(e.target.value)}
              />
            </div>
          </div>

          {/* Hugging Face Settings */}
          <div className="settings-section">
            <div className="settings-section-title">
              <Key size={16} />
              <span>Hugging Face Configuration</span>
              <a 
                href="https://huggingface.co/settings/tokens" 
                target="_blank" 
                rel="noreferrer"
                style={{ marginLeft: 'auto', fontSize: '0.75rem', color: 'var(--emerald-400)', display: 'flex', alignItems: 'center', gap: '3px' }}
              >
                Hugging Face Token <ExternalLink size={12} />
              </a>
            </div>

            <div className="form-group">
              <label>Hugging Face Token (Optional - local SentenceTransformers is already active!):</label>
              <input
                type={showKeys ? 'text' : 'password'}
                className="form-control"
                placeholder="hf_... (Optional)"
                value={hfKey}
                onChange={(e) => setHfKey(e.target.value)}
              />
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', color: 'var(--text-secondary)', cursor: 'pointer' }}>
              <input 
                type="checkbox" 
                checked={showKeys} 
                onChange={(e) => setShowKeys(e.target.checked)} 
              />
              <span>Show API key text</span>
            </label>

            <button
              type="button"
              className="btn btn-secondary"
              style={{ fontSize: '0.8rem', padding: '6px 12px' }}
              onClick={handleTriggerIndex}
              disabled={indexing}
            >
              <RefreshCw size={14} className={indexing ? 'animate-spin' : ''} />
              <span>{indexing ? 'Indexing...' : 'Re-index Vector Store'}</span>
            </button>
          </div>

          {/* Form Actions */}
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Cancel
            </button>
            <button type="submit" className="btn btn-primary" disabled={saving}>
              <Check size={16} />
              <span>{saving ? 'Saving...' : 'Save & Connect'}</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
