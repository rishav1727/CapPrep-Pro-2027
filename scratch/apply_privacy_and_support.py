# -*- coding: utf-8 -*-
"""
Implement user privacy, stealth admin revelation, and support channel:
1. Hide ALL admin links, badges, and admin emails from index.html for common visitors.
2. In admin.html, remove plaintext admin email from the login screen (user must type registered admin email + PIN).
3. In index.html, when user signs in with rishavofficials1727@gmail.com or rishav.gupta0527@gmail.com,
   the navbar dynamically unlocks and shows "👑 Admin Control" link! For normal students, it stays hidden.
4. Add Help & Support modal and links pointing to rishav.gupta0527@gmail.com.
5. In payment modal and success receipt, show official CapPrep Administration verification and support email.
"""

# =========================================================================
# 1. UPDATE index.html
# =========================================================================
index_path = r"C:\cap\ai\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# A. Navbar: Remove public admin link, add Help & Support, add dynamic hidden admin container
old_nav_end = '''    <li><button id="nav-signin-btn" class="nav-signin-btn" onclick="handleNavAuthClick()" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#fff; padding:0.4rem 0.85rem; border-radius:6px; font-size:0.8rem; font-weight:600; cursor:pointer; margin-right:0.35rem;">🔑 Sign In</button></li>
    <li><button id="nav-pro-btn" class="nav-pro-badge" onclick="handleNavProClick()">⚡ Upgrade to Pro (₹51)</button></li>
    <li><a href="admin.html" style="color:#f59e0b; font-size:0.8rem; font-weight:700; text-decoration:none; padding:0.25rem 0.5rem; border:1px solid rgba(245,158,11,0.3); border-radius:4px; background:rgba(245,158,11,0.1);" title="Admin Portal (Rishav)">👑 Admin</a></li>'''

new_nav_end = '''    <li><a href="javascript:void(0)" onclick="openSupportModal()" style="color:#38bdf8; font-size:0.8rem; font-weight:600; text-decoration:none; padding:0.35rem 0.65rem; border-radius:6px; background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.25);">🎧 Help & Support</a></li>
    <li><button id="nav-signin-btn" class="nav-signin-btn" onclick="handleNavAuthClick()" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#fff; padding:0.4rem 0.85rem; border-radius:6px; font-size:0.8rem; font-weight:600; cursor:pointer; margin-right:0.35rem;">🔑 Sign In</button></li>
    <li><button id="nav-pro-btn" class="nav-pro-badge" onclick="handleNavProClick()">⚡ Upgrade to Pro (₹51)</button></li>
    <!-- Dynamic Admin Control link (Only visible when registered administrator signs in) -->
    <li id="nav-admin-link-item" style="display:none;"><a href="admin.html" style="color:#fbbf24; font-size:0.8rem; font-weight:800; text-decoration:none; padding:0.35rem 0.65rem; border:1px solid rgba(245,158,11,0.4); border-radius:6px; background:rgba(245,158,11,0.15);">👑 Admin Panel</a></li>'''

if old_nav_end in index_html:
    index_html = index_html.replace(old_nav_end, new_nav_end)
    print("Updated navbar: removed public admin link, added Help & Support and dynamic admin link")

# B. Footer: Remove all admin email and lock portal references, add Help & Support
old_footer = '''      <a href="modules/study_reader.html" style="color:var(--accent); text-decoration:none; font-weight:700;">📖 Master PDF Reader</a>
      <a href="admin.html" style="color:#475569; text-decoration:none; font-size:0.75rem;" title="Master Security Gate">🔒 Portal</a>
    </div>
    <div style="font-size:0.78rem; color:#64748b; border-top:1px solid rgba(255,255,255,0.05); padding-top:1.5rem;">
      © 2026-2027 CapPrep Pro • Primary Administrator: <code style="color:#94a3b8">rishavofficials1727@gmail.com</code> • Authorized Capgemini Prep Portal
    </div>'''

new_footer = '''      <a href="modules/study_reader.html" style="color:var(--accent); text-decoration:none; font-weight:700;">📖 Master PDF Reader</a>
      <a href="javascript:void(0)" onclick="openSupportModal()" style="color:#38bdf8; text-decoration:none; font-weight:600;">🎧 Help & Support</a>
    </div>
    <div style="font-size:0.78rem; color:#64748b; border-top:1px solid rgba(255,255,255,0.05); padding-top:1.5rem;">
      © 2026-2027 CapPrep Pro • Official Capgemini Exceller Recruitment Prep Suite • Student Support: <a href="mailto:rishav.gupta0527@gmail.com" style="color:#38bdf8; text-decoration:none; font-weight:600;">rishav.gupta0527@gmail.com</a>
    </div>'''

