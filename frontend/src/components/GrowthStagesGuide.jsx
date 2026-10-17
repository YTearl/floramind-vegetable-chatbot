import React from 'react';
import { 
  Clock, 
  Sprout, 
  Calendar, 
  CheckCircle, 
  Sun, 
  Droplet, 
  HelpCircle,
  ArrowRight,
  MessageSquare
} from 'lucide-react';

export default function GrowthStagesGuide({ onAskInChat }) {
  const STAGES = [
    {
      num: 1,
      title: "Seed Sowing & Germination",
      duration: "3 to 14 Days",
      icon: "🌱",
      desc: "Water activates enzymes inside the seed embryo. Proper temperature (20°C–30°C) and consistent moisture are critical. Emerging radicle (primary root) anchors first, followed by cotyledons (seed leaves).",
      action: "Direct sow in moist loose soil or in plug trays with fine potting mix."
    },
    {
      num: 2,
      title: "Seedling Establishment & Transplanting",
      duration: "10 to 35 Days After Sowing",
      icon: "🌿",
      desc: "Seedlings develop 3 to 5 true leaves and a sturdy root plug. Legumes (Sitaw) and root crops (Labanos, Carrots) are NEVER transplanted, while Solanaceous crops (Tomato, Eggplant) and Brassicas (Pechay, Cabbage) benefit from transplanting.",
      action: "Harden seedlings 3–5 days prior to transplanting by gradually exposing them to full sun."
    },
    {
      num: 3,
      title: "Vegetative Canopy & Branching",
      duration: "15 to 45 Days After Transplanting",
      icon: "☀️",
      desc: "Rapid stem, leaf, and root development. High Nitrogen demand to build photosynthetic factory. Staking, trellising (for Ampalaya, Sitaw, Tomato), and basal weed control are implemented here.",
      action: "Apply first side-dress of Nitrogen (Urea) and maintain uniform soil moisture."
    },
    {
      num: 4,
      title: "First Harvest (Days to First Harvest)",
      duration: "25 to 75 Days (Varies by crop)",
      icon: "✂️",
      desc: "The exact day the grower picks the very first marketable, edible leaves or fruits. For leafy crops like Pechay, this can be as early as 25–30 days. For fruiting crops like Tomato, this is around 55–70 days after transplanting.",
      action: "Harvest early morning when tissues are turgid and crisp; avoid bruising."
    },
    {
      num: 5,
      title: "Full Maturity & Extended Harvest Window",
      duration: "40 to 120+ Days Total",
      icon: "🧺",
      desc: "The duration over which a vegetable crop reaches physiological ripeness or continues yielding. Indeterminate crops (Ampalaya, Eggplant, Okra, Sitaw) produce flushes every 2–3 days for 2 to 4 months if regularly picked and fed.",
      action: "Side-dress balanced N-P-K and Potassium after each major flush to sustain vigor."
    }
  ];

  const CROPS_COMPARISON = [
    {
      category: "Leafy Vegetables (Pechay, Lettuce, Kangkong)",
      germination: "3–6 days",
      transplant: "10–15 days",
      firstHarvest: "25–35 days",
      maturity: "35–45 days",
      harvestType: "Single cut or continuous outer leaf priming (cut-and-come-again)"
    },
    {
      category: "Fruiting Solanaceous (Tomato, Eggplant, Pepper)",
      germination: "6–12 days",
      transplant: "25–35 days",
      firstHarvest: "55–75 days after transplant",
      maturity: "75–110 days",
      harvestType: "Continuous repeated picking every 4–5 days for 3–6 months"
    },
    {
      category: "Cucurbits / Gourds (Ampalaya, Squash, Cucumber)",
      germination: "4–8 days",
      transplant: "12–18 days or direct",
      firstHarvest: "45–65 days",
      maturity: "70–95 days",
      harvestType: "Frequent picking every 2–3 days to prevent fruit hardening"
    },
    {
      category: "Legumes (Sitaw / Yardlong Bean)",
      germination: "3–5 days",
      transplant: "Direct seeded only",
      firstHarvest: "45–55 days",
      maturity: "55–65 days",
      harvestType: "Continuous picking every 2 days for 6–8 weeks"
    },
    {
      category: "Root Crops (Carrots, Labanos / Radish)",
      germination: "4–12 days",
      transplant: "Direct seeded only",
      firstHarvest: "35–85 days",
      maturity: "40–90 days",
      harvestType: "Single harvest when root shoulder reaches marketable diameter"
    }
  ];

  return (
    <div className="catalog-container animate-fade-in">
      {/* Intro Header */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
          <Clock size={24} color="var(--emerald-400)" />
          <h2 style={{ fontSize: '1.45rem', color: '#ffffff' }}>Vegetable Growth Stages & Timeline Guide</h2>
        </div>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem', maxWidth: '850px' }}>
          Understanding the distinct differences between <strong>Days to Germination</strong>, <strong>Seedling Transplanting</strong>, 
          <strong> Days to First Harvest</strong>, and <strong>Days to Maturity</strong> is essential for proper crop scheduling and harvest planning.
        </p>
      </div>

      {/* Crucial Concept Clarification Box */}
      <div className="glass-panel" style={{ padding: '24px', borderLeft: '4px solid var(--emerald-400)' }}>
        <h3 style={{ fontSize: '1.15rem', color: '#ffffff', marginBottom: '12px' }}>
          Clarifying Botanical Definitions
        </h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px' }}>
          <div style={{ background: 'rgba(7, 19, 14, 0.5)', padding: '14px', borderRadius: 'var(--radius-md)' }}>
            <strong style={{ color: 'var(--emerald-300)' }}>Days to First Harvest:</strong>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '4px' }}>
              The number of calendar days from seed sowing (or transplanting) until the grower can make the first edible picking. Always clarify whether counted from seed or transplant.
            </p>
          </div>

          <div style={{ background: 'rgba(7, 19, 14, 0.5)', padding: '14px', borderRadius: 'var(--radius-md)' }}>
            <strong style={{ color: 'var(--amber-400)' }}>Days to Maturity:</strong>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '4px' }}>
              The time required for a vegetable variety to reach its full size, color, seed viability, or peak culinary flavor. Influenced heavily by day length, temperature, and soil nutrition.
            </p>
          </div>

          <div style={{ background: 'rgba(7, 19, 14, 0.5)', padding: '14px', borderRadius: 'var(--radius-md)' }}>
            <strong style={{ color: '#38bdf8' }}>Overall Harvesting Window:</strong>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '4px' }}>
              The duration over which a plant produces harvestable yields. Determinant crops yield all at once, whereas indeterminate crops yield over 2 to 5 months.
            </p>
          </div>
        </div>
      </div>

      {/* 5-Stage Visual Progression */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <h3 style={{ fontSize: '1.2rem', color: '#ffffff', marginBottom: '16px' }}>
          The 5 Sequential Growing Milestones
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
          {STAGES.map(s => (
            <div key={s.num} className="timeline-step">
              <div className="timeline-step-num" style={{ background: 'var(--emerald-800)' }}>
                {s.num}
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', flex: 1 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap' }}>
                  <strong style={{ fontSize: '1.05rem', color: '#ffffff' }}>
                    {s.icon} {s.title}
                  </strong>
                  <span className="badge badge-emerald">{s.duration}</span>
                </div>
                <p style={{ fontSize: '0.88rem', color: 'var(--text-secondary)' }}>{s.desc}</p>
                <div style={{ fontSize: '0.82rem', color: 'var(--emerald-300)', marginTop: '2px' }}>
                  <strong>Key Grower Action:</strong> {s.action}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Crop Category Comparison Table */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <h3 style={{ fontSize: '1.2rem', color: '#ffffff', marginBottom: '14px' }}>
          Crop Category Comparison Table
        </h3>
        <div style={{ overflowX: 'auto' }}>
          <table>
            <thead>
              <tr>
                <th>Vegetable Category</th>
                <th>Germination</th>
                <th>Transplanting</th>
                <th>Days to First Harvest</th>
                <th>Days to Maturity</th>
                <th>Harvest Pattern</th>
              </tr>
            </thead>
            <tbody>
              {CROPS_COMPARISON.map((c, idx) => (
                <tr key={idx}>
                  <td style={{ fontWeight: 600, color: '#ffffff' }}>{c.category}</td>
                  <td>{c.germination}</td>
                  <td>{c.transplant}</td>
                  <td style={{ color: 'var(--emerald-300)', fontWeight: 600 }}>{c.firstHarvest}</td>
                  <td style={{ color: 'var(--amber-400)', fontWeight: 600 }}>{c.maturity}</td>
                  <td style={{ fontSize: '0.82rem' }}>{c.harvestType}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
          <button 
            className="btn btn-primary"
            onClick={() => onAskInChat('What are the exact days to harvest and maturity periods for common Philippine vegetables (Pechay, Ampalaya, Sitaw, Talong)?')}
          >
            <MessageSquare size={16} />
            <span>Ask Floramind for Specific Crop Schedules</span>
          </button>
        </div>
      </div>
    </div>
  );
}
