// api/save-user.js
// Vercel Serverless Function — securely saves/updates a user and password in Supabase.

const SUPABASE_URL = process.env.SUPABASE_URL || "https://ynayovthgrlysfogleqo.supabase.co";
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InluYXlvdnRoZ3JseXNmb2dsZXFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE2MTg4NzYsImV4cCI6MjEwNzE5NDg3Nn0.NkHNeS6FTzshLmETxaSEravCBA9ner9gjyKvcUZK4Qs";

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  const { name, email, password, phone, college, isPro } = req.body || {};

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required.' });
  }

  const cleanEmail = email.trim().toLowerCase();
  const payload = {
    email: cleanEmail,
    name: name || "CapPrep Student",
    password: password,
    phone: phone || "+91 98000 00000",
    college: college || "Capgemini Candidate",
    is_pro: isPro ?? true,
    is_vip: false,
  };

  try {
    const dbRes = await fetch(`${SUPABASE_URL}/rest/v1/capprep_users`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "apikey": SUPABASE_ANON_KEY,
        "Authorization": `Bearer ${SUPABASE_ANON_KEY}`,
        "Prefer": "resolution=merge-duplicates"
      },
      body: JSON.stringify(payload)
    });

    if (dbRes.ok) {
      return res.status(200).json({ success: true, message: 'User saved to Supabase.' });
    } else {
      const errText = await dbRes.text();
      console.warn('Supabase save error:', errText);
      return res.status(500).json({ error: 'Database save failed', details: errText });
    }
  } catch(err) {
    console.error('Supabase network error:', err);
    return res.status(500).json({ error: 'Database connection error' });
  }
}
