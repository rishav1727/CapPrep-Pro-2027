import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css_rules = """
/* Prominent Lock & Free Badges requested by user */
.test-lock-pill {
  background: #dc2626 !important;
  color: #ffffff !important;
  font-size: 0.65rem !important;
  font-weight: 800 !important;
  padding: 0.2rem 0.5rem !important;
  border-radius: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.25rem !important;
  letter-spacing: 0.5px !important;
  box-shadow: 0 0 8px rgba(220, 38, 38, 0.4) !important;
  text-transform: uppercase !important;
  margin-left: auto !important;
}

.test-free-pill {
  background: #059669 !important;
  color: #ffffff !important;
  font-size: 0.65rem !important;
  font-weight: 800 !important;
  padding: 0.2rem 0.55rem !important;
  border-radius: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.25rem !important;
  letter-spacing: 0.5px !important;
  text-transform: uppercase !important;
  box-shadow: 0 0 8px rgba(5, 150, 105, 0.4) !important;
  margin-left: auto !important;
}

.test-pill-btn.locked {
  border-color: rgba(239, 68, 68, 0.35) !important;
  background: rgba(239, 68, 68, 0.04) !important;
}
.test-pill-btn.locked:hover {
  border-color: #ef4444 !important;
  background: rgba(239, 68, 68, 0.1) !important;
}

.test-card.locked {
  border-color: rgba(239, 68, 68, 0.35) !important;
  background: rgba(20, 24, 39, 0.95) !important;
  position: relative;
}
.test-card.locked:hover {
  border-color: #ef4444 !important;
}

/* Grand Mock Live Drive Choice Banner */
.gm-choice-banner {
  background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.gm-choice-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.gm-live-badge {
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.4);
  font-size: 0.75rem;
  font-weight: 800;
  padding: 0.25rem 0.65rem;
  border-radius: 20px;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  animation: pulse 2s infinite;
}
.gm-toggle-container {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.gm-toggle-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #cbd5e1;
  padding: 0.6rem 1.15rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}
.gm-toggle-btn:hover {
  border-color: var(--accent);
  color: #fff;
}
.gm-toggle-btn.active {
  background: linear-gradient(135deg, #00d4ff, #7c3aed);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 4px 15px rgba(0, 212, 255, 0.25);
}
"""

if '.test-lock-pill' not in css:
    css += "\n" + new_css_rules
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated css/style.css with prominent lock pills and choice banner styles")
else:
    print("css/style.css already has test-lock-pill")
