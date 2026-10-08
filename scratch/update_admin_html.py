# -*- coding: utf-8 -*-
"""
Update C:\cap\ai\admin.html with comprehensive VIP Candidate Free Subscription management.
Allows Rishav to:
1. Self-unlock Pro on current device with 1 click.
2. Grant 100% free lifetime VIP pass to ANY candidate ID, roll number, or email.
3. Generate 1-click shareable WhatsApp / email access links.
4. Manage whitelisted VIP candidates with active status and revoke authority.
5. Create custom 100% free promo codes.
"""

path = r"C:\cap\ai\admin.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the alert banner buttons
old_alert_btns = '''    <div style="display:flex; gap:0.5rem;">
      <button class="btn-action" onclick="triggerTestNotification()">🔔 Test Notification to My Email</button>
      <button class="btn-action btn-primary-action" onclick="openGrantModal()">➕ Grant Access Manually</button>
    </div>'''

new_alert_btns = '''    <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
      <button class="btn-action" style="background:#059669; border-color:#10b981; color:#fff; font-weight:700;" onclick="selfUnlockPro()">⭐ Self-Unlock My Browser (Free Pro)</button>
      <button class="btn-action" onclick="triggerTestNotification()">🔔 Test Notification to My Email</button>
      <button class="btn-action btn-primary-action" onclick="openVipModal()">👑 Grant Free VIP to Any ID</button>
    </div>'''

if old_alert_btns in content:
    content = content.replace(old_alert_btns, new_alert_btns)
else:
    print("Warning: old_alert_btns not found directly, checking variations...")

# 2. Update navigation tabs to include VIP Pass Controller
old_tabs = '''  <div class="admin-tabs">
    <button class="tab-item active" onclick="switchTab('orders-panel')">📋 Paid Student Orders (<span id="tab-orders-count">0</span>)</button>
    <button class="tab-item" onclick="switchTab('notifs-panel')">🔔 Live Notifications Log (<span id="tab-notifs-count">0</span>)</button>
    <button class="tab-item" onclick="switchTab('pricing-panel')">💰 Pricing & Coupon Engine</button>
    <button class="tab-item" onclick="switchTab('gateway-panel')">💳 Payment Partner & UPI Setup</button>
    <button class="tab-item" onclick="switchTab('security-panel')">🛡️ Authority & Security Settings</button>
  </div>'''

new_tabs = '''  <div class="admin-tabs">
    <button class="tab-item active" onclick="switchTab('orders-panel')">📋 Paid Student Orders (<span id="tab-orders-count">0</span>)</button>
    <button class="tab-item" onclick="switchTab('vip-panel')">👑 Free VIP Pass Controller (<span id="tab-vip-count">0</span>)</button>
    <button class="tab-item" onclick="switchTab('notifs-panel')">🔔 Live Notifications Log (<span id="tab-notifs-count">0</span>)</button>
    <button class="tab-item" onclick="switchTab('pricing-panel')">💰 Pricing & Coupon Engine</button>
    <button class="tab-item" onclick="switchTab('gateway-panel')">💳 Payment Partner & UPI Setup</button>
    <button class="tab-item" onclick="switchTab('security-panel')">🛡️ Authority & Security Settings</button>
  </div>'''

if old_tabs in content:
    content = content.replace(old_tabs, new_tabs)
else:
    print("Warning: old_tabs not found directly")

