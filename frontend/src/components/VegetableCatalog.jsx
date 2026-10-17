import React, { useState, useEffect } from 'react';
import { 
  Search, 
  Leaf, 
  Calendar, 
  Clock, 
  MessageSquare, 
  Beaker, 
  Info, 
  X,
  Droplets,
  Sun,
  Thermometer,
  Layers
} from 'lucide-react';

export default function VegetableCatalog({ onSelectVegetableForChat }) {
  const [vegetables, setVegetables] = useState([]);
  const [families, setFamilies] = useState([]);
  const [selectedFamily, setSelectedFamily] = useState('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedVeg, setSelectedVeg] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchVegetables();
  }, []);

  const fetchVegetables = async () => {
    try {
      setLoading(true);
      const res = await fetch('/api/vegetables');
      if (res.ok) {
        const data = await res.json();
        setVegetables(data);

        // Extract unique families
        const fams = ['All', ...new Set(data.map(v => v.family.split(' ')[0]))];
        setFamilies(fams);
      }
    } catch (e) {
      console.error('Failed to load vegetables:', e);
    } finally {
      setLoading(false);
    }
  };

  const filteredVegetables = vegetables.filter(veg => {
    const matchesFamily = selectedFamily === 'All' || veg.family.toLowerCase().includes(selectedFamily.toLowerCase());
    const matchesSearch = 
      veg.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      veg.scientific_name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (veg.local_names && veg.local_names.some(n => n.toLowerCase().includes(searchQuery.toLowerCase())));
    return matchesFamily && matchesSearch;
  });

  return (
    <div className="catalog-container animate-fade-in">
      {/* Search and Filters Header */}
      <div className="glass-panel" style={{ padding: '20px' }}>
        <div className="catalog-header-bar">
          <div>
            <h2 style={{ fontSize: '1.4rem', color: '#ffffff' }}>Agricultural Vegetable Catalog</h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Scientifically verified profiles, days to harvest, and cultivation requirements
            </p>
          </div>

          <div className="catalog-search-box">
            <Search size={18} color="var(--emerald-400)" />
            <input
              type="text"
              placeholder="Search by vegetable, scientific, or local name..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
        </div>

        {/* Botanical Family Filter Pills */}
        <div style={{ marginTop: '16px', display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600 }}>Family:</span>
          {families.map((fam, idx) => (
            <button
              key={idx}
              className={`family-pill ${selectedFamily === fam ? 'active' : ''}`}
              onClick={() => setSelectedFamily(fam)}
            >
              {fam}
            </button>
          ))}
        </div>
      </div>

      {/* Grid of Vegetables */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '60px' }}>
          <div className="typing-dot" />
          <div className="typing-dot" style={{ margin: '0 8px' }} />
          <div className="typing-dot" />
          <div style={{ marginTop: '12px', color: 'var(--text-secondary)' }}>Loading verified vegetable database...</div>
        </div>
      ) : filteredVegetables.length === 0 ? (
        <div className="glass-panel" style={{ textAlign: 'center', padding: '50px' }}>
          <Leaf size={36} color="var(--text-muted)" style={{ margin: '0 auto 12px auto' }} />
          <h3>No vegetables matched your search</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginTop: '6px' }}>
            Try searching for another common or scientific name (e.g. Pechay, Ampalaya, Sitaw, Talong, Kamatis).
          </p>
        </div>
      ) : (
        <div className="vegetable-grid">
          {filteredVegetables.map(veg => (
            <div key={veg.id} className="glass-panel veg-card">
              <div className="veg-card-top">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <span className="badge badge-emerald">{veg.family.split(' ')[0]}</span>
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                    Germination: {veg.germination_period.split(' ')[0]} days
                  </span>
                </div>

                <h3>{veg.name}</h3>
                <div className="veg-scientific">{veg.scientific_name}</div>
              </div>

              {/* Stats Row */}
              <div className="veg-stats-row">
                <div className="veg-stat-item">
                  <span className="veg-stat-label">Days to First Harvest</span>
                  <span className="veg-stat-value" style={{ color: 'var(--emerald-300)' }}>
                    {veg.days_to_harvest.split('(')[0].trim()}
                  </span>
                </div>

                <div className="veg-stat-item">
                  <span className="veg-stat-label">Days to Maturity</span>
                  <span className="veg-stat-value" style={{ color: 'var(--amber-400)' }}>
                    {veg.days_to_maturity.split(' ')[0]} days
                  </span>
                </div>
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', marginTop: '4px' }}>
                <button
                  className="btn btn-secondary"
                  style={{ padding: '8px 10px', fontSize: '0.825rem' }}
                  onClick={() => setSelectedVeg(veg)}
                >
                  <Info size={14} />
                  <span>View Details</span>
                </button>

                <button
                  className="btn btn-primary"
                  style={{ padding: '8px 10px', fontSize: '0.825rem' }}
                  onClick={() => onSelectVegetableForChat(`How do I cultivate ${veg.name} (${veg.scientific_name})? Please give me the complete planting, harvest days, and fertilizer guide.`)}
                >
                  <MessageSquare size={14} />
                  <span>Ask Floramind</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Vegetable Detail Modal Sheet */}
      {selectedVeg && (
        <div className="modal-overlay animate-fade-in" onClick={() => setSelectedVeg(null)}>
          <div className="glass-panel modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <div>
                <span className="badge badge-emerald">{selectedVeg.family}</span>
                <h2 style={{ marginTop: '4px' }}>{selectedVeg.name}</h2>
                <div style={{ color: 'var(--emerald-300)', fontStyle: 'italic', fontSize: '0.95rem' }}>
                  {selectedVeg.scientific_name}
                </div>
              </div>
              <button className="close-btn" onClick={() => setSelectedVeg(null)}>
                <X size={22} />
              </button>
            </div>

            {/* Environmental Requirements Card */}
            <div className="settings-section">
              <div className="settings-section-title">
                <Thermometer size={16} />
                <span>Growing Requirements & Environmental Factors</span>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', fontSize: '0.85rem' }}>
                <div><strong>Temperature:</strong> {selectedVeg.ideal_conditions?.temperature}</div>
                <div><strong>Sunlight:</strong> {selectedVeg.ideal_conditions?.sunlight}</div>
                <div><strong>Soil Type:</strong> {selectedVeg.ideal_conditions?.soil_type}</div>
                <div><strong>Soil pH:</strong> {selectedVeg.ideal_conditions?.soil_ph}</div>
                <div><strong>Watering:</strong> {selectedVeg.ideal_conditions?.water_needs}</div>
                <div><strong>Plant Spacing:</strong> {selectedVeg.ideal_conditions?.spacing}</div>
              </div>
            </div>

            {/* Planting & Harvesting Times */}
            <div className="settings-section">
              <div className="settings-section-title">
                <Calendar size={16} />
                <span>Timeline & Harvesting Protocol</span>
              </div>
              <div style={{ fontSize: '0.88rem', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <div><strong>Planting Method:</strong> {selectedVeg.planting_method}</div>
                <div><strong>Germination:</strong> {selectedVeg.germination_period}</div>
                <div><strong>Seedling Age / Transplanting:</strong> {selectedVeg.seedling_age_transplant}</div>
                <div><strong>Days to First Harvest:</strong> {selectedVeg.days_to_harvest}</div>
                <div><strong>Days to Maturity:</strong> {selectedVeg.days_to_maturity}</div>
                <div style={{ marginTop: '4px' }}>
                  <strong>Harvesting Indicators:</strong> {selectedVeg.harvesting_guide}
                </div>
              </div>
            </div>

            {/* Fertilizer Guide */}
            <div className="settings-section">
              <div className="settings-section-title">
                <Beaker size={16} />
                <span>Fertilizer Management</span>
              </div>
              <div style={{ fontSize: '0.88rem', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <div><strong>Recommended Nutrients:</strong> {selectedVeg.fertilizer_recommendation?.nutrients}</div>
                <div><strong>Application Schedule:</strong> {selectedVeg.fertilizer_recommendation?.timing_method}</div>
                <div><strong>Rate Summary:</strong> {selectedVeg.fertilizer_recommendation?.rates_summary}</div>
              </div>
            </div>

            {/* Practical Advice & Citations */}
            <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              <strong>Growing Tips:</strong> {selectedVeg.growing_tips}
            </div>

            {selectedVeg.citations && (
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                <strong>Citations:</strong> {selectedVeg.citations.join('; ')}
              </div>
            )}

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button 
                className="btn btn-primary"
                onClick={() => {
                  const veg = selectedVeg;
                  setSelectedVeg(null);
                  onSelectVegetableForChat(`How do I cultivate ${veg.name}? Please provide planting steps, days to harvest, and fertilizer rates.`);
                }}
              >
                <MessageSquare size={16} />
                <span>Ask Floramind in Chat</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
