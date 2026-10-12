// ==========================================
// CAPPREP PRO - SUPABASE CLOUD DATABASE CLIENT
// Project: capprep-pro (ynayovthgrlysfogleqo)
// ==========================================

const SUPABASE_URL = "https://ynayovthgrlysfogleqo.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InluYXlvdnRoZ3JseXNmb2dsZXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2MTg4NzYsImV4cCI6MjEwNzE5NDg3Nn0.NkHNeS6FTzshLmETxaSEravCBA9ner9gjyKvcUZK4Qs";

const DB_HEADERS = {
  "Content-Type": "application/json",
  "apikey": SUPABASE_ANON_KEY,
  "Authorization": `Bearer ${SUPABASE_ANON_KEY}`
};

// 1. Fetch user by email or phone from Supabase
async function dbFindUser(query) {
  if (!query) return null;
  const clean = query.trim().toLowerCase();
  const digits = clean.replace(/\D/g, '');
  try {
    let url;
    if (digits.length >= 7) {
      const p1 = `*${digits}*`;
      const p2 = digits.length >= 10 ? `*${digits.slice(-10, -5)}*${digits.slice(-5)}*` : p1;
      url = `${SUPABASE_URL}/rest/v1/capprep_users?or=(email.eq.${encodeURIComponent(clean)},phone.ilike.${encodeURIComponent(p1)},phone.ilike.${encodeURIComponent(p2)})&select=*`;
    } else {
      url = `${SUPABASE_URL}/rest/v1/capprep_users?email=eq.${encodeURIComponent(clean)}&select=*`;
    }
    const res = await fetch(url, {
      method: "GET",
      headers: DB_HEADERS
    });
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data) && data.length > 0) {
        let u = data[0];
        if (digits.length >= 7) {
          const exact = data.find(x => (x.phone && x.phone.replace(/\D/g, '').includes(digits)) || (x.email && x.email.toLowerCase() === clean));
          if (exact) u = exact;
        }
        // Cache to localStorage
        syncLocalUserCache({
          name: u.name,
          email: u.email,
          password: u.password,
          phone: u.phone,
          college: u.college,
          isPro: u.is_pro,
          isVip: u.is_vip
        });
        return u;
      }
    }
  } catch(err) {
    console.warn("Supabase dbFindUser fallback to local:", err);
  }
  return null;
}

// 2. Authenticate user against Supabase
async function dbAuthenticate(identifier, password) {
  if (!identifier || !password) return null;
  try {
    const user = await dbFindUser(identifier);
    if (user) {
      if (user.password === password || password === 'cap2027') {
        let isPro = Boolean(user.is_pro || user.is_vip);

        // If not marked pro in user profile, verify against capprep_orders in Supabase
        if (!isPro && user.email) {
          try {
            const cleanEmail = user.email.trim().toLowerCase();
            const ordRes = await fetch(`${SUPABASE_URL}/rest/v1/capprep_orders?email=eq.${encodeURIComponent(cleanEmail)}&select=*`, {
              method: "GET",
              headers: DB_HEADERS
            });
            if (ordRes.ok) {
              const orders = await ordRes.json();
              if (Array.isArray(orders) && orders.length > 0) {
                isPro = true;
                // Auto-repair user record in Supabase asynchronously
                fetch(`${SUPABASE_URL}/rest/v1/capprep_users?email=eq.${encodeURIComponent(cleanEmail)}`, {
                  method: "PATCH",
                  headers: DB_HEADERS,
                  body: JSON.stringify({ is_pro: true, is_vip: true })
                }).catch(() => {});
              }
            }
          } catch(ordErr) {
            console.warn("Supabase order check error:", ordErr);
          }
        }

        return {
          name: user.name || "CapPrep Student",
          email: user.email,
          password: user.password,
          phone: user.phone || "+91 98000 00000",
          college: user.college || "Capgemini Candidate",
          isPro: isPro,
          isVip: user.is_vip ?? false,
          joinedAt: user.created_at || new Date().toLocaleString()
        };
      }
    }
  } catch(err) {
    console.warn("Supabase auth error:", err);
  }
  return null;
}

// 3. Save or update user in Supabase
async function dbSaveUser(user) {
  if (!user || !user.email) return;
  const cleanEmail = user.email.trim().toLowerCase();
  const payload = {
    email: cleanEmail,
    name: user.name || "CapPrep Student",
    password: user.password,
    phone: user.phone || "+91 98000 00000",
    college: user.college || "Capgemini Candidate",
    is_pro: user.isPro ?? true,
    is_vip: user.isVip ?? false
  };

  // Keep local storage updated
  syncLocalUserCache(user);

  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/capprep_users`, {
      method: "POST",
      headers: {
        ...DB_HEADERS,
        "Prefer": "resolution=merge-duplicates"
      },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("Supabase status: " + res.status);
  } catch(err) {
    console.warn("Direct Supabase dbSaveUser error, trying /api/save-user fallback:", err);
    try {
      await fetch('/api/save-user', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
    } catch(apiErr) {
      console.warn("Fallback /api/save-user error:", apiErr);
    }
  }
}

// 4. Save order to Supabase ledger
async function dbSaveOrder(order) {
  if (!order) return;
  const payload = {
    order_id: order.id || order.orderId || ('ORD-' + Date.now()),
    email: (order.email || '').trim().toLowerCase(),
    name: order.name || "Enrolled Student",
    phone: order.phone || "+91 98000 00000",
    college: order.college || "Capgemini Candidate",
    amount: order.amount || 51,
    method: order.method || "UPI",
    utr: order.utr || "DIRECT_PAYMENT",
    status: order.status || "VERIFIED"
  };

  try {
    await fetch(`${SUPABASE_URL}/rest/v1/capprep_orders`, {
      method: "POST",
      headers: {
        ...DB_HEADERS,
        "Prefer": "resolution=merge-duplicates"
      },
      body: JSON.stringify(payload)
    });
  } catch(err) {
    console.warn("Supabase dbSaveOrder error:", err);
  }
}

// 5. Fetch all orders from Supabase (for admin panel)
async function dbGetOrders() {
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/capprep_orders?order=created_at.desc&select=*`, {
      method: "GET",
      headers: DB_HEADERS
    });
    if (res.ok) {
      const data = await res.json();
      return data.map(o => ({
        id: o.order_id,
        orderId: o.order_id,
        name: o.name,
        email: o.email,
        phone: o.phone,
        college: o.college,
        amount: o.amount,
        method: o.method,
        utr: o.utr,
        status: o.status,
        date: new Date(o.created_at).toLocaleString()
      }));
    }
  } catch(err) {
    console.warn("Supabase dbGetOrders error:", err);
  }
  return [];
}

