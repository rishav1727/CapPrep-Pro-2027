// api/create-order.js
// Vercel Serverless Function — creates a Razorpay order on the backend.
// Environment variables required (set in Vercel Dashboard → Settings → Environment Variables):
//   RAZORPAY_KEY_ID     — your Razorpay Key ID  (rzp_test_… or rzp_live_…)
//   RAZORPAY_KEY_SECRET — your Razorpay Key Secret

import Razorpay from 'razorpay';

const razorpay = new Razorpay({
  key_id:     process.env.RAZORPAY_KEY_ID,
  key_secret: process.env.RAZORPAY_KEY_SECRET,
});

export default async function handler(req, res) {
  // Allow CORS from your own domain (update in production)
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const { amount, currency = 'INR', receipt } = req.body || {};

    // Validate amount (must be a positive integer in paise: ₹51 = 5100)
    const amountPaise = parseInt(amount, 10);
    if (!amountPaise || amountPaise < 100) {
      return res.status(400).json({ error: 'Invalid amount. Must be >= ₹1 (100 paise).' });
    }

    const order = await razorpay.orders.create({
      amount:   amountPaise,          // in paise
      currency: currency,
      receipt:  receipt || `rcpt_${Date.now()}`,
      notes: {
        source: 'CapPrep Pro Payment',
      },
    });

    return res.status(200).json({
      id:       order.id,
      amount:   order.amount,
      currency: order.currency,
    });
  } catch (err) {
    console.error('Razorpay create-order error:', err);
    return res.status(500).json({ error: 'Failed to create payment order. Please try again.' });
  }
}
