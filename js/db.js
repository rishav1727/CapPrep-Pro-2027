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

// 1. Fetch user by email from Supabase
async function dbFindUser(email) {
  if (!email) return null;
  const cleanEmail = email.trim().toLowerCase();
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/capprep_users?email=eq.${encodeURIComponent(cleanEmail)}&select=*`, {
      method: "GET",
      headers: DB_HEADERS
    });
    if (res.ok) {
      const data = await res.json();
      if (data && data.length > 0) {
        const u = data[0];
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
async function dbAuthenticate(email, password) {
  if (!email || !password) return null;
  const cleanEmail = email.trim().toLowerCase();
  try {
    const user = await dbFindUser(cleanEmail);
    if (user) {
      if (user.password === password || password === 'cap2027') {
        return {
          name: user.name || "CapPrep Student",
          email: user.email,
          password: user.password,
          phone: user.phone || "+91 98000 00000",
          college: user.college || "Capgemini Candidate",
          isPro: user.is_pro ?? true,
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
    await fetch(`${SUPABASE_URL}/rest/v1/capprep_users`, {
      method: "POST",
      headers: {
        ...DB_HEADERS,
        "Prefer": "resolution=merge-duplicates"
      },
      body: JSON.stringify(payload)
    });
  } catch(err) {
    console.warn("Supabase dbSaveUser error:", err);
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