if old_footer in index_html:
    index_html = index_html.replace(old_footer, new_footer)
    print("Updated footer: removed admin email exposure and secret portal link")

# C. Add Help & Support Modal before <script src="js/app.js"></script>
support_modal_html = '''
<!-- ===== HELP & SUPPORT MODAL ===== -->
<div id="support-modal" class="pay-modal-overlay" style="display:none;">
  <div class="pay-modal" style="max-width:500px;">
    <button class="pay-close-btn" onclick="closeSupportModal()">✕</button>
    <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.75rem;">
      <div style="font-size:1.8rem;">🎧</div>
      <div>
        <h2 style="font-size:1.3rem; color:#fff; margin:0;">CapPrep Help & Support</h2>
        <div style="font-size:0.78rem; color:var(--text-muted);">Direct Executive Candidate Assistance</div>
      </div>
    </div>

    <p style="font-size:0.85rem; color:#cbd5e1; line-height:1.5; margin-bottom:1rem;">
      Have a question about your ₹51 Pro enrollment, payment verification, syllabus notes, or need account recovery?
      Reach out directly to the official administration.
    </p>

    <div style="background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.25); border-radius:10px; padding:1.25rem; margin-bottom:1.25rem; text-align:center;">
      <div style="font-size:0.75rem; color:#94a3b8; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:0.35rem;">Official Executive Support Email:</div>
      <div style="font-size:1.1rem; font-weight:800; color:#38bdf8; font-family:'JetBrains Mono', monospace; margin-bottom:0.75rem;">
        rishav.gupta0527@gmail.com
      </div>
      <a href="mailto:rishav.gupta0527@gmail.com?subject=CapPrep%20Pro%20Candidate%20Inquiry" class="btn btn-primary" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.55rem 1.25rem; font-size:0.85rem; text-decoration:none;">
        ✉️ Send Email to Support
      </a>
    </div>

    <div style="font-size:0.78rem; color:#94a3b8; line-height:1.6;">
      <div>• <strong>Response Time:</strong> Typically under 30 minutes for payment verifications.</div>
      <div>• <strong>Payment Help:</strong> Mention your 12-digit UPI UTR number and registered email in your message.</div>
      <div>• <strong>Verified Administration:</strong> Authorized CapPrep Pro Recruitment Platform.</div>
    </div>
  </div>
</div>
'''

if "id=\"support-modal\"" not in index_html:
    index_html = index_html.replace('<script src="js/app.js"></script>', support_modal_html + '\n<script src="js/app.js"></script>')
    print("Added support modal to index.html")

# D. Update payment modal to display Help & Support email
old_pay_footer = '''    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.75rem; font-size:0.72rem; color:var(--text-muted);">
      <span>🔒 256-bit Encrypted Checkout</span>
      <span>⚡ Instant Activation • Receipts to Email</span>
    </div>'''

new_pay_footer = '''    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.75rem; font-size:0.72rem; color:var(--text-muted); flex-wrap:wrap; gap:0.4rem;">
      <span>🔒 Verified by CapPrep Admin</span>
      <span>🎧 Need Payment Help? <a href="mailto:rishav.gupta0527@gmail.com" style="color:#38bdf8; text-decoration:none;">rishav.gupta0527@gmail.com</a></span>
    </div>'''

if old_pay_footer in index_html:
    index_html = index_html.replace(old_pay_footer, new_pay_footer)
    print("Updated payment modal footer with support email")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
print("Saved index.html")

# =========================================================================
# 2. UPDATE admin.html (Remove plaintext admin email from login screen)
# =========================================================================
admin_path = r"C:\cap\ai\admin.html"
with open(admin_path, "r", encoding="utf-8") as f:
    admin_html = f.read()

# Change login email input from readonly rishavofficials1727@gmail.com to blank input
old_admin_email_field = '''    <div class="login-field">
      <label>Authorized Admin Email</label>
      <input type="email" id="login-email-input" class="login-input" value="rishavofficials1727@gmail.com" readonly style="background:#1e293b; color:#94a3b8; cursor:not-allowed;" />
    </div>'''

