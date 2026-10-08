# -*- coding: utf-8 -*-
"""
Append VIP management JS functions to admin.html
"""

path = r"C:\cap\ai\admin.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

vip_functions = '''
// ==========================================
// VIP CANDIDATE 100% FREE ACCESS ENGINE
// ==========================================

function selfUnlockPro() {
  localStorage.setItem('capprep_pro_unlocked', 'true');
  localStorage.setItem('capprep_txn_id', 'ADMIN-RISHAV-VIP');
  localStorage.setItem('capprep_unlocked_date', new Date().toISOString());
  alert("⭐ SUCCESS! Pro Lifetime Access has been activated on your current browser!\\n\\nYou can now open the student site (index.html), take all 76+ Mock Tests, and open the Protected PDF reader without any restrictions.");
}

function openVipModal() {
  switchTab('vip-panel');
  document.getElementById('vip-grant-name').focus();
}

function getStoredVipWhitelist() {
  try {
    return JSON.parse(localStorage.getItem('capprep_vip_whitelist') || '[]');
  } catch(e) {
    return [];
  }
}

function saveStoredVipWhitelist(list) {
  localStorage.setItem('capprep_vip_whitelist', JSON.stringify(list));
}

function getStoredCustomCoupons() {
  try {
    return JSON.parse(localStorage.getItem('capprep_custom_coupons') || '["RISHAV100", "FREEVIP", "CAP2027", "EXCELLER100"]');
  } catch(e) {
    return ["RISHAV100", "FREEVIP", "CAP2027", "EXCELLER100"];
  }
}

function saveStoredCustomCoupons(list) {
  localStorage.setItem('capprep_custom_coupons', JSON.stringify(list));
}

function executeVipGrant() {
  const name = document.getElementById('vip-grant-name').value.trim() || "VIP Candidate";
  const idOrEmail = document.getElementById('vip-grant-id').value.trim();
  const phone = document.getElementById('vip-grant-phone').value.trim() || "+91 98000 00000";
  const reason = document.getElementById('vip-grant-reason').value.trim() || "100% Free VIP Pass";

  if (!idOrEmail) {
    alert("Please enter the Candidate ID, Roll Number, or Email.");
    document.getElementById('vip-grant-id').focus();
    return;
  }

  // 1. Add to VIP Whitelist
  const whitelist = getStoredVipWhitelist();
  const refCode = "VIP-" + Math.floor(10000 + Math.random() * 90000);
  
  // Check if already in whitelist
  const existingIdx = whitelist.findIndex(item => item.id.toLowerCase() === idOrEmail.toLowerCase());
  const entry = {
    ref: refCode,
    name: name,
    id: idOrEmail,
    phone: phone,
    reason: reason,
    date: new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString(),
    status: "ACTIVE_VIP"
  };

  if (existingIdx >= 0) {
    whitelist[existingIdx] = entry;
  } else {
    whitelist.unshift(entry);
  }
  saveStoredVipWhitelist(whitelist);

  // 2. Also register in the master orders ledger
  const orders = getStoredOrders();
  orders.unshift({
    orderId: refCode,
    name: name,
    email: idOrEmail,
    phone: phone,
    college: reason,
    amount: 0,
    method: "ADMIN_FREE_SUBSCRIPTION",
    utr: "GRANTED_BY_RISHAV",
    status: "VERIFIED",
    date: new Date().toLocaleString()
  });
  saveStoredOrders(orders);

  // 3. Clear inputs & refresh UI
  document.getElementById('vip-grant-name').value = '';
  document.getElementById('vip-grant-id').value = '';
  document.getElementById('vip-grant-phone').value = '';
  document.getElementById('vip-grant-reason').value = '';

  generateShareableVipLinkForEntry(idOrEmail, name);
  loadDashboardData();

  alert(`👑 SUCCESS! Candidate "${name}" (${idOrEmail}) now has 100% Free VIP Lifetime Access!\\n\\nTheir ID is whitelisted and a 1-click WhatsApp share link has been generated below.`);
}

function generateShareableVipLink() {
  const idOrEmail = document.getElementById('vip-grant-id').value.trim() || "candidate@college.edu";
  const name = document.getElementById('vip-grant-name').value.trim() || "Candidate";
  generateShareableVipLinkForEntry(idOrEmail, name);
}

function generateShareableVipLinkForEntry(idOrEmail, name) {
  const origin = window.location.origin;
  const path = window.location.pathname.replace('admin.html', 'index.html');
  const token = btoa(idOrEmail + ":FREE_VIP_PASS_RISHAV");
  const fullUrl = `${origin}${path}?vip_unlock=true&user=${encodeURIComponent(idOrEmail)}&name=${encodeURIComponent(name)}&token=${encodeURIComponent(token)}`;

  const outputDiv = document.getElementById('vip-link-output');
  const urlInput = document.getElementById('vip-generated-url');
  if (outputDiv && urlInput) {
    outputDiv.style.display = 'block';
    urlInput.value = fullUrl;
  }
}

function copyVipGeneratedLink() {
  const urlInput = document.getElementById('vip-generated-url');
  if (urlInput && urlInput.value) {
    navigator.clipboard.writeText(urlInput.value).then(() => {
      alert("📋 1-Click WhatsApp Invite Link copied to clipboard!\\n\\nSend this link to the student on WhatsApp or Email. When they click it, their browser automatically activates the Free VIP Pro Pass!");
    }).catch(() => {
      urlInput.select();
      document.execCommand('copy');
      alert("📋 Link copied to clipboard!");
    });
  }
}

function renderVipWhitelistTable() {
  const tbody = document.getElementById('vip-whitelist-table-body');
  const countEl = document.getElementById('tab-vip-count');
  if (!tbody) return;

  const list = getStoredVipWhitelist();
  if (countEl) countEl.textContent = list.length;

  if (list.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:2rem; color:var(--text-muted);">No candidate IDs whitelisted yet. Enter any student ID or email above to grant instant free access.</td></tr>`;
    return;
  }

  const origin = window.location.origin;
  const path = window.location.pathname.replace('admin.html', 'index.html');

  tbody.innerHTML = list.map(item => {
    const link = `${origin}${path}?vip_unlock=true&user=${encodeURIComponent(item.id)}&name=${encodeURIComponent(item.name)}`;
    return `
      <tr>
        <td><strong style="color:#c084fc; font-family:'JetBrains Mono'">${item.ref}</strong></td>
        <td><strong style="color:#fff;">${escapeHtml(item.name)}</strong></td>
        <td><code style="color:var(--accent); font-weight:700;">${escapeHtml(item.id)}</code></td>
        <td style="font-size:0.8rem; color:#94a3b8;">${escapeHtml(item.phone)}</td>
        <td><span style="font-size:0.75rem; background:rgba(124,58,237,0.15); color:#c084fc; border:1px solid rgba(124,58,237,0.3); padding:0.2rem 0.5rem; border-radius:4px;">${escapeHtml(item.reason)}</span></td>
        <td style="font-size:0.75rem; color:var(--text-muted);">${escapeHtml(item.date)}</td>
        <td><span class="status-badge status-success">● Free Lifetime</span></td>
        <td>
          <div style="display:flex; gap:0.4rem;">
            <button class="btn-action" style="padding:0.25rem 0.5rem; font-size:0.75rem;" onclick="navigator.clipboard.writeText('${link}').then(() => alert('📋 Link copied for ${escapeHtml(item.name)}!'))">🔗 Copy Link</button>
            <button class="btn-action" style="padding:0.25rem 0.5rem; font-size:0.75rem; color:#f87171;" onclick="revokeVipAccess('${item.id}')">Revoke</button>
          </div>
        </td>
      </tr>
    `;
  }).join('');
}

function revokeVipAccess(candidateId) {
  if (confirm(`Revoke free VIP subscription for "${candidateId}"?`)) {
    let list = getStoredVipWhitelist();
    list = list.filter(item => item.id.toLowerCase() !== candidateId.toLowerCase());
    saveStoredVipWhitelist(list);

    let orders = getStoredOrders();
    orders = orders.filter(o => (o.email || '').toLowerCase() !== candidateId.toLowerCase());
    saveStoredOrders(orders);

    loadDashboardData();
    alert(`❌ Free access revoked for ${candidateId}.`);
  }
}

function createCustomFreeCoupon() {
  const input = document.getElementById('new-free-coupon-code');
  if (!input) return;
  const code = (input.value || '').trim().toUpperCase();
  if (!code) {
    alert("Please enter a coupon code name.");
    return;
  }
  const coupons = getStoredCustomCoupons();
  if (!coupons.includes(code)) {
    coupons.push(code);
    saveStoredCustomCoupons(coupons);
    input.value = '';
    renderCustomCoupons();
    alert(`🎉 100% Free Coupon "${code}" created successfully!\\n\\nStudents who enter "${code}" at checkout will get 100% free access.`);
  } else {
    alert(`Coupon "${code}" already exists.`);
  }
}

function deleteCustomFreeCoupon(code) {
  if (confirm(`Delete coupon "${code}"?`)) {
    let coupons = getStoredCustomCoupons();
    coupons = coupons.filter(c => c !== code);
    saveStoredCustomCoupons(coupons);
    renderCustomCoupons();
  }
}

function renderCustomCoupons() {
  const container = document.getElementById('custom-coupons-list');
  if (!container) return;
  const coupons = getStoredCustomCoupons();
  container.innerHTML = coupons.map(c => `
    <div style="background:rgba(6,214,160,0.12); border:1px solid rgba(6,214,160,0.3); border-radius:6px; padding:0.35rem 0.75rem; display:flex; align-items:center; gap:0.5rem; font-size:0.82rem;">
      <strong style="color:var(--accent-green); font-family:'JetBrains Mono'">${escapeHtml(c)}</strong>
      <span style="color:#a7f3d0; font-size:0.75rem;">(100% FREE)</span>
      <button style="background:none; border:none; color:#f87171; cursor:pointer; font-size:0.85rem; padding:0;" onclick="deleteCustomFreeCoupon('${c}')" title="Delete">✕</button>
    </div>
  `).join('');
}
'''

# Update loadDashboardData in content to also call renderVipWhitelistTable() and renderCustomCoupons()
old_load = "  renderOrdersTable(orders);\n  renderNotificationsFeed();"
new_load = "  renderOrdersTable(orders);\n  renderNotificationsFeed();\n  renderVipWhitelistTable();\n  renderCustomCoupons();"

if old_load in content:
    content = content.replace(old_load, new_load)

# Append functions before </script>
content = content.replace('document.addEventListener(\'DOMContentLoaded\', checkAuth);', vip_functions + '\ndocument.addEventListener(\'DOMContentLoaded\', checkAuth);')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Appended VIP management functions to admin.html")
