import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Define free test IDs (exactly 2 per stage + grand mock)
FREE_TEST_IDS = {
    'vb_1', 'vb_2',      # Stage 1
    'ai_1', 'ai_2',      # Stage 2A
    'dbg_1', 'dbg_2',    # Stage 2B
    'aic_1', 'aic_2',    # Stage 3
    'sit_1', 'sit_2',    # Stage 4
    'int_1', 'int_2',    # Stages 5-6
    'full_1', 'full_2'   # Grand Mocks
}

# Update isPremium for every test in MOCK_TESTS
def update_mock_tests(text):
    # Regex to find test entries
    def replace_test(match):
        t_id = match.group(1)
        body = match.group(0)
        is_free = t_id in FREE_TEST_IDS
        new_prem = f"isPremium:{'false' if is_free else 'true'}"
        body = re.sub(r'isPremium\s*:\s*(true|false)', new_prem, body)
        return body

    updated = re.sub(r'\{\s*id\s*:\s*"([^"]+)"[^}]+isPremium\s*:\s*(true|false)[^}]*\}', replace_test, text)
    return updated

code = update_mock_tests(code)

# Ensure full_1 is Stage 2A-6 (Stage 1 Skipped) and full_2 is All Stages (Stage 1 Included)
full_1_repl = """  { id:"full_1", title:"Full Mock Test 1 — Main Assessment Drive (Stages 2A to 6)", category:"Grand Mocks", icon:"🎯", difficulty:"medium", questions:42, duration:45, isPremium:false, spec:[{bank:"ai_literacy",n:5},{bank:"pseudocode",n:5},{bank:"dsa",n:5},{bank:"dbms",n:4},{bank:"oops",n:4},{bank:"os",n:4},{bank:"debugging",n:5},{bank:"ai_coding",n:5},{bank:"situational",n:5}] },"""
full_2_repl = """  { id:"full_2", title:"Full Mock Test 2 — All Stages Complete Marathon (Stage 1 Included)", category:"Grand Mocks", icon:"🚀", difficulty:"hard", questions:50, duration:55, isPremium:false, spec:[{bank:"verbal",n:8},{bank:"ai_literacy",n:5},{bank:"pseudocode",n:5},{bank:"dsa",n:5},{bank:"dbms",n:4},{bank:"oops",n:4},{bank:"debugging",n:5},{bank:"ai_coding",n:5},{bank:"situational",n:5},{bank:"interview",n:4}] },"""

code = re.sub(r'\{\s*id:"full_1".*?\},', full_1_repl, code)
code = re.sub(r'\{\s*id:"full_2".*?\},', full_2_repl, code)

# Check if stage-wise grand mocks exist in MOCK_TESTS, if not add them
stage_wise_mocks = """
  // ==========================================
  // STAGE-WISE GRAND MOCKS
  // ==========================================
  { id:"gm_s1", title:"Stage 1 Grand Mock — English Communication", category:"Stage-Wise Grand Mocks", bank:"verbal", icon:"🎙️", difficulty:"medium", questions:25, duration:25, isPremium:true },
  { id:"gm_s2a", title:"Stage 2A Grand Mock — Technical Assessment", category:"Stage-Wise Grand Mocks", icon:"💻", difficulty:"hard", questions:30, duration:35, isPremium:true, spec:[{bank:"ai_literacy",n:5},{bank:"pseudocode",n:5},{bank:"dsa",n:5},{bank:"dbms",n:4},{bank:"oops",n:4},{bank:"os",n:4},{bank:"networks",n:3}] },
  { id:"gm_s2b", title:"Stage 2B Grand Mock — Debugging Marathon", category:"Stage-Wise Grand Mocks", bank:"debugging", icon:"🐛", difficulty:"hard", questions:15, duration:25, isPremium:true },
  { id:"gm_s3", title:"Stage 3 Grand Mock — AI-Assisted Coding Assessment", category:"Stage-Wise Grand Mocks", bank:"ai_coding", icon:"🤖", difficulty:"hard", questions:15, duration:20, isPremium:true },
  { id:"gm_s4", title:"Stage 4 Grand Mock — Cognitive Games & ADEPT-15", category:"Stage-Wise Grand Mocks", bank:"situational", icon:"🧠", difficulty:"medium", questions:20, duration:25, isPremium:true },
  { id:"gm_s56", title:"Stages 5 & 6 Grand Mock — Tech Defense & HR Values", category:"Stage-Wise Grand Mocks", bank:"interview", icon:"🏆", difficulty:"hard", questions:15, duration:20, isPremium:true },
"""

if 'id:"gm_s1"' not in code:
    code = code.replace('// GRAND MOCK MARATHON SUITE (10 FULL TESTS - PRO TIER)', stage_wise_mocks + '\n  // GRAND MOCK MARATHON SUITE (10 FULL TESTS)')
    print("Added Stage-Wise Grand Mocks to MOCK_TESTS")

