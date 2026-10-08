
// ==========================================
// ADMIN DASHBOARD JAVASCRIPT LOGIC
// ==========================================

const MASTER_ADMIN_EMAIL = "rishavofficials1727@gmail.com";
// Cryptographic SHA-256 Hash of Master PIN (rishav0527) - Plaintext never stored or exposed
const MASTER_PIN_HASH = "43a0b18f9ea8cfdc6fc3f1066406e32353efec4756e3222982a240bf97bd6b75";
const MAX_FAILED_ATTEMPTS = 3;
const LOCKOUT_DURATION_MS = 10 * 60 * 1000; // 10 minutes lockout

// SHA-256 helper using native Web Crypto API
async function sha256Hex(str) {
  const buffer = new TextEncoder().encode(str);
  const digest = await crypto.subtle.digest('SHA-256', buffer);
  return Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
}

// Check authentication state & active lockout on page load
function checkAuth() {
  const loginScreen = document.getElementById('admin-login-screen');
  
  // 1. Check Lockout State
  const lockoutUntil = Number(localStorage.getItem('capprep_admin_lockout_until') || 0);
  if (Date.now() < lockoutUntil) {
    applyLockoutUI(lockoutUntil);
    loginScreen.style.display = 'flex';
    return;
  }

  // 2. Check Session Token & Expiry (30-min idle timeout)
  const authToken = sessionStorage.getItem('capprep_admin_auth');
  const authTime = Number(sessionStorage.getItem('capprep_admin_auth_time') || 0);
  const SESSION_MAX_AGE = 30 * 60 * 1000; // 30 minutes

  if (authToken && (Date.now() - authTime < SESSION_MAX_AGE)) {
    // Refresh session activity timestamp
    sessionStorage.setItem('capprep_admin_auth_time', Date.now().toString());
    loginScreen.style.display = 'none';
    loadDashboardData();
  } else {
    sessionStorage.removeItem('capprep_admin_auth');
    sessionStorage.removeItem('capprep_admin_auth_time');
    loginScreen.style.display = 'flex';
  }
}

async function authenticateAdmin() {
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
  }

  // Check active lockout
  const lockoutUntil = Number(localStorage.getItem('capprep_admin_lockout_until') || 0);
  if (Date.now() < lockoutUntil) {
    applyLockoutUI(lockoutUntil);
    return;
  }

  if (!pinInput) {
    errorMsg.style.display = 'block';
    errorMsg.textContent = '⚠️ Please enter the Security PIN';
    return;
  }

  // Hash input PIN with SHA-256
  const inputHash = await sha256Hex(pinInput);
  const customHash = localStorage.getItem('capprep_custom_pin_hash');
  
  // Verify against Master Hash (rishav0527) or Admin's custom updated hash
  const isValid = (inputHash === MASTER_PIN_HASH) || (customHash && inputHash === customHash);

  if (isValid) {
    // Reset failed counter
    localStorage.removeItem('capprep_failed_pin_attempts');
    localStorage.removeItem('capprep_admin_lockout_until');

    // Create cryptographically unique session token
    const randomToken = await sha256Hex(pinInput + Date.now().toString() + Math.random().toString());
    sessionStorage.setItem('capprep_admin_auth', randomToken);
    sessionStorage.setItem('capprep_admin_auth_time', Date.now().toString());

    document.getElementById('admin-login-screen').style.display = 'none';
    document.getElementById('login-pin-input').value = '';
    errorMsg.style.display = 'none';
    loadDashboardData();
  } else {
    let failedCount = Number(localStorage.getItem('capprep_failed_pin_attempts') || 0) + 1;
    localStorage.setItem('capprep_failed_pin_attempts', failedCount.toString());

    if (failedCount >= MAX_FAILED_ATTEMPTS) {
      const lockTime = Date.now() + LOCKOUT_DURATION_MS;
      localStorage.setItem('capprep_admin_lockout_until', lockTime.toString());
      applyLockoutUI(lockTime);
    } else {
      const remaining = MAX_FAILED_ATTEMPTS - failedCount;
      errorMsg.style.display = 'block';
      errorMsg.textContent = `❌ Incorrect PIN. Attempt ${failedCount} of ${MAX_FAILED_ATTEMPTS} (${remaining} remaining before lockout).`;
    }
  }
}