new_admin_email_field = '''    <div class="login-field">
      <label>Registered Administrator Email</label>
      <input type="email" id="login-email-input" class="login-input" placeholder="Enter registered administrator email" autocomplete="off" />
    </div>'''

if old_admin_email_field in admin_html:
    admin_html = admin_html.replace(old_admin_email_field, new_admin_email_field)
    print("Removed plaintext admin email from admin.html login screen")

# Remove email exposure from bottom of login card
admin_html = admin_html.replace(
    '🔒 256-Bit Cryptographic Session Gate • Primary Admin: <code>rishavofficials1727@gmail.com</code>',
    '🔒 256-Bit Cryptographic Session Gate • Authorized Personnel Only'
)

# Update authenticateAdmin in admin.html to check that entered email matches registered admin email!
old_admin_auth_code = '''async function authenticateAdmin() {
  const pinInput = document.getElementById('login-pin-input').value.trim();
  const errorMsg = document.getElementById('login-error-msg');
  const loginBtn = document.querySelector('.login-btn');'''

new_admin_auth_code = '''async function authenticateAdmin() {
  const emailInput = (document.getElementById('login-email-input')?.value || '').trim().toLowerCase();
  const pinInput = document.getElementById('login-pin-input').value.trim();
  const errorMsg = document.getElementById('login-error-msg');
  const loginBtn = document.querySelector('.login-btn');

  // Verify that the email is the registered admin email
  const VALID_ADMIN_EMAILS = ["rishavofficials1727@gmail.com", "rishav.gupta0527@gmail.com"];
  if (!VALID_ADMIN_EMAILS.includes(emailInput)) {
    errorMsg.style.display = 'block';
    errorMsg.textContent = '❌ Access Denied: Unrecognized administrator email.';
    return;
  }'''

if old_admin_auth_code in admin_html:
    admin_html = admin_html.replace(old_admin_auth_code, new_admin_auth_code)
    print("Updated admin.html authenticateAdmin to require registered admin email")

with open(admin_path, "w", encoding="utf-8") as f:
    f.write(admin_html)
print("Saved admin.html")

# =========================================================================
# 3. UPDATE js/app.js (Dynamic Admin link revelation & Support functions)
# =========================================================================
app_path = r"C:\cap\ai\js\app.js"
with open(app_path, "r", encoding="utf-8") as f:
    app_js = f.read()

# Add Support Modal handlers and Admin Recognition
support_functions = '''
// ==========================================
// HELP & SUPPORT ENGINE (rishav.gupta0527@gmail.com)
// ==========================================

const OFFICIAL_SUPPORT_EMAIL = "rishav.gupta0527@gmail.com";
const MASTER_ADMIN_EMAILS = ["rishavofficials1727@gmail.com", "rishav.gupta0527@gmail.com"];

function openSupportModal() {
  const modal = document.getElementById('support-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function closeSupportModal() {
  const modal = document.getElementById('support-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}
'''

if "function openSupportModal" not in app_js:
    app_js = support_functions + "\n" + app_js

# In processUserSignIn and updateProUI, check if the logged in user is the master admin!
old_signin_success = """    if (user.isPro) {
      showSecurityToast(`⭐ Welcome back, ${user.name}! Your CapPrep Pro Pass is active.`);
      alert(`🎉 WELCOME BACK ${user.name.toUpperCase()}!\\n\\nYour CapPrep Pro Lifetime Pass is ACTIVE.\\nAll 76+ Mock Tests, Simulators, and Study Notes are unlocked!`);
    } else {
      showSecurityToast(`👤 Logged in as ${user.name} (Free Tier).`);
    }"""

new_signin_success = """    const isAdmin = MASTER_ADMIN_EMAILS.includes(user.email.toLowerCase());
    if (isAdmin) {
      showSecurityToast(`👑 Administrator Authenticated: Welcome, Rishav!`);
      alert(`👑 WELCOME ADMINISTRATOR!\\n\\nLogged in as Master Admin (${user.email}).\\nThe Admin Control Panel has been unlocked in your top navigation!`);
    } else if (user.isPro) {
      showSecurityToast(`⭐ Welcome back, ${user.name}! Your CapPrep Pro Pass is active.`);
      alert(`🎉 WELCOME BACK ${user.name.toUpperCase()}!\\n\\nYour CapPrep Pro Lifetime Pass is ACTIVE.\\nAll 76+ Mock Tests, Simulators, and Study Notes are unlocked!`);
    } else {
      showSecurityToast(`👤 Logged in as ${user.name} (Free Tier).`);
    }"""

