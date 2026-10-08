# -*- coding: utf-8 -*-
"""
Update C:\cap\ai\js\app.js with VIP Whitelist checking, custom coupon support,
and 1-click URL parameter VIP activation.
"""

path = r"C:\cap\ai\js\app.js"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update applyCoupon to support all built-in and admin custom 100% free coupons
old_coupon_block = """  if (code === 'SUPER51' || code === 'CAP51') {
    currentPayablePrice = 51;
    if (priceDisplay) priceDisplay.textContent = '₹51';
    feedback.innerHTML = `<span style="color:#06d6a0">🎉 Auto-Coupon Applied! You save ₹248 (83% OFF). Pay ₹51.</span>`;
  } else if (code === 'CAP2027' || code === 'EXCELLER100' || code === 'FREEPASS') {
    currentPayablePrice = 0;
    if (priceDisplay) priceDisplay.textContent = '₹0';
    feedback.innerHTML = `<span style="color:#06d6a0">🎉 VIP Voucher Applied: 100% OFF! Activating Pro Pass...</span>`;
    setTimeout(() => {
      completeOrderActivation({
        name: document.getElementById('cust-name-input')?.value || "VIP Student",
        email: document.getElementById('cust-email-input')?.value || "vip@candidate.edu",
        phone: document.getElementById('cust-phone-input')?.value || "VIP",
        college: "Campus VIP",
        method: "COUPON_" + code,
        utr: "PROMO_100_FREE",
        amount: 0
      });
    }, 700);
  } else if (code === 'PRO50') {
    currentPayablePrice = 149;
    if (priceDisplay) priceDisplay.textContent = '₹149';
    feedback.innerHTML = `<span style="color:#00d4ff">🏷️ 50% OFF applied! Special price ₹149.</span>`;
  } else {
    feedback.innerHTML = `<span style="color:#ef4444">❌ Invalid code. Use default <strong>SUPER51</strong> for ₹51 flash access.</span>`;
  }"""

new_coupon_block = """  // Built-in 100% free codes & custom admin codes
  let customCoupons = [];
  try {
    customCoupons = JSON.parse(localStorage.getItem('capprep_custom_coupons') || '[]');
  } catch(e) {}
  const freeCodes = ['CAP2027', 'EXCELLER100', 'FREEPASS', 'RISHAV100', 'FREEVIP', 'RISHAVVIP', 'FREECAP', 'VIP100', 'VIPFREE', 'SUPERFREE', ...customCoupons];

  if (code === 'SUPER51' || code === 'CAP51') {
    currentPayablePrice = 51;
    if (priceDisplay) priceDisplay.textContent = '₹51';
    feedback.innerHTML = `<span style="color:#06d6a0">🎉 Auto-Coupon Applied! You save ₹248 (83% OFF). Pay ₹51.</span>`;
  } else if (freeCodes.includes(code)) {
    currentPayablePrice = 0;
    if (priceDisplay) priceDisplay.textContent = '₹0 (FREE VIP)';
    feedback.innerHTML = `<span style="color:#06d6a0">👑 VIP 100% Free Pass Applied! Activating Lifetime Pro Access...</span>`;
    setTimeout(() => {
      completeOrderActivation({
        name: document.getElementById('cust-name-input')?.value || "VIP Candidate",
        email: document.getElementById('cust-email-input')?.value || "vip@candidate.edu",
        phone: document.getElementById('cust-phone-input')?.value || "+91 98000 00000",
        college: "VIP Scholarship / Exemption",
        method: "ADMIN_FREE_COUPON_" + code,
        utr: "FREE_BY_RISHAV",
        amount: 0
      });
    }, 600);
  } else if (code === 'PRO50') {
    currentPayablePrice = 149;
    if (priceDisplay) priceDisplay.textContent = '₹149';
    feedback.innerHTML = `<span style="color:#00d4ff">🏷️ 50% OFF applied! Special price ₹149.</span>`;
  } else {
    feedback.innerHTML = `<span style="color:#ef4444">❌ Invalid code. Use default <strong>SUPER51</strong> for ₹51 flash access.</span>`;
  }"""

