import React, { useState, useEffect } from 'react';
import { 
  Calculator, 
  Beaker, 
  AlertTriangle, 
  CheckCircle2, 
  Leaf, 
  MessageSquare, 
  Calendar,
  Layers,
  ArrowRight
} from 'lucide-react';

const VEGETABLES = [
  { id: 'pechay', name: 'Pechay (Pak Choi)', defaultArea: 50 },
  { id: 'ampalaya', name: 'Ampalaya (Bitter Gourd)', defaultArea: 100 },
  { id: 'sitaw', name: 'Sitaw (Yardlong Bean)', defaultArea: 80 },
  { id: 'talong', name: 'Talong (Eggplant)', defaultArea: 100 },
  { id: 'kalabasa', name: 'Kalabasa (Squash)', defaultArea: 200 },
  { id: 'kamatis', name: 'Kamatis (Tomato)', defaultArea: 100 },
  { id: 'okra', name: 'Okra (Lady\'s Finger)', defaultArea: 80 },
  { id: 'sili', name: 'Sili (Chili / Pepper)', defaultArea: 60 },
  { id: 'kangkong', name: 'Kangkong (Water Spinach)', defaultArea: 40 },
  { id: 'repolyo', name: 'Repolyo (Cabbage)', defaultArea: 120 },
  { id: 'carrots', name: 'Carrots', defaultArea: 60 },
  { id: 'lettuce', name: 'Lettuce', defaultArea: 40 },
  { id: 'pipino', name: 'Pipino (Cucumber)', defaultArea: 100 },
  { id: 'labanos', name: 'Labanos (Radish)', defaultArea: 50 },
];

