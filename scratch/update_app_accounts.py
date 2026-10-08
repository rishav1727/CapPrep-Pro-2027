# -*- coding: utf-8 -*-
"""
Update C:\cap\ai\js\app.js with full user authentication, signin/signup,
account-based Pro access, locked test modal triggers, and updated payment handlers.
"""

path = r"C:\cap\ai\js\app.js"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace isProUser and payment engine helpers
old_engine_start = """const ADMIN_NOTIFICATION_EMAIL = "rishavofficials1727@gmail.com";
let currentPayablePrice = 51;
let flashTimerInterval = null;
let socialProofInterval = null;

function isProUser() {
  return localStorage.getItem('capprep_pro_unlocked') === 'true';
}"""

new_engine_start = """const ADMIN_NOTIFICATION_EMAIL = "rishavofficials1727@gmail.com";
let currentPayablePrice = 51;
let flashTimerInterval = null;
let socialProofInterval = null;

// ==========================================
// USER ACCOUNTS & AUTHENTICATION ENGINE
// ==========================================

function getStoredUsers() {
  try {
    return JSON.parse(localStorage.getItem('capprep_users') || '[]');
  } catch(e) {
    return [];
  }
}

function saveStoredUsers(users) {
  localStorage.setItem('capprep_users', JSON.stringify(users));
}

function getCurrentUser() {
  try {
    return JSON.parse(localStorage.getItem('capprep_current_user') || 'null');
  } catch(e) {
    return null;
  }
}

function setCurrentUser(user) {
  if (user) {
    localStorage.setItem('capprep_current_user', JSON.stringify(user));
    if (user.isPro) {
      localStorage.setItem('capprep_pro_unlocked', 'true');
    } else {
      localStorage.removeItem('capprep_pro_unlocked');
    }
  } else {
    localStorage.removeItem('capprep_current_user');
    localStorage.removeItem('capprep_pro_unlocked');
  }
  updateProUI();
}

function isProUser() {
  const cur = getCurrentUser();
  if (cur && cur.isPro) return true;
  return localStorage.getItem('capprep_pro_unlocked') === 'true';
}

function openSignInModal() {
  closeLockedTestModal();
  closePaymentModal();
  const modal = document.getElementById('signin-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    const err = document.getElementById('signin-error-msg');
    if (err) err.style.display = 'none';
    setTimeout(() => document.getElementById('signin-email-input')?.focus(), 100);
  }
}

function closeSignInModal() {
  const modal = document.getElementById('signin-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function handleNavAuthClick() {
  const cur = getCurrentUser();
  if (cur) {
    if (confirm(`Logged in as ${cur.name} (${cur.email}).\\nDo you want to sign out?`)) {
      userSignOut();
    }
  } else {
    openSignInModal();
  }
}

function handleNavProClick() {
  if (isProUser()) {
    showSecurityToast("⭐ You have unlimited CapPrep Pro Lifetime access!");
  } else {
    openPaymentModal();
  }
}

function userSignOut() {
  setCurrentUser(null);
  showSecurityToast("👋 Signed out successfully. Reverted to Free tier (Test 1 available).");
}

function processUserSignIn() {
  const email = (document.getElementById('signin-email-input')?.value || '').trim().toLowerCase();
  const password = (document.getElementById('signin-password-input')?.value || '').trim();
  const errorEl = document.getElementById('signin-error-msg');

  if (!email || !password) {
    if (errorEl) {
      errorEl.style.display = 'block';
      errorEl.textContent = '⚠️ Please enter both email and password.';
    }
    return;
  }

  const users = getStoredUsers();
  const user = users.find(u => u.email.toLowerCase() === email && u.password === password);

  if (user) {
    setCurrentUser(user);
    closeSignInModal();
    if (user.isPro) {
      showSecurityToast(`⭐ Welcome back, ${user.name}! Your CapPrep Pro Pass is active.`);
      alert(`🎉 WELCOME BACK ${user.name.toUpperCase()}!\\n\\nYour CapPrep Pro Lifetime Pass is ACTIVE.\\nAll 76+ Mock Tests, Simulators, and Study Notes are unlocked!`);
    } else {
      showSecurityToast(`👤 Logged in as ${user.name} (Free Tier).`);
    }
  } else {
    if (errorEl) {
      errorEl.style.display = 'block';
      errorEl.textContent = '❌ Invalid email or password. If you haven\\'t enrolled yet, click "Enroll now for ₹51" below.';
    }
  }
}

function openLockedTestModal(test) {
  const modal = document.getElementById('locked-test-modal');
  if (!modal) {
    openPaymentModal(test);
    return;
  }
  document.getElementById('locked-modal-test-title').textContent = `🔒 ${test.title} is Locked`;
  document.getElementById('locked-modal-test-meta').textContent = `${test.category} • ${test.questions} Questions • ${test.duration} Minutes (Pro Tier)`;
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeLockedTestModal() {
  const modal = document.getElementById('locked-test-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}"""

