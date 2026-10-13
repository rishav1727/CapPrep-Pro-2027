// api/referral-stats.js
// Tracks and counts referrals by visitor ID & IP

const SUPABASE_URL = process.env.SUPABASE_URL || "https://ynayovthgrlysfogleqo.supabase.co";
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InluYXlvdnRoZ3JseXNmb2dsZXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2MTg4NzYsImV4cCI6MjEwNzE5NDg3Nn0.NkHNeS6FTzshLmETxaSEravCBA9ner9gjyKvcUZK4Qs";

const SB_HEADERS = {
  "Content-Type": "application/json",
  "apikey": SUPABASE_ANON_KEY,
  "Authorization": `Bearer ${SUPABASE_ANON_KEY}`
};

function getClientIP(req) {
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

  const ref = req.query.ref;
  const track = req.query.track === '1';
  const ip = getClientIP(req);

  if (!ref) {
    return res.status(400).json({ error: 'Missing ref parameter' });
  }

  try {
    // If track=1, record this referral event if this IP has not been referred for this ref yet
    if (track && ip) {
      const checkRes = await fetch(
        `${SUPABASE_URL}/rest/v1/capprep_referrals?referred_ip=eq.${encodeURIComponent(ip)}&select=id`,
        { method: 'GET', headers: SB_HEADERS }
      );
      if (checkRes.ok) {
        const existing = await checkRes.json();
        if (!existing || existing.length === 0) {
          // Record referral
          await fetch(`${SUPABASE_URL}/rest/v1/capprep_referrals`, {
            method: 'POST',
            headers: SB_HEADERS,
            body: JSON.stringify({
              referrer_id: ref,
              referred_ip: ip
            })
          });
        }
      }
    }

    // Count referrals for this referrer_id
    const countRes = await fetch(
      `${SUPABASE_URL}/rest/v1/capprep_referrals?referrer_id=eq.${encodeURIComponent(ref)}&select=id`,
      { method: 'GET', headers: SB_HEADERS }
    );

    let count = 0;
    if (countRes.ok) {
      const rows = await countRes.json();
      count = Array.isArray(rows) ? rows.length : 0;
    }

    return res.status(200).json({
      success: true,
      ref,
      count,
      bonusUnlocked: count >= 1
    });
  } catch (err) {
    console.error('Referral stats error:', err);
    return res.status(200).json({ success: false, ref, count: 0, error: err.message });
  }
}