if old_coupon_block in code:
    code = code.replace(old_coupon_block, new_coupon_block)
    print("Replaced coupon block successfully")
else:
    print("Warning: old_coupon_block not found directly")

# 2. Add VIP whitelist check and URL param check
vip_helper_logic = """
// Check if candidate email/ID is in VIP whitelist
function checkVipCandidateWhitelist(inputVal) {
  if (!inputVal) return false;
  const val = inputVal.trim().toLowerCase();
  try {
    const list = JSON.parse(localStorage.getItem('capprep_vip_whitelist') || '[]');
    const match = list.find(item => item.id && item.id.trim().toLowerCase() === val);
    if (match) {
      currentPayablePrice = 0;
      const priceDisplay = document.getElementById('modal-display-price');
      if (priceDisplay) priceDisplay.textContent = '₹0 (FREE VIP)';
      const feedback = document.getElementById('coupon-feedback');
      if (feedback) {
        feedback.innerHTML = `<span style="color:#06d6a0">👑 Welcome VIP Candidate <strong>${escHTML(match.name)}</strong>! Your subscription is 100% FREE pre-approved by Admin Rishav.</span>`;
      }
      return true;
    }
  } catch(e) {}
  return false;
}

// Attach listener to customer email input when modal opens
"""

# 3. Update DOMContentLoaded to check URL parameters for 1-click VIP unlock links
old_dom_init = """// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  updateProUI();
  startSocialProofLoop();
  // Ensure all sections are visible immediately
  document.querySelectorAll('.fade-in').forEach(el => {
    el.classList.add('visible');
    el.style.opacity = '1';
    el.style.transform = 'none';
  });
});"""

new_dom_init = """// VIP Whitelist auto-check helper
function initVipCheckListeners() {
  const emailInput = document.getElementById('cust-email-input');
  if (emailInput) {
    emailInput.addEventListener('input', (e) => {
      checkVipCandidateWhitelist(e.target.value);
    });
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  // Check 1-Click VIP Unlock via URL parameter (e.g. sent by Rishav via WhatsApp)
  try {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('vip_unlock') === 'true' || urlParams.get('unlock_vip') === 'true') {
      const candidateUser = urlParams.get('user') || 'VIP Candidate';
      const candidateName = urlParams.get('name') || candidateUser;
      unlockProPass('VIP-LINK-' + candidateUser);
      showSecurityToast(`👑 VIP Pro Lifetime Pass Activated! Sponsored by Admin Rishav for ${candidateName}.`);
      alert(`🎉 WELCOME ${candidateName.toUpperCase()}!\\n\\nYour CapPrep Pro Lifetime Pass has been ACTIVATED for 100% FREE!\\nSponsored by Master Admin Rishav (rishavofficials1727@gmail.com).\\n\\nAll 76+ Mock Tests, Lab 27 AI Simulator, and Protected PDF Guides are now UNLOCKED!`);
    } else if (urlParams.get('coupon')) {
      const c = urlParams.get('coupon').toUpperCase();
      const codeInput = document.getElementById('coupon-code-input');
      if (codeInput) {
        codeInput.value = c;
        openPaymentModal();
        applyCoupon();
      }
    }
  } catch(err) {
    console.error("VIP URL check error:", err);
  }

  updateProUI();
  startSocialProofLoop();
  initVipCheckListeners();

  // Ensure all sections are visible immediately
  document.querySelectorAll('.fade-in').forEach(el => {
    el.classList.add('visible');
    el.style.opacity = '1';
    el.style.transform = 'none';
  });
});"""

if old_dom_init in code:
    code = code.replace(old_dom_init, vip_helper_logic + "\n" + new_dom_init)
    print("Replaced DOMContentLoaded initialization with VIP checker successfully")
else:
    print("Warning: old_dom_init not found directly")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated app.js with VIP whitelist and 1-click URL unlock support.")