export default function FertilizerCalculator({ onAskInChat }) {
  const [selectedVeg, setSelectedVeg] = useState('pechay');
  const [areaSqm, setAreaSqm] = useState(50);
  const [soilCondition, setSoilCondition] = useState('medium');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    calculateFertilizer();
  }, [selectedVeg, areaSqm, soilCondition]);

  const calculateFertilizer = async () => {
    if (!areaSqm || areaSqm <= 0) return;
    try {
      setLoading(true);
      const res = await fetch('/api/calculator/fertilizer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          vegetable_id: selectedVeg,
          area_sqm: parseFloat(areaSqm),
          soil_condition: soilCondition
        })
      });
      if (res.ok) {
        const data = await res.json();
        setResults(data);
      }
    } catch (e) {
      console.error('Calculation error:', e);
    } finally {
      setLoading(false);
    }
  };

  const handleQuickArea = (val) => {
    setAreaSqm(val);
  };

  return (
    <div className="calc-container animate-fade-in">
      {/* Sidebar Controls */}
      <div className="glass-panel calc-sidebar">
        <h2>
          <Calculator size={22} color="var(--emerald-400)" />
          <span>Fertilizer Calculator</span>
        </h2>
        <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
          Calculate exact N-P-K nutrient doses and commercial fertilizer weights tailored to your specific vegetable plot size.
        </p>

        {/* Crop Selection */}
        <div className="form-group">
          <label>Select Vegetable Crop:</label>
          <select 
            className="form-control"
            value={selectedVeg}
            onChange={(e) => setSelectedVeg(e.target.value)}
          >
            {VEGETABLES.map(v => (
              <option key={v.id} value={v.id}>{v.name}</option>
            ))}
          </select>
        </div>

        {/* Plot Area in Sq. Meters */}
        <div className="form-group">
          <label>Planting Area (Square Meters, m²):</label>
          <input
            type="number"
            min="1"
            max="100000"
            className="form-control"
            value={areaSqm}
            onChange={(e) => setAreaSqm(e.target.value)}
          />
          {/* Quick Area Preset Buttons */}
          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', marginTop: '6px' }}>
            {[10, 25, 50, 100, 500, 1000].map(size => (
              <button
                key={size}
                type="button"
                className={`family-pill ${areaSqm === size ? 'active' : ''}`}
                style={{ padding: '3px 8px', fontSize: '0.75rem' }}
                onClick={() => handleQuickArea(size)}
              >
                {size} m²
              </button>
            ))}
          </div>
        </div>

        {/* Soil Fertility Condition */}
        <div className="form-group">
          <label>Soil Fertility Condition:</label>
          <select
            className="form-control"
            value={soilCondition}
            onChange={(e) => setSoilCondition(e.target.value)}
          >
            <option value="medium">Medium / Average Garden Loam (Standard)</option>
            <option value="low">Low Fertility / Sandy / Depleted (+25% dosage)</option>
            <option value="rich">High Organic Matter / Composted Soil (-25% dosage)</option>
          </select>
        </div>

        {/* Call to Chat */}
        {results && (
          <button
            className="btn btn-primary"
            style={{ marginTop: '10px' }}
            onClick={() => onAskInChat(`I am growing ${results.vegetable} on a ${results.planting_area_sqm} sqm plot with ${results.soil_fertility_level} soil fertility. Could you explain the exact application timing and tips for using Complete (14-14-14) and Urea?`)}
          >
            <MessageSquare size={16} />
            <span>Consult Floramind on Plan</span>
          </button>
        )}
      </div>

      {/* Results Display Panel */}
      <div className="calc-results-panel">
        {results ? (
          <>
            {/* Header info */}
            <div className="glass-panel" style={{ padding: '18px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
              <div>
                <span className="badge badge-emerald">Crop Plan</span>
                <h3 style={{ fontSize: '1.3rem', color: '#ffffff', marginTop: '2px' }}>
                  {results.vegetable} ({results.scientific_name})
                </h3>
              </div>
              <div style={{ display: 'flex', gap: '12px' }}>
                <span className="status-pill">Area: <strong>{results.planting_area_sqm} m²</strong></span>
                <span className="status-pill">Soil: <strong>{results.soil_fertility_level}</strong></span>
              </div>
            </div>

            {/* Commercial Materials Required KPI Grid */}
            <div className="calc-kpi-grid">
              <div className="kpi-card" style={{ borderLeft: '4px solid var(--emerald-400)' }}>
                <span className="kpi-label">Complete 14-14-14</span>
                <div className="kpi-value">{results.recommended_materials.complete_14_14_14_kg} <span style={{ fontSize: '1rem', color: 'var(--text-secondary)' }}>kg</span></div>
                <span className="kpi-subtext">Basal foundation application</span>
              </div>

              <div className="kpi-card" style={{ borderLeft: '4px solid #38bdf8' }}>
                <span className="kpi-label">Urea 46-0-0</span>
                <div className="kpi-value">{results.recommended_materials.urea_46_0_0_kg} <span style={{ fontSize: '1rem', color: 'var(--text-secondary)' }}>kg</span></div>
                <span className="kpi-subtext">Vegetative side-dress (Nitrogen)</span>
              </div>

              <div className="kpi-card" style={{ borderLeft: '4px solid var(--amber-400)' }}>
                <span className="kpi-label">Potash 0-0-60</span>
                <div className="kpi-value">{results.recommended_materials.potash_0_0_60_kg} <span style={{ fontSize: '1rem', color: 'var(--text-secondary)' }}>kg</span></div>
                <span className="kpi-subtext">Fruiting / flower set booster</span>
              </div>

              <div className="kpi-card" style={{ borderLeft: '4px solid #a855f7' }}>
                <span className="kpi-label">Organic Compost</span>
                <div className="kpi-value">{results.recommended_materials.organic_compost_kg} <span style={{ fontSize: '1rem', color: 'var(--text-secondary)' }}>kg</span></div>
                <span className="kpi-subtext">Humus & soil microbiome</span>
              </div>
            </div>

            {/* Step-by-Step Application Timeline */}
            <div className="glass-panel" style={{ padding: '24px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '16px' }}>
                <Calendar size={20} color="var(--emerald-400)" />
                <h3 style={{ fontSize: '1.15rem', color: '#ffffff' }}>Application Schedule & Stages</h3>
              </div>

              <div className="schedule-timeline">
                {results.application_schedule.map((step, idx) => (
                  <div key={idx} className="timeline-step">
                    <div className="timeline-step-num">{idx + 1}</div>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                      <strong style={{ color: 'var(--emerald-300)', fontSize: '0.95rem' }}>{step.stage}</strong>
                      <p style={{ fontSize: '0.88rem', color: 'var(--text-primary)' }}>{step.action}</p>
                      <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                        <strong>Agronomic Purpose:</strong> {step.purpose}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Overapplication Precautions Alert */}
            <div className="glass-panel" style={{ padding: '20px', borderLeft: '4px solid var(--amber-500)', background: 'rgba(245, 158, 11, 0.05)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--amber-400)', fontWeight: 700, marginBottom: '8px' }}>
                <AlertTriangle size={18} />
                <span>Precautions Against Overapplication & Fertilizer Burn</span>
              </div>
              <ul style={{ paddingLeft: '20px', fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                {results.precautions.map((p, idx) => (
                  <li key={idx} style={{ marginBottom: '4px' }}>{p}</li>
                ))}
              </ul>
            </div>
          </>
        ) : (
          <div className="glass-panel" style={{ textAlign: 'center', padding: '60px' }}>
            <Beaker size={36} color="var(--text-muted)" style={{ margin: '0 auto 12px auto' }} />
            <h3>Enter your plot size to compute fertilizer dosage</h3>
          </div>
        )}
      </div>
    </div>
  );
}
