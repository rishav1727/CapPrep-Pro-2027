# -*- coding: utf-8 -*-
"""
Update C:\cap\ai\index.html:
1. Add missing #quiz-container (so clicking on tests opens the full-screen proctored assessment).
2. Add #locked-test-modal (so clicking any of the 75 locked tests shows a popup to get Pro or Sign In).
3. Add #signin-modal (so existing buyers can sign in with their Email + Password to unlock everything).
4. Update #payment-modal with Password creation field and rishavofficials1727@oksbi UPI details.
5. Add Sign In button to navbar.
"""

path = r"C:\cap\ai\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Navbar to include Sign In button & Auth profile
old_nav_btn = '<li><button id="nav-pro-btn" class="nav-pro-badge" onclick="openPaymentModal()">⚡ Upgrade to Pro (₹51)</button></li>'
new_nav_btn = '''<li><button id="nav-signin-btn" class="nav-signin-btn" onclick="handleNavAuthClick()" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#fff; padding:0.4rem 0.85rem; border-radius:6px; font-size:0.8rem; font-weight:600; cursor:pointer; margin-right:0.35rem;">🔑 Sign In</button></li>
    <li><button id="nav-pro-btn" class="nav-pro-badge" onclick="handleNavProClick()">⚡ Upgrade to Pro (₹51)</button></li>'''

if old_nav_btn in html:
    html = html.replace(old_nav_btn, new_nav_btn)
    print("Updated navbar buttons")

# 2. Update UPI ID in payment modal
html = html.replace('rishavofficials1727@okhdfcbank', 'rishavofficials1727@oksbi')

# 3. Add Password field into payment modal enrollment form
old_cust_grid = '''      <div class="customer-input-grid">
        <input type="tel" id="cust-phone-input" class="customer-input" placeholder="WhatsApp Number (+91)" required />
        <input type="text" id="cust-college-input" class="customer-input" placeholder="College / Batch (e.g. VIT 2027)" />
      </div>'''

new_cust_grid = '''      <div class="customer-input-grid">
        <input type="tel" id="cust-phone-input" class="customer-input" placeholder="WhatsApp Number (+91)" required />
        <input type="text" id="cust-college-input" class="customer-input" placeholder="College / Batch (e.g. VIT 2027)" />
      </div>
      <div style="margin-bottom:0.75rem;">
        <input type="password" id="cust-password-input" class="customer-input" placeholder="Create Account Password (min 6 characters for future sign-in)" required />
        <div style="font-size:0.72rem; color:#94a3b8; margin-top:0.25rem;">🔒 You will use this password to sign back in anytime from any device.</div>
      </div>'''

if old_cust_grid in html:
    html = html.replace(old_cust_grid, new_cust_grid)
    print("Added password field to payment modal")