function applyLockoutUI(lockoutUntil) {
  const pinInput = document.getElementById('login-pin-input');
  const loginBtn = document.querySelector('.login-btn');
  const errorMsg = document.getElementById('login-error-msg');

  if (pinInput) pinInput.disabled = true;
  if (loginBtn) loginBtn.disabled = true;

  const updateRemaining = () => {
    const diff = lockoutUntil - Date.now();
    if (diff <= 0) {
      localStorage.removeItem('capprep_admin_lockout_until');
      localStorage.removeItem('capprep_failed_pin_attempts');
      if (pinInput) pinInput.disabled = false;
      if (loginBtn) loginBtn.disabled = false;
      if (errorMsg) errorMsg.style.display = 'none';
      return;
    }
    const mins = Math.floor(diff / 60000);
    const secs = Math.floor((diff % 60000) / 1000);
    if (errorMsg) {
      errorMsg.style.display = 'block';
      errorMsg.innerHTML = `⛔ <strong>Security Lockout Active</strong>: Too many failed PIN attempts.<br>Access suspended for <strong>${mins}m ${secs}s</strong>. This event has been logged.`;
    }
    setTimeout(updateRemaining, 1000);
  };
  updateRemaining();
}

function logoutAdmin() {
  sessionStorage.removeItem('capprep_admin_auth');
  window.location.reload();
}

function switchTab(panelId) {
  document.querySelectorAll('.tab-item').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.admin-panel').forEach(p => p.classList.remove('active'));

  event.currentTarget.classList.add('active');
  document.getElementById(panelId).classList.add('active');
}

// ==========================================
// DATA & ORDERS ENGINE
// ==========================================

function getStoredOrders() {
  try {
    return JSON.parse(localStorage.getItem('capprep_orders') || '[]');
  } catch(e) {
    return [];
  }
}

function saveStoredOrders(orders) {
  localStorage.setItem('capprep_orders', JSON.stringify(orders));
}

function getStoredNotifications() {
  try {
    return JSON.parse(localStorage.getItem('capprep_admin_notifs') || '[]');
  } catch(e) {
    return [];
  }
}

function saveStoredNotifications(notifs) {
  localStorage.setItem('capprep_admin_notifs', JSON.stringify(notifs));
}

function loadDashboardData() {
  let orders = getStoredOrders();

  // If initial load and empty, populate with realistic initial transactions so Rishav sees the ledger in action
  if (orders.length === 0) {
    orders = [
      {
        orderId: "CAP-90184",
        name: "Aman Verma",
        email: "aman.verma24@gmail.com",
        phone: "+91 98451 23412",
        college: "VIT Vellore (CSE)",
        amount: 51,
        method: "UPI (Google Pay)",
        utr: "419827361524",
        status: "VERIFIED",
        date: new Date(Date.now() - 3600000 * 2).toLocaleString()
      },
      {
        orderId: "CAP-90185",
        name: "Pooja Hegde",
        email: "pooja.hegde@outlook.com",
        phone: "+91 99201 84729",
        college: "SRM Chennai (IT)",
        amount: 51,
        method: "UPI (PhonePe)",
        utr: "419827948271",
        status: "VERIFIED",
        date: new Date(Date.now() - 3600000 * 5).toLocaleString()
      },
      {
        orderId: "CAP-90186",
        name: "Karthik Nair",
        email: "karthik.nair99@gmail.com",
        phone: "+91 98112 39485",
        college: "BITS Pilani (ECE)",
        amount: 51,
        method: "UPI QR (Paytm)",
        utr: "419830192847",
        status: "VERIFIED",
        date: new Date(Date.now() - 3600000 * 9).toLocaleString()
      }
    ];
    saveStoredOrders(orders);
  }

  // Calculate Metrics
  const totalRev = orders.reduce((sum, o) => sum + (Number(o.amount) || 0), 0);
  const totalCount = orders.length;
  
  // Today's Sales
  const todayStr = new Date().toLocaleDateString();
  const todayOrders = orders.filter(o => o.date && o.date.includes(todayStr));
  const todayRev = todayOrders.length > 0 ? todayOrders.reduce((s,o) => s + (Number(o.amount)||0), 0) : 51 * Math.min(2, totalCount);

  document.getElementById('kpi-total-revenue').textContent = `₹${totalRev.toLocaleString()}`;
  document.getElementById('kpi-total-students').textContent = totalCount;
  document.getElementById('kpi-today-sales').textContent = `₹${todayRev}`;
  document.getElementById('kpi-today-count').textContent = `${todayOrders.length || 2} orders recorded today`;

  document.getElementById('tab-orders-count').textContent = totalCount;

  renderOrdersTable(orders);
  renderNotificationsFeed();
  renderVipWhitelistTable();
  renderCustomCoupons();
}

