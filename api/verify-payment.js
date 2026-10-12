// api/verify-payment.js
// Vercel Serverless Function — verifies Razorpay payment signature
// AND permanently stores user account & password into Supabase cloud database.

import crypto from 'crypto';

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

  const {
    razorpay_order_id,
    razorpay_payment_id,
    razorpay_signature,
    customerData,   // { name, email, phone, college, password }
  } = req.body || {};

  if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
    return res.status(400).json({ error: 'Missing Razorpay payment fields.' });
  }

  const secret = process.env.RAZORPAY_KEY_SECRET;
  if (!secret) {
    console.error('RAZORPAY_KEY_SECRET is not set in Vercel!');
    return res.status(500).json({ error: 'Server configuration error: Key Secret not configured.' });
  }

  // Generate expected HMAC-SHA256 signature
  const body = razorpay_order_id + '|' + razorpay_payment_id;
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(body)
    .digest('hex');

  const isValid = crypto.timingSafeEqual(
    Buffer.from(expectedSignature, 'hex'),
    Buffer.from(razorpay_signature,  'hex')
  );

  if (!isValid) {
    return res.status(400).json({ success: false, error: 'Invalid payment signature. Possible fraud attempt.' });
  }

  // -----------------------------------------------------------------------
  // Payment is 100% GENUINE & CONFIRMED.
  // Save student account & password permanently to Supabase Cloud Database!
  // -----------------------------------------------------------------------
  let dbSaved = false;
  if (customerData && customerData.email) {
    const cleanEmail = customerData.email.trim().toLowerCase();
    const userPayload = {
      email: cleanEmail,
      name: customerData.name || "CapPrep Student",
      password: customerData.password,
      phone: customerData.phone || "+91 98000 00000",
      college: customerData.college || "Capgemini Candidate",
      is_pro: true,
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
        body: JSON.stringify(userPayload)
      });
      if (dbRes.ok) {
        dbSaved = true;
        console.log(`✅ Student account & password saved to Supabase: ${cleanEmail}`);
      } else {
        const errText = await dbRes.text();
        console.warn(`Supabase user save status: ${dbRes.status}`, errText);
      }
    } catch(dbErr) {
      console.error("Supabase user save network error:", dbErr);
    }

    // Save order in orders ledger
    try {
      await fetch(`${SUPABASE_URL}/rest/v1/capprep_orders`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "apikey": SUPABASE_ANON_KEY,
          "Authorization": `Bearer ${SUPABASE_ANON_KEY}`,
          "Prefer": "resolution=merge-duplicates"
        },
        body: JSON.stringify({
          order_id: razorpay_order_id,
          email: cleanEmail,
          name: customerData.name || "Enrolled Student",
          phone: customerData.phone || "+91 98000 00000",
          college: customerData.college || "Capgemini Candidate",
          amount: 21,
          method: "Razorpay (Live Gateway)",
          utr: razorpay_payment_id,
          status: "VERIFIED_ACTIVE"
        })
      });
    } catch(orderErr) {
      console.warn("Supabase order save error:", orderErr);
    }

    // Server-side instant admin notification dispatch to testprep795@gmail.com
    try {
      const adminEmail = "testprep795@gmail.com";
      const studentName = customerData.name || "Enrolled Student";
      await fetch(`https://formsubmit.co/ajax/${encodeURIComponent(adminEmail)}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Origin": "https://capprep-pro-2027.vercel.app",
          "Referer": "https://capprep-pro-2027.vercel.app"
        },
        body: JSON.stringify({
          _subject: `💰 [NEW SALE] ₹21 Received from ${studentName} (Order #${razorpay_order_id})`,
          _template: "table",
          _captcha: "false",
          _replyto: cleanEmail,
          "Order ID": `#${razorpay_order_id}`,
          "Payment ID (Razorpay)": razorpay_payment_id,
          "Student Name": studentName,
          "Student Email": cleanEmail,
          "Mobile Phone": customerData.phone || "N/A",
          "College": customerData.college || "Capgemini Candidate",
          "Amount Paid": "₹21 INR (CapPrep Pro Lifetime)",
          "Status": "CONFIRMED & UNLOCKED",
          "Account Password": customerData.password || "N/A",
          "Admin Dashboard": "https://capprep-pro-2027.vercel.app/admin.html"
        })
      });
      console.log(`✅ Admin sale notification dispatched to ${adminEmail}`);
    } catch(mailErr) {
      console.warn("Admin server notification error:", mailErr);
    }
  }

  return res.status(200).json({
    success:    true,
    payment_id: razorpay_payment_id,
    order_id:   razorpay_order_id,
    db_saved:   dbSaved,
    message:    'Payment verified, credentials saved, and admin notified.',
  });
}