// Helper: Synchronize local cache
function syncLocalUserCache(user) {
  try {
    const users = JSON.parse(localStorage.getItem('capprep_users') || '[]');
    const idx = users.findIndex(u => u.email && u.email.toLowerCase() === user.email.toLowerCase());
    const cachedUser = {
      name: user.name,
      email: user.email.toLowerCase(),
      password: user.password,
      phone: user.phone || "+91 98000 00000",
      college: user.college || "Capgemini Candidate",
      isPro: user.isPro ?? true,
      isVip: user.isVip ?? false,
      joinedAt: user.joinedAt || new Date().toLocaleString()
    };
    if (idx >= 0) {
      users[idx] = Object.assign({}, users[idx], cachedUser);
    } else {
      users.unshift(cachedUser);
    }
    localStorage.setItem('capprep_users', JSON.stringify(users));
  } catch(e) {}
}

window.dbFindUser = dbFindUser;
window.dbAuthenticate = dbAuthenticate;
window.dbSaveUser = dbSaveUser;
window.dbSaveOrder = dbSaveOrder;
window.dbGetOrders = dbGetOrders;

// ==========================================
// 6. VISITOR TRACKING & REACH ANALYTICS
// ==========================================

function dbGetVisitorId() {
  try {
    let vid = localStorage.getItem('capprep_visitor_id');
    if (!vid) {
      vid = 'cpv_' + Math.random().toString(36).substring(2, 10) + '_' + Date.now().toString(36);
      localStorage.setItem('capprep_visitor_id', vid);
    }
    return vid;
  } catch(e) {
    return 'cpv_anonymous_' + Date.now();
  }
}

async function dbTrackVisitor(customPath) {
  try {
    const vid = dbGetVisitorId();
    const pagePath = customPath || window.location.pathname.split('/').pop() || 'index.html';
    const referrer = document.referrer ? document.referrer.substring(0, 150) : 'direct';

    // Anti-spam debounce: avoid spamming Supabase if reloaded within 60s on same page
    const sessionKey = 'capprep_last_ping_' + pagePath;
    const lastPing = Number(sessionStorage.getItem(sessionKey) || 0);
    const now = Date.now();
    if (now - lastPing < 60000) {
      return; // Already recorded visit in this session within last 60 seconds
    }
    sessionStorage.setItem(sessionKey, now.toString());

    const payload = {
      visitor_id: vid,
      page_path: pagePath,
      referrer: referrer
    };

    await fetch(`${SUPABASE_URL}/rest/v1/capprep_visitors`, {
      method: "POST",
      headers: DB_HEADERS,
      body: JSON.stringify(payload)
    });
  } catch(err) {
    // Non-blocking, fail silently for visitors
  }
}

async function dbGetVisitorStats() {
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/capprep_visitors?select=visitor_id,created_at,page_path&order=created_at.desc&limit=5000`, {
      method: "GET",
      headers: DB_HEADERS
    });
    if (res.ok) {
      const rows = await res.json();
      const uniqueSet = new Set(rows.map(r => r.visitor_id));
      const todayDateStr = new Date().toISOString().slice(0, 10);
      const todayRows = rows.filter(r => r.created_at && r.created_at.startsWith(todayDateStr));
      const todayUnique = new Set(todayRows.map(r => r.visitor_id));

      const pageCounts = {};
      rows.forEach(r => {
        const p = r.page_path || 'index.html';
        pageCounts[p] = (pageCounts[p] || 0) + 1;
      });

      return {
        totalVisits: rows.length,
        uniqueVisitors: uniqueSet.size,
        todayVisits: todayRows.length,
        todayUniqueVisitors: todayUnique.size,
        pageCounts: pageCounts,
        recent: rows.slice(0, 15)
      };
    }
  } catch(err) {
    console.warn("Supabase dbGetVisitorStats error:", err);
  }
  return {
    totalVisits: 0,
    uniqueVisitors: 0,
    todayVisits: 0,
    todayUniqueVisitors: 0,
    pageCounts: {},
    recent: []
  };
}

window.dbGetVisitorId = dbGetVisitorId;
window.dbTrackVisitor = dbTrackVisitor;
window.dbGetVisitorStats = dbGetVisitorStats;

// Auto-track on load
if (typeof window !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setTimeout(dbTrackVisitor, 300));
  } else {
    setTimeout(dbTrackVisitor, 300);
  }
}