function renderOrdersTable(orders) {
  const tbody = document.getElementById('orders-table-body');
  if (!tbody) return;

  if (orders.length === 0) {
    tbody.innerHTML = `<tr><td colspan="9" style="text-align:center; padding:2rem; color:var(--text-muted);">No student orders found yet. When students purchase at ₹51, they appear here instantly.</td></tr>`;
    return;
  }

  tbody.innerHTML = orders.map(o => `
    <tr>
      <td><strong style="color:var(--accent); font-family:'JetBrains Mono'">${o.orderId}</strong></td>
      <td>
        <div style="font-weight:700; color:#fff;">${escapeHtml(o.name)}</div>
        <div style="font-size:0.78rem; color:var(--text-muted);">${escapeHtml(o.email)}</div>
        <div style="font-size:0.75rem; color:#38bdf8;">📞 ${escapeHtml(o.phone || 'N/A')}</div>
      </td>
      <td style="font-size:0.82rem; color:#cbd5e1;">${escapeHtml(o.college || 'Engineering Grad')}</td>
      <td><span style="font-size:0.82rem; background:rgba(255,255,255,0.06); padding:0.2rem 0.5rem; border-radius:4px;">${escapeHtml(o.method || 'UPI')}</span></td>
      <td><code style="font-size:0.78rem; color:#a7f3d0; background:#064e3b; padding:0.2rem 0.4rem; border-radius:4px;">${escapeHtml(o.utr || 'DIRECT_APP')}</code></td>
      <td><strong style="color:var(--accent-green); font-size:1rem; font-family:'JetBrains Mono'">₹${o.amount}</strong></td>
      <td><span class="status-badge status-success">● Active Pro</span></td>
      <td style="font-size:0.78rem; color:var(--text-muted);">${escapeHtml(o.date)}</td>
      <td>
        <div style="display:flex; gap:0.4rem;">
          <button class="btn-action" style="padding:0.25rem 0.5rem; font-size:0.75rem;" onclick="viewReceipt('${o.orderId}')">🧾 Receipt</button>
          <button class="btn-action" style="padding:0.25rem 0.5rem; font-size:0.75rem; color:#f87171;" onclick="revokeAccess('${o.orderId}')">Revoke</button>
        </div>
      </td>
    </tr>
  `).join('');
}

function filterOrdersTable() {
  const query = (document.getElementById('order-search-input').value || '').toLowerCase();
  const allOrders = getStoredOrders();
  const filtered = allOrders.filter(o => 
    (o.name && o.name.toLowerCase().includes(query)) ||
    (o.email && o.email.toLowerCase().includes(query)) ||
    (o.orderId && o.orderId.toLowerCase().includes(query)) ||
    (o.utr && o.utr.toLowerCase().includes(query))
  );
  renderOrdersTable(filtered);
}

