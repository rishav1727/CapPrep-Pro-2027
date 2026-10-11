// api/verify-payment.js
// Vercel Serverless Function — verifies a Razorpay payment signature.
// Environment variables required:
//   RAZORPAY_KEY_SECRET — your Razorpay Key Secret
//
// How it works:
//   Razorpay sends razorpay_payment_id + razorpay_order_id + razorpay_signature
//   We HMAC-SHA256 sign (order_id + "|" + payment_id) with the secret and compare.
//   Only a valid Razorpay server-generated signature can pass this check.

import crypto from 'crypto';

export default function handler(req, res) {
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
    console.error('RAZORPAY_KEY_SECRET is not set!');
    return res.status(500).json({ error: 'Server configuration error.' });
  }

  // Generate expected signature
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
  // Payment is GENUINE.
  // Here you can:
  //   1. Write the user record to a database (Firebase, Supabase, PlanetScale…)
  //   2. Send a confirmation email (Resend, SendGrid, Nodemailer…)
  //   3. Return success — the frontend will unlock Pro in localStorage.
  //
  // For now we return the verified data to the frontend, which then activates
  // the Pro account in localStorage + shows the confirmation screen.
  // -----------------------------------------------------------------------

  console.log(`✅ Payment verified | Order: ${razorpay_order_id} | Payment: ${razorpay_payment_id}`);
  if (customerData) {
    console.log(`   Student: ${customerData.name} <${customerData.email}>`);
  }

  return res.status(200).json({
    success:    true,
    payment_id: razorpay_payment_id,
    order_id:   razorpay_order_id,
    message:    'Payment verified. Pro access activated.',
  });
}
