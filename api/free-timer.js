// api/free-timer.js
// Vercel Serverless Function
// Tracks a visitor's first-access time by IP and returns how many seconds remain
// of their 5-minute (300 s) free window for the Study Reader.

const SUPABASE_URL      = process.env.SUPABASE_URL      || "https://ynayovthgrlysfogleqo.supabase.co";
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InluYXlvdnRoZ3JseXNmb2dsZXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2MTg4NzYsImV4cCI6MjEwNzE5NDg3Nn0.NkHNeS6FTzshLmETxaSEravCBA9ner9gjyKvcUZK4Qs";

const FREE_SECONDS = 300; // 5 minutes

const SB_HEADERS = {
  "Content-Type": "application/json",
  "apikey": SUPABASE_ANON_KEY,
  "Authorization": `Bearer ${SUPABASE_ANON_KEY}`
};

function getClientIP(req) {
  // Vercel forwards the real IP in x-forwarded-for
  const forwarded = req.headers['x-forwarded-for'];
  if (forwarded) return forwarded.split(',')[0].trim();
  return req.socket?.remoteAddress || req.connection?.remoteAddress || 'unknown';
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method Not Allowed' });

  const ip = getClientIP(req);
  const now = Date.now();

  try {
    // 1. Look up existing record for this IP
    const lookupRes = await fetch(
      `${SUPABASE_URL}/rest/v1/capprep_free_timer?ip=eq.${encodeURIComponent(ip)}&select=*`,
      { method: 'GET', headers: SB_HEADERS }
    );

    if (!lookupRes.ok) throw new Error('Supabase lookup failed: ' + lookupRes.status);

    const rows = await lookupRes.json();

    if (rows.length > 0) {
      // Existing visitor — return remaining time
      const firstSeen = new Date(rows[0].first_seen_at).getTime();
      const elapsed   = Math.floor((now - firstSeen) / 1000);
      const remaining = Math.max(0, FREE_SECONDS - elapsed);
      return res.status(200).json({ remaining, firstSeen: rows[0].first_seen_at, ip });
    }

    // 2. New visitor — insert their first-seen timestamp
    const insertRes = await fetch(
      `${SUPABASE_URL}/rest/v1/capprep_free_timer`,
      {
        method: 'POST',
        headers: { ...SB_HEADERS, "Prefer": "resolution=merge-duplicates" },
        body: JSON.stringify({ ip, first_seen_at: new Date(now).toISOString() })
      }
    );

    if (!insertRes.ok) {
      const errText = await insertRes.text();
      console.warn('Supabase insert error:', errText);
      // Fail open: give them the full window so a DB hiccup doesn't block everyone
      return res.status(200).json({ remaining: FREE_SECONDS, firstSeen: new Date(now).toISOString(), ip });
    }

    return res.status(200).json({ remaining: FREE_SECONDS, firstSeen: new Date(now).toISOString(), ip });

  } catch (err) {
    console.error('free-timer error:', err);
    // Fail open on network errors
    return res.status(200).json({ remaining: FREE_SECONDS, firstSeen: new Date().toISOString(), ip: 'error' });
  }
}