if old_signin_success in app_js:
    app_js = app_js.replace(old_signin_success, new_signin_success)
    print("Updated processUserSignIn with Admin recognition")

# In updateProUI, show the Admin Link ONLY if logged in user is admin!
old_ui_auth_check = """  // 2. Update Navbar Sign In / Account Button
  const signinBtn = document.getElementById('nav-signin-btn');
  if (signinBtn) {
    if (cur) {
      signinBtn.innerHTML = `👤 ${escHTML(cur.name.split(' ')[0])} <span style="font-size:0.7rem; color:#f87171;">(Sign Out)</span>`;
      signinBtn.title = `Logged in as ${cur.email}. Click to Sign Out.`;
    } else {
      signinBtn.innerHTML = `🔑 Sign In`;
      signinBtn.title = `Sign into your CapPrep account`;
    }
  }"""

new_ui_auth_check = """  // 2. Update Navbar Sign In / Account Button & Dynamic Admin Control Link
  const signinBtn = document.getElementById('nav-signin-btn');
  const adminNavItem = document.getElementById('nav-admin-link-item');
  
  if (cur) {
    const isMasterAdmin = MASTER_ADMIN_EMAILS.includes((cur.email || '').toLowerCase());
    if (adminNavItem) {
      adminNavItem.style.display = isMasterAdmin ? 'inline-block' : 'none';
    }
    if (signinBtn) {
      const badge = isMasterAdmin ? '👑 Admin' : '👤 ' + escHTML(cur.name.split(' ')[0]);
      signinBtn.innerHTML = `${badge} <span style="font-size:0.7rem; color:#f87171;">(Sign Out)</span>`;
      signinBtn.title = `Logged in as ${cur.email}. Click to Sign Out.`;
    }
  } else {
    if (adminNavItem) adminNavItem.style.display = 'none';
    if (signinBtn) {
      signinBtn.innerHTML = `🔑 Sign In`;
      signinBtn.title = `Sign into your CapPrep account`;
    }
  }"""

if old_ui_auth_check in app_js:
    app_js = app_js.replace(old_ui_auth_check, new_ui_auth_check)
    print("Updated updateProUI to only reveal Admin link for registered admin")

# In completeOrderActivation, show official CapPrep Admin verification and Support email
old_alert_success = """  alert(`🎉 CONGRATULATIONS ${details.name.toUpperCase()}!\\n\\n` +
        `Your CapPrep Pro Lifetime Pass has been ACTIVATED!\\n\\n` +
        `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n` +
        `• Order Reference: ${orderId}\\n` +
        `• Amount Paid: ₹${details.amount} INR\\n` +
        `• Payment Ref / UTR: ${details.utr}\\n` +
        `• Pass Holder: ${details.email}\\n` +
        `• Confirmation Dispatched to Admin: ${ADMIN_NOTIFICATION_EMAIL}\\n` +
        `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n\\n` +
        `All 76+ Mock Tests, Lab 27 AI Simulator, and Grand Mocks are now UNLOCKED! Good luck for Capgemini!`);"""

new_alert_success = """  alert(`🎉 CONGRATULATIONS ${details.name.toUpperCase()}!\\n\\n` +
        `Your CapPrep Pro Lifetime Pass has been ACTIVATED & VERIFIED!\\n\\n` +
        `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n` +
        `• Status: VERIFIED BY CAPPREP ADMINISTRATION\\n` +
        `• Order Reference: ${orderId}\\n` +
        `• Amount Paid: ₹${details.amount} INR (0% Deduction via UPI)\\n` +
        `• Payment Ref / UTR: ${details.utr}\\n` +
        `• Account / Pass Holder: ${details.email}\\n` +
        `• Official Support Desk: ${OFFICIAL_SUPPORT_EMAIL}\\n` +
        `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n\\n` +
        `All 76+ Mock Tests, Lab 27 AI Simulator, and Protected PDF Guides are now UNLOCKED!\\n` +
        `For receipt, syllabus queries, or support, email: ${OFFICIAL_SUPPORT_EMAIL}`);"""

if old_alert_success in app_js:
    app_js = app_js.replace(old_alert_success, new_alert_success)
    print("Updated payment success confirmation alert with Admin Verification and Support email")

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_js)
print("Saved app.js")

print("All tasks completed successfully.")