if old_engine_start in code:
    code = code.replace(old_engine_start, new_engine_start)
    print("Replaced engine start with user authentication system")
else:
    print("Warning: old_engine_start not found directly")

# Update startTest to call openLockedTestModal
old_start_test = """  // Payment Wall Guard
  if (test.isPremium && !isProUser()) {
    openPaymentModal(test);
    return;
  }"""

new_start_test = """  // Payment Wall Guard: Only Test 1 (vb_1) is free! All other tests require Pro
  if (test.isPremium && !isProUser()) {
    openLockedTestModal(test);
    return;
  }"""

if old_start_test in code:
    code = code.replace(old_start_test, new_start_test)
    print("Updated startTest to use openLockedTestModal")

# Update processUpiPayment to read Password, register user, and enforce ₹51 payment
old_upi_func = """function processUpiPayment() {
  const name = (document.getElementById('cust-name-input')?.value || '').trim();
  const email = (document.getElementById('cust-email-input')?.value || '').trim();
  const phone = (document.getElementById('cust-phone-input')?.value || '').trim();
  const college = (document.getElementById('cust-college-input')?.value || '').trim();
  const utr = (document.getElementById('upi-utr-input')?.value || '').trim();

  if (!name) {
    alert("Please enter your Full Name.");
    document.getElementById('cust-name-input')?.focus();
    return;
  }
  if (!email || !email.includes('@')) {
    alert("Please enter a valid Email Address (where your Pro Pass will be dispatched).");
    document.getElementById('cust-email-input')?.focus();
    return;
  }
  if (!utr || utr.length < 8) {
    alert("Please enter a valid 12-digit UPI UTR / Transaction Reference number after paying ₹51 in your UPI app.");
    document.getElementById('upi-utr-input')?.focus();
    return;
  }

  const btn = event.target;
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `⏳ Verifying ₹${currentPayablePrice} UPI Payment...`;
  }

  setTimeout(() => {
    completeOrderActivation({
      name,
      email,
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      method: "UPI Direct (0% Fee)",
      utr: utr,
      amount: currentPayablePrice
    });
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `⚡ Verify & Unlock Pro`;
    }
  }, 1000);
}"""

new_upi_func = """function processUpiPayment() {
  const name = (document.getElementById('cust-name-input')?.value || '').trim();
  const email = (document.getElementById('cust-email-input')?.value || '').trim().toLowerCase();
  const password = (document.getElementById('cust-password-input')?.value || '').trim();
  const phone = (document.getElementById('cust-phone-input')?.value || '').trim();
  const college = (document.getElementById('cust-college-input')?.value || '').trim();
  const utr = (document.getElementById('upi-utr-input')?.value || '').trim();

  if (!name) {
    alert("⚠️ Please enter your Full Name.");
    document.getElementById('cust-name-input')?.focus();
    return;
  }
  if (!email || !email.includes('@')) {
    alert("⚠️ Please enter a valid Email Address (will be your login ID).");
    document.getElementById('cust-email-input')?.focus();
    return;
  }
  if (!password || password.length < 6) {
    alert("⚠️ Please create an Account Password of at least 6 characters so you can sign back in anytime!");
    document.getElementById('cust-password-input')?.focus();
    return;
  }
  if (!utr || utr.length < 8) {
    alert("⚠️ Please enter the 12-digit UPI UTR / Transaction Reference number after paying ₹51 to rishavofficials1727@oksbi in your UPI app.");
    document.getElementById('upi-utr-input')?.focus();
    return;
  }

  const btn = event.target;
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `⏳ Verifying ₹${currentPayablePrice} UPI Payment & Registering Account...`;
  }

  setTimeout(() => {
    // 1. Register / Update user account with password
    const users = getStoredUsers();
    const existingIdx = users.findIndex(u => u.email.toLowerCase() === email);
    const userObj = {
      name: name,
      email: email,
      password: password, // user's private password
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      isPro: true,
      joinedAt: new Date().toLocaleString()
    };

    if (existingIdx >= 0) {
      users[existingIdx] = userObj;
    } else {
      users.unshift(userObj);
    }
    saveStoredUsers(users);
    setCurrentUser(userObj);

    // 2. Complete order activation and dispatch admin alert
    completeOrderActivation({
      name,
      email,
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      method: "UPI Direct (rishavofficials1727@oksbi)",
      utr: utr,
      amount: currentPayablePrice
    });

    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `⚡ Verify & Unlock Pro`;
    }
  }, 1000);
}"""