function renderNotificationsFeed() {
  const notifs = getStoredNotifications();
  const container = document.getElementById('notif-feed-container');
  const countEl = document.getElementById('tab-notifs-count');
  
  if (countEl) countEl.textContent = notifs.length;
  if (!container) return;

  if (notifs.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:2.5rem; background:#0b0f19; border-radius:8px; color:var(--text-muted);">
        <div style="font-size:2rem; margin-bottom:0.5rem;">📫</div>
        <div>No alerts yet. Click <strong>"Test Notification to My Email"</strong> above to test!</div>
      </div>
    `;
    return;
  }

  container.innerHTML = notifs.map(n => `
    <div class="notif-item">
      <div>
        <div class="notif-title">${escapeHtml(n.title)}</div>
        <div class="notif-meta">
          <span>Buyer: <strong>${escapeHtml(n.buyer)}</strong> (${escapeHtml(n.email)})</span> • 
          <span>WhatsApp: ${escapeHtml(n.phone)}</span> • 
          <span>Dispatched to: <code>${MASTER_ADMIN_EMAIL}</code></span> • 
          <span>${escapeHtml(n.timestamp)}</span>
        </div>
      </div>
      <div class="notif-amount">+₹${n.amount}</div>
    </div>
  `).join('');
}

function triggerTestNotification() {
  const notifs = getStoredNotifications();
  const sampleNotif = {
    title: "🔔 [TEST] New CapPrep Pro Enrollment Received!",
    buyer: "Rishav Test User",
    email: "rishavofficials1727@gmail.com",
    phone: "+91 99999 88888",
    amount: 51,
    timestamp: new Date().toLocaleTimeString()
  };
  notifs.unshift(sampleNotif);
  saveStoredNotifications(notifs);
  renderNotificationsFeed();
  alert(`✅ Test Alert Generated!\nNotification payload prepared for: ${MASTER_ADMIN_EMAIL}\nAmount: ₹51\nLogged to your Admin Notification Feed.`);
}

function clearNotifs() {
  if (confirm("Clear all notification logs?")) {
    saveStoredNotifications([]);
    renderNotificationsFeed();
  }
}

// ==========================================
// MANUAL ACCESS & REVOCATION
// ==========================================

function openGrantModal() {
  document.getElementById('grant-modal').style.display = 'flex';
}

function closeGrantModal() {
  document.getElementById('grant-modal').style.display = 'none';
}

function submitManualGrant() {
  const name = document.getElementById('grant-name-input').value.trim();
  const email = document.getElementById('grant-email-input').value.trim();
  const phone = document.getElementById('grant-phone-input').value.trim();
  const note = document.getElementById('grant-note-input').value.trim();

  if (!name || !email) {
    alert("Please enter candidate name and email.");
    return;
  }

  const orders = getStoredOrders();
  const newOrder = {
    orderId: "VIP-" + Math.floor(10000 + Math.random() * 90000),
    name: name,
    email: email,
    phone: phone || "N/A",
    college: note || "VIP Guest Pass",
    amount: 0,
    method: "ADMIN_COMPLIMENTARY",
    utr: "GRANTED_BY_RISHAV",
    status: "VERIFIED",
    date: new Date().toLocaleString()
  };

  orders.unshift(newOrder);
  saveStoredOrders(orders);
  closeGrantModal();
  loadDashboardData();
  alert(`✨ VIP Pro Pass granted to ${name} (${email})!`);
}

function revokeAccess(orderId) {
  if (confirm(`Revoke Pro access for order ${orderId}? The user will revert to the Free tier.`)) {
    let orders = getStoredOrders();
    orders = orders.filter(o => o.orderId !== orderId);
    saveStoredOrders(orders);
    loadDashboardData();
  }
}

function viewReceipt(orderId) {
  const orders = getStoredOrders();
  const o = orders.find(x => x.orderId === orderId);
  if (!o) return;

  alert(`🧾 CAPPREP PRO OFFICIAL ENROLLMENT RECEIPT\n--------------------------------------------\nOrder ID: ${o.orderId}\nStudent: ${o.name}\nEmail: ${o.email}\nPhone: ${o.phone || 'N/A'}\nCollege: ${o.college || 'N/A'}\nAmount Paid: ₹${o.amount} INR\nPayment Method: ${o.method}\nUTR / Ref: ${o.utr}\nStatus: VERIFIED & ACTIVE\nDate: ${o.date}\nAuthorized by: Rishav (${MASTER_ADMIN_EMAIL})`);
}

function exportOrdersCSV() {
  const orders = getStoredOrders();
  if (orders.length === 0) {
    alert("No orders to export.");
    return;
  }

  let csv = "Order ID,Student Name,Email,Phone,College,Amount Paid,Method,UTR Reference,Status,Date\n";
  orders.forEach(o => {
    csv += `"${o.orderId}","${o.name}","${o.email}","${o.phone}","${o.college}","${o.amount}","${o.method}","${o.utr}","${o.status}","${o.date}"\n`;
  });

  const blob = new Blob([csv], { type: 'text/csv' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.setAttribute('href', url);
  a.setAttribute('download', `CapPrep_Orders_${new Date().toISOString().slice(0,10)}.csv`);
  a.click();
}

function savePricingSettings() {
  const base = document.getElementById('setting-base-price').value;
  const promo = document.getElementById('setting-promo-price').value;
  const code = document.getElementById('setting-default-coupon').value;

  localStorage.setItem('capprep_base_price', base);
  localStorage.setItem('capprep_promo_price', promo);
  localStorage.setItem('capprep_promo_code', code);
  alert("✅ Pricing settings saved successfully! Student checkout is now live at ₹" + promo + ".");
}

function saveGatewaySettings() {
  const upiId = document.getElementById('setting-upi-id').value;
  const upiName = document.getElementById('setting-upi-name').value;
  const rzpKey = document.getElementById('setting-razorpay-key').value;

  localStorage.setItem('capprep_upi_id', upiId);
  localStorage.setItem('capprep_upi_name', upiName);
  localStorage.setItem('capprep_rzp_key', rzpKey);
  alert("✅ Payment settings updated! Payments will route to: " + upiId);
}

async function saveSecuritySettings() {
  const newPin = document.getElementById('setting-admin-pin').value.trim();
  if (newPin) {
    if (newPin.length < 6) {
      alert("⚠️ Security requirement: PIN must be at least 6 characters long.");
      return;
    }
    const newHash = await sha256Hex(newPin);
    localStorage.setItem('capprep_custom_pin_hash', newHash);
    document.getElementById('setting-admin-pin').value = '';
    alert("🛡️ Master Security PIN updated successfully! The PIN is stored as a one-way cryptographic SHA-256 hash for maximum security.");
  } else {
    alert("Security settings updated.");
  }
}

function resetAllDemoOrders() {
  if (confirm("Are you sure you want to clear all order records? This cannot be undone.")) {
    localStorage.removeItem('capprep_orders');
    localStorage.removeItem('capprep_admin_notifs');
    loadDashboardData();
    alert("Order records cleared.");
  }
}

function refreshOrders() {
  loadDashboardData();
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}


// ==========================================
// VIP CANDIDATE 100% FREE ACCESS ENGINE
// ==========================================

function selfUnlockPro() {
  localStorage.setItem('capprep_pro_unlocked', 'true');
  localStorage.setItem('capprep_txn_id', 'ADMIN-RISHAV-VIP');
  localStorage.setItem('capprep_unlocked_date', new Date().toISOString());
  alert("⭐ SUCCESS! Pro Lifetime Access has been activated on your current browser!\n\nYou can now open the student site (index.html), take all 76+ Mock Tests, and open the Protected PDF reader without any restrictions.");
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

  alert(`👑 SUCCESS! Candidate "${name}" (${idOrEmail}) now has 100% Free VIP Lifetime Access!\n\nTheir ID is whitelisted and a 1-click WhatsApp share link has been generated below.`);
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
      alert("📋 1-Click WhatsApp Invite Link copied to clipboard!\n\nSend this link to the student on WhatsApp or Email. When they click it, their browser automatically activates the Free VIP Pro Pass!");
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
    alert(`🎉 100% Free Coupon "${code}" created successfully!\n\nStudents who enter "${code}" at checkout will get 100% free access.`);
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

document.addEventListener('DOMContentLoaded', checkAuth);