# 4. Add #quiz-container, #locked-test-modal, and #signin-modal before <script src="js/app.js"></script>
extra_modals = '''
<!-- ===== FULL-SCREEN PROCTORED MOCK TEST ASSESSMENT RUNNER ===== -->
<div id="quiz-container" style="display:none;">
  <div class="quiz-header">
    <div>
      <div id="quiz-title" class="quiz-title">Diagnostic Verbal Assessment</div>
      <div style="font-size:0.75rem; color:var(--text-muted);">Proctored Mode • Capgemini Exceller Standard</div>
    </div>
    <div style="display:flex; align-items:center; gap:0.75rem;">
      <div id="quiz-timer" class="quiz-timer">⏱ 15:00</div>
      <button class="tool-btn" onclick="closeQuiz()" style="background:rgba(239,68,68,0.15); border-color:#ef4444; color:#fca5a5; cursor:pointer;">✕ Exit Test</button>
    </div>
  </div>

  <div class="quiz-progress-bar">
    <div id="quiz-progress-fill" class="quiz-progress-fill" style="width:0%;"></div>
  </div>

  <!-- Question Card -->
  <div id="question-card" class="question-card">
    <div id="q-num" class="question-num">Question 1 of 10</div>
    <div id="q-text" class="question-text">Loading question...</div>
    <div id="q-code"></div>

    <div id="options-grid" class="options-grid"></div>

    <div id="explanation-box" class="explanation-box" style="display:none;"></div>

    <div class="quiz-actions">
      <button class="btn btn-outline" onclick="closeQuiz()">✕ Quit Test</button>
      <button id="btn-next" class="btn btn-primary" onclick="nextQuestion()">Next →</button>
    </div>
  </div>

  <!-- Result Card -->
  <div id="quiz-result" class="quiz-result" style="display:none;"></div>
</div>

<!-- ===== LOCKED TEST POP-UP MODAL ===== -->
<div id="locked-test-modal" class="pay-modal-overlay" style="display:none;">
  <div class="pay-modal" style="max-width:520px; text-align:center;">
    <button class="pay-close-btn" onclick="closeLockedTestModal()">✕</button>
    <div style="font-size:2.8rem; margin-bottom:0.5rem;">🔒</div>
    <div style="display:inline-block; background:rgba(245,158,11,0.15); border:1px solid #f59e0b; color:#fbbf24; font-size:0.75rem; font-weight:800; padding:0.25rem 0.65rem; border-radius:20px; margin-bottom:0.75rem;">
      CAPPREP PRO ASSESSMENT
    </div>
    <h2 style="font-size:1.35rem; color:#fff; margin-bottom:0.35rem;" id="locked-modal-test-title">
      This Assessment is Locked
    </h2>
    <p style="font-size:0.82rem; color:#cbd5e1; margin-bottom:0.75rem;" id="locked-modal-test-meta">
      Only Test 1 (Diagnostic Verbal Assessment) is available for free demo.
    </p>

    <div style="background:rgba(0,212,255,0.06); border:1px solid rgba(0,212,255,0.25); border-radius:10px; padding:1rem; margin:1rem 0; text-align:left;">
      <div style="font-size:0.85rem; font-weight:700; color:#fff; margin-bottom:0.35rem;">Unlock Complete Exceller 2027 Suite for ₹51:</div>
      <ul style="font-size:0.78rem; color:#cbd5e1; line-height:1.6; padding-left:1.2rem; margin:0;">
        <li>All 75+ Stage-wise Tests & 10 Grand Marathon Mocks</li>
        <li>Stage 2B Debugging Simulator & Stage 3 Lab 27 AI Simulator</li>
        <li>In-Browser Protected PDF Study Manuals across all 6 Stages</li>
      </ul>
    </div>

    <div style="display:flex; flex-direction:column; gap:0.65rem; margin-top:1.25rem;">
      <button class="pay-btn-checkout" onclick="closeLockedTestModal(); openPaymentModal();">
        ⚡ Unlock Pro Pass for ₹51 (Flash 83% OFF)
      </button>
      <div style="display:flex; gap:0.5rem;">
        <button class="btn btn-outline" style="flex:1; justify-content:center; font-size:0.82rem;" onclick="closeLockedTestModal(); openSignInModal();">
          🔑 Already Purchased? Sign In
        </button>
        <button class="btn btn-outline" style="flex:1; justify-content:center; font-size:0.82rem; color:#06d6a0; border-color:rgba(6,214,160,0.3);" onclick="closeLockedTestModal(); startTest('vb_1');">
          🎯 Try Free Test 1
        </button>
      </div>
    </div>
  </div>
</div>

<!-- ===== USER SIGN IN MODAL ===== -->
<div id="signin-modal" class="pay-modal-overlay" style="display:none;">
  <div class="pay-modal" style="max-width:440px;">
    <button class="pay-close-btn" onclick="closeSignInModal()">✕</button>
    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
      <div style="font-size:1.6rem;">🔑</div>
      <div>
        <h2 style="font-size:1.25rem; color:#fff; margin:0;">Student Sign In</h2>
        <div style="font-size:0.75rem; color:var(--text-muted);">Access your unlocked CapPrep Pro account</div>
      </div>
    </div>

    <div style="margin:1rem 0;">
      <div style="margin-bottom:0.75rem;">
        <label style="font-size:0.78rem; font-weight:600; color:#cbd5e1; display:block; margin-bottom:0.3rem;">Email Address</label>
        <input type="email" id="signin-email-input" class="customer-input" placeholder="e.g. rahul@gmail.com" onkeydown="if(event.key==='Enter') processUserSignIn()" />
      </div>

      <div style="margin-bottom:0.75rem;">
        <label style="font-size:0.78rem; font-weight:600; color:#cbd5e1; display:block; margin-bottom:0.3rem;">Password</label>
        <input type="password" id="signin-password-input" class="customer-input" placeholder="Enter your account password" onkeydown="if(event.key==='Enter') processUserSignIn()" />
      </div>

      <div id="signin-error-msg" style="display:none; color:#f87171; font-size:0.78rem; margin-bottom:0.75rem; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); padding:0.5rem; border-radius:6px;"></div>

      <button class="pay-btn-checkout" onclick="processUserSignIn()">
        🔓 Sign In & Unlock My Tests
      </button>

      <div style="text-align:center; margin-top:1rem; font-size:0.8rem; color:var(--text-muted);">
        Don't have a Pro account yet? 
        <a href="javascript:void(0)" onclick="closeSignInModal(); openPaymentModal();" style="color:var(--accent); font-weight:700; text-decoration:none;">
          Enroll now for ₹51 →
        </a>
      </div>
    </div>
  </div>
</div>
'''

if extra_modals.strip() not in html:
    html = html.replace('<script src="js/app.js"></script>', extra_modals + '\n<script src="js/app.js"></script>')
    print("Injected quiz-container, locked-test-modal, and signin-modal")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html")