if old_upi_func in code:
    code = code.replace(old_upi_func, new_upi_func)
    print("Updated processUpiPayment with user account registration")
else:
    print("Warning: old_upi_func not found directly")

# Update updateProUI to handle navbar signin button and user profile
old_update_ui = """function updateProUI() {
  const isPro = isProUser();
  const proBadgeNav = document.getElementById('nav-pro-btn');
  if (proBadgeNav) {
    if (isPro) {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.innerHTML = `⭐ PRO ACTIVATED`;
      proBadgeNav.onclick = () => showSecurityToast("⭐ You have unlimited CapPrep Pro Lifetime access!");
    } else {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.style.background = 'linear-gradient(135deg, #00d4ff, #7c3aed)';
      proBadgeNav.innerHTML = `⚡ Upgrade to Pro (₹51)`;
      proBadgeNav.onclick = () => openPaymentModal();
    }
  }

  // Update lock badges on test cards
  document.querySelectorAll('.test-pill-btn, .test-card').forEach(el => {
    const onclickAttr = el.getAttribute('onclick') || '';
    const match = onclickAttr.match(/startTest\('([^']+)'\)/);
    if (match) {
      const testId = match[1];
      const test = MOCK_TESTS.find(t => t.id === testId);
      if (test && test.isPremium) {
        let lockEl = el.querySelector('.premium-lock-badge');
        if (isPro) {
          if (lockEl) lockEl.remove();
          el.classList.remove('locked');
        } else {
          if (!lockEl) {
            const badge = document.createElement('span');
            badge.className = 'premium-lock-badge';
            badge.innerHTML = `🔒 PRO`;
            const tpTag = el.querySelector('.tp-tag, .test-difficulty');
            if (tpTag) tpTag.parentNode.insertBefore(badge, tpTag);
          }
          el.classList.add('locked');
        }
      }
    }
  });
}"""

new_update_ui = """function updateProUI() {
  const isPro = isProUser();
  const cur = getCurrentUser();

  // 1. Update Navbar Pro Badge
  const proBadgeNav = document.getElementById('nav-pro-btn');
  if (proBadgeNav) {
    if (isPro) {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.style.background = 'linear-gradient(135deg, #06d6a0, #059669)';
      proBadgeNav.innerHTML = `⭐ PRO ACTIVE`;
      proBadgeNav.onclick = () => showSecurityToast("⭐ Your CapPrep Pro Lifetime Pass is Active! All 76+ tests are unlocked.");
    } else {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.style.background = 'linear-gradient(135deg, #00d4ff, #7c3aed)';
      proBadgeNav.innerHTML = `⚡ Upgrade to Pro (₹51)`;
      proBadgeNav.onclick = () => openPaymentModal();
    }
  }

  // 2. Update Navbar Sign In / Account Button
  const signinBtn = document.getElementById('nav-signin-btn');
  if (signinBtn) {
    if (cur) {
      signinBtn.innerHTML = `👤 ${escHTML(cur.name.split(' ')[0])} <span style="font-size:0.7rem; color:#f87171;">(Sign Out)</span>`;
      signinBtn.title = `Logged in as ${cur.email}. Click to Sign Out.`;
    } else {
      signinBtn.innerHTML = `🔑 Sign In`;
      signinBtn.title = `Sign into your CapPrep account`;
    }
  }

  // 3. Update lock badges on test cards (vb_1 is free; all others locked if !isPro)
  document.querySelectorAll('.test-pill-btn, .test-card').forEach(el => {
    const onclickAttr = el.getAttribute('onclick') || '';
    const match = onclickAttr.match(/startTest\('([^']+)'\)/);
    if (match) {
      const testId = match[1];
      const test = MOCK_TESTS.find(t => t.id === testId);
      if (test && test.isPremium) {
        let lockEl = el.querySelector('.premium-lock-badge');
        if (isPro) {
          if (lockEl) lockEl.remove();
          el.classList.remove('locked');
        } else {
          if (!lockEl) {
            const badge = document.createElement('span');
            badge.className = 'premium-lock-badge';
            badge.innerHTML = `🔒 PRO`;
            const tpTag = el.querySelector('.tp-tag, .test-difficulty');
            if (tpTag) tpTag.parentNode.insertBefore(badge, tpTag);
          }
          el.classList.add('locked');
        }
      } else if (test && !test.isPremium) {
        // Test 1 free badge
        let lockEl = el.querySelector('.premium-lock-badge');
        if (lockEl) lockEl.remove();
        el.classList.remove('locked');
      }
    }
  });
}"""

if old_update_ui in code:
    code = code.replace(old_update_ui, new_update_ui)
    print("Updated updateProUI with account status handling")
else:
    print("Warning: old_update_ui not found directly")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated app.js")