# Add togglePasswordVisibility and setGrandMockMode helper
helper_funcs = """
// Show / Hide Password Helper
function togglePasswordVisibility(inputId, btn) {
  const input = document.getElementById(inputId);
  if (!input) return;
  if (input.type === 'password') {
    input.type = 'text';
    if (btn) btn.innerHTML = '🙈';
    if (btn) btn.title = 'Hide Password';
  } else {
    input.type = 'password';
    if (btn) btn.innerHTML = '👁️';
    if (btn) btn.title = 'Show Password';
  }
}

// Grand Mock Mode Switcher (Stage 2 Focus vs All Stages with Stage 1)
let grandMockMode = 'stage2_only';
function setGrandMockMode(mode) {
  grandMockMode = mode;
  const btnStage2 = document.getElementById('btn-mode-stage2');
  const btnAll = document.getElementById('btn-mode-allstages');
  const descEl = document.getElementById('gm-mode-desc');
  
  if (mode === 'stage2_only') {
    if (btnStage2) btnStage2.classList.add('active');
    if (btnAll) btnAll.classList.remove('active');
    if (descEl) descEl.innerHTML = '⚡ <strong>Currently Active Pattern:</strong> Stage 2A + 2B + 3 + 4 + 5/6 (Stage 1 English Communication skipped as Stage 2 is live).';
    showSecurityToast("⚡ Grand Mock pattern set to: Stages 2A to 6 (Stage 1 skipped).");
  } else {
    if (btnStage2) btnStage2.classList.remove('active');
    if (btnAll) btnAll.classList.add('active');
    if (descEl) descEl.innerHTML = '🌐 <strong>Currently Active Pattern:</strong> Full 6 Stages (Stage 1 English Communication + Stages 2A to 6 included).';
    showSecurityToast("🌐 Grand Mock pattern set to: Complete 6 Stages (Stage 1 included).");
  }
}
"""

if 'function togglePasswordVisibility' not in code:
    code = helper_funcs + "\n" + code

# Update updateProUI() and userSignOut()
new_update_pro_ui = """function userSignOut() {
  setCurrentUser(null);
  localStorage.removeItem('capprep_pro_unlocked');
  localStorage.removeItem('capprep_txn_id');
  updateProUI();
  showSecurityToast("👋 Signed out successfully. Reverted to Free Tier (2 Free Trials per Stage).");
}

function updateProUI() {
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

  // 2. Update Navbar Sign In / User Pill / Logout Buttons & Dynamic Admin Link
  const signinBtn = document.getElementById('nav-signin-btn');
  const userItem = document.getElementById('nav-user-item');
  const userNameEl = document.getElementById('nav-user-name');
  const logoutItem = document.getElementById('nav-logout-item');
  const adminNavItem = document.getElementById('nav-admin-link-item');
  
  if (cur) {
    const isMasterAdmin = MASTER_ADMIN_EMAILS.includes((cur.email || '').toLowerCase());
    if (adminNavItem) {
      adminNavItem.style.display = isMasterAdmin ? 'inline-block' : 'none';
    }
    if (signinBtn) signinBtn.style.display = 'none';
    if (userItem) {
      userItem.style.display = 'inline-block';
      if (userNameEl) {
        const badge = isMasterAdmin ? '👑 Admin' : '👤 ' + escHTML(cur.name.split(' ')[0]);
        userNameEl.innerHTML = badge;
      }
    }
    if (logoutItem) logoutItem.style.display = 'inline-block';
  } else {
    if (adminNavItem) adminNavItem.style.display = 'none';
    if (userItem) userItem.style.display = 'none';
    if (logoutItem) logoutItem.style.display = 'none';
    if (signinBtn) {
      signinBtn.style.display = 'inline-block';
      signinBtn.innerHTML = `🔑 Sign In`;
    }
  }

  // 3. Update lock badges on test pills and cards
  // Rule: 2 Free Tests per Stage; all others strictly LOCKED unless isPro
  document.querySelectorAll('.test-pill-btn, .test-card').forEach(el => {
    const onclickAttr = el.getAttribute('onclick') || '';
    const match = onclickAttr.match(/startTest\('([^']+)'\)/);
    if (!match) return;

    const testId = match[1];
    const test = MOCK_TESTS.find(t => t.id === testId);
    if (!test) return;

    // Clean existing badges
    const existingLock = el.querySelector('.test-lock-pill, .premium-lock-badge');
    const existingFree = el.querySelector('.test-free-pill');

    if (test.isPremium) {
      if (isPro) {
        if (existingLock) existingLock.remove();
        el.classList.remove('locked');
      } else {
        if (!existingLock) {
          const lockPill = document.createElement('span');
          lockPill.className = 'test-lock-pill';
          lockPill.innerHTML = `🔒 LOCKED`;
          const tpTag = el.querySelector('.tp-tag, .test-difficulty, .test-meta');
          if (tpTag) {
            tpTag.parentNode.insertBefore(lockPill, tpTag);
          } else {
            el.appendChild(lockPill);
          }
        }
        if (existingFree) existingFree.remove();
        el.classList.add('locked');
      }
    } else {
      // Free Trial Test (2 tests per stage)
      if (existingLock) existingLock.remove();
      el.classList.remove('locked');
      if (!isPro && !existingFree) {
        const freePill = document.createElement('span');
        freePill.className = 'test-free-pill';
        freePill.innerHTML = `🟢 FREE TRIAL`;
        const tpTag = el.querySelector('.tp-tag, .test-difficulty, .test-meta');
        if (tpTag) {
          tpTag.parentNode.insertBefore(freePill, tpTag);
        } else {
          el.appendChild(freePill);
        }
      } else if (isPro && existingFree) {
        existingFree.remove();
      }
    }
  });
}"""

# Replace existing userSignOut and updateProUI
code = re.sub(r'function userSignOut\(\)\s*\{.*?function updateProUI\(\)\s*\{.*?\n\}', new_update_pro_ui, code, flags=re.DOTALL)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated js/app.js with 2 free tests per stage, prominent lock badges, and logout flow!")