# 3. Add VIP panel HTML before security-panel
vip_panel_html = '''  <!-- PANEL: VIP CANDIDATE FREE PASS CONTROLLER -->
  <div id="vip-panel" class="admin-panel">
    <div class="panel-card" style="border-color:rgba(124,58,237,0.35); background:linear-gradient(180deg, rgba(124,58,237,0.06), rgba(11,15,25,0.95));">
      <div class="panel-header">
        <div class="panel-title" style="color:#c084fc;">
          <span>👑</span> Grant 100% Free Lifetime VIP Subscription to Any Candidate ID or Email
        </div>
        <div class="panel-actions">
          <button class="btn-action" style="background:#059669; color:#fff;" onclick="selfUnlockPro()">⭐ Self-Unlock My Browser</button>
        </div>
      </div>

      <p style="font-size:0.85rem; color:#cbd5e1; margin-bottom:1.25rem; line-height:1.6;">
        As Master Admin, you have full authority to grant <strong>100% Free Lifetime VIP Access (₹0)</strong> to any student, friend, college representative, or candidate ID.
        When granted, the candidate gets instant access to all 76+ Mock Tests, Lab 27 AI Simulator, and Study Notes without paying anything.
      </p>

      <div style="background:#0b0f19; border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:1.25rem; margin-bottom:1.75rem;">
        <h4 style="color:#fff; font-size:0.95rem; margin-bottom:0.75rem;">⚡ Quick Grant Form: Issue Free Subscription</h4>
        <div class="form-grid">
          <div class="form-group">
            <label>Candidate Name</label>
            <input type="text" id="vip-grant-name" class="form-control" placeholder="e.g. Sneha Sharma" />
          </div>
          <div class="form-group">
            <label>Candidate ID / Roll Number / Email <span style="color:#f87171">*</span></label>
            <input type="text" id="vip-grant-id" class="form-control" placeholder="e.g. 2024CS014 or sneha@gmail.com" />
            <div class="form-help">Enter candidate's email, student ID, or college roll number.</div>
          </div>
          <div class="form-group">
            <label>WhatsApp / Phone Number</label>
            <input type="tel" id="vip-grant-phone" class="form-control" placeholder="+91 98765 43210" />
          </div>
          <div class="form-group">
            <label>Grant Reason / Tag</label>
            <input type="text" id="vip-grant-reason" class="form-control" placeholder="e.g. Campus Ambassador / Free Grant" />
          </div>
        </div>

        <div style="display:flex; gap:0.75rem; margin-top:1.25rem; flex-wrap:wrap;">
          <button class="btn-action btn-primary-action" onclick="executeVipGrant()">⚡ Grant 100% Free VIP Lifetime Pass</button>
          <button class="btn-action" onclick="generateShareableVipLink()">🔗 Generate 1-Click WhatsApp Share Link</button>
        </div>

        <div id="vip-link-output" style="display:none; margin-top:1rem; background:rgba(0,212,255,0.08); border:1px solid var(--accent); border-radius:8px; padding:0.75rem 1rem;">
          <div style="font-size:0.78rem; color:#94a3b8; margin-bottom:0.35rem;">Copy & send this 1-click free activation link to candidate on WhatsApp / Email:</div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <input type="text" id="vip-generated-url" class="search-input" style="flex:1; font-family:'JetBrains Mono'; font-size:0.8rem;" readonly />
            <button class="btn-action" onclick="copyVipGeneratedLink()">📋 Copy Link</button>
          </div>
        </div>
      </div>

      <!-- Whitelisted Free VIP Candidates Table -->
      <h3 style="font-size:1.05rem; color:#fff; margin-bottom:0.75rem;">📋 Currently Active Whitelisted Free VIP Candidates</h3>
      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>VIP Pass Ref</th>
              <th>Candidate Name</th>
              <th>Candidate ID / Email</th>
              <th>WhatsApp / Phone</th>
              <th>Tag / Reason</th>
              <th>Granted Date</th>
              <th>Status</th>
              <th>Authority Actions</th>
            </tr>
          </thead>
          <tbody id="vip-whitelist-table-body">
            <!-- Dynamic VIP rows rendered via JS -->
          </tbody>
        </table>
      </div>

      <hr style="border:0; border-top:1px solid var(--card-border); margin:2rem 0;">

      <!-- Custom 100% Free Promo Code Generator -->
      <div class="panel-title" style="margin-bottom:0.75rem; font-size:1rem;">
        <span>🎟️</span> Create Custom 100% Free Promo / Voucher Codes
      </div>
      <p style="font-size:0.82rem; color:var(--text-muted); margin-bottom:1rem;">
        Generate voucher codes that students can enter in the checkout modal to reduce the price to ₹0 and get instant access.
      </p>

      <div style="display:flex; gap:0.75rem; align-items:center; flex-wrap:wrap; margin-bottom:1.25rem;">
        <input type="text" id="new-free-coupon-code" class="search-input" placeholder="e.g. RISHAV100, FREEVIP, BATCH2027" style="text-transform:uppercase; font-weight:700;" />
        <button class="btn-action btn-primary-action" onclick="createCustomFreeCoupon()">➕ Create 100% Free Coupon</button>
      </div>

      <div id="custom-coupons-list" style="display:flex; gap:0.5rem; flex-wrap:wrap;">
        <!-- Dynamic badge pills -->
      </div>
    </div>
  </div>
'''

if '<!-- PANEL 4: PAYMENT PARTNER & UPI (INDIA) -->' in content:
    content = content.replace('<!-- PANEL 4: PAYMENT PARTNER & UPI (INDIA) -->', vip_panel_html + '\n  <!-- PANEL 4: PAYMENT PARTNER & UPI (INDIA) -->')
else:
    print("Warning: anchor for vip_panel_html not found")

# Write out the updated file
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated HTML markup in {path}")
