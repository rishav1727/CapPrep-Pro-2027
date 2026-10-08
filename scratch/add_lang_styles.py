# -*- coding: utf-8 -*-
"""
Add styles for .lang-selector-bar in css/style.css
"""

path = r"C:\cap\ai\css\style.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

lang_styles = """
/* Language Selector for Coding & Pseudocode Questions */
.lang-selector-bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0.85rem 0 0.5rem;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(0, 212, 255, 0.2);
  border-radius: 8px;
  padding: 0.4rem 0.75rem;
  flex-wrap: wrap;
}
.lang-label {
  font-size: 0.76rem;
  font-weight: 700;
  color: #94a3b8;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}
.lang-pill {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #cbd5e1;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}
.lang-pill:hover {
  background: rgba(0, 212, 255, 0.15);
  border-color: var(--accent);
  color: #fff;
}
.lang-pill.active {
  background: linear-gradient(135deg, #00d4ff, #7c3aed);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 2px 8px rgba(0, 212, 255, 0.35);
}
.lang-badge {
  margin-left: auto;
  font-size: 0.7rem;
  color: #06d6a0;
  font-weight: 600;
}
"""

if ".lang-selector-bar" not in css:
    css += lang_styles
    with open(path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Added .lang-selector-bar styles to css/style.css")
else:
    print("Styles already present")
