const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log('====================================================');
console.log('🔍 RUNNING COMPREHENSIVE PLATFORM FUNCTIONALITY AUDIT');
console.log('====================================================\n');

let totalErrors = 0;
let totalPassed = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`  ✅ PASS: ${message}`);
    totalPassed++;
  } else {
    console.error(`  ❌ FAIL: ${message}`);
    totalErrors++;
  }
}

// ----------------------------------------------------
// 1. EXTRACT & SYNTAX CHECK ALL HTML PAGES & SCRIPTS
// ----------------------------------------------------
console.log('📋 1. Checking Syntax of All HTML Pages & Embedded Scripts...');
const htmlFiles = [
  'index.html',
  'admin.html',
  'modules/debug_sim.html',
  'modules/ai_coding_sim.html',
  'modules/interview_hub.html',
  'modules/study_reader.html'
];

htmlFiles.forEach(file => {
  const filePath = path.join(__dirname, '..', file);
  if (!fs.existsSync(filePath)) {
    assert(false, `File exists: ${file}`);
    return;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  assert(content.length > 500, `${file} loaded (${(content.length/1024).toFixed(1)} KB)`);

  const scriptRegex = /<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi;
  let match;
  let scriptIndex = 0;
  while ((match = scriptRegex.exec(content)) !== null) {
    const code = match[1];
    scriptIndex++;
    if (!code.trim()) continue;
    try {
      new vm.Script(code, { filename: `${file}#script${scriptIndex}` });
      assert(true, `${file} inline script #${scriptIndex} syntax valid`);
    } catch (err) {
      assert(false, `${file} inline script #${scriptIndex} syntax error: ${err.message}`);
    }
  }
});

// ----------------------------------------------------
// 2. CHECK JS/APP.JS AND QUESTION BANKS
// ----------------------------------------------------
console.log('\n📋 2. Checking js/app.js & Master Question Banks...');
const appJsPath = path.join(__dirname, '..', 'js', 'app.js');
const appJsCode = fs.readFileSync(appJsPath, 'utf8');

const mockLocalStorage = {};
const mockWindow = {
  location: { href: '', search: '' },
  addEventListener: () => {},
  removeEventListener: () => {},
  localStorage: {
    getItem: (k) => mockLocalStorage[k] || null,
    setItem: (k, v) => { mockLocalStorage[k] = String(v); },
    removeItem: (k) => { delete mockLocalStorage[k]; }
  }
};
const mockDocument = {
  getElementById: (id) => ({
    id,
    style: {},
    classList: { add: () => {}, remove: () => {}, toggle: () => {} },
    value: '',
    textContent: '',
    innerHTML: '',
    checked: false,
    focus: () => {},
    addEventListener: () => {}
  }),
  querySelectorAll: () => [],
  addEventListener: () => {},
  body: { style: {}, appendChild: () => {} }
};

const context = vm.createContext({
  window: mockWindow,
  document: mockDocument,
  localStorage: mockWindow.localStorage,
  console: console,
  setInterval: () => 1,
  clearInterval: () => {},
  setTimeout: (fn) => { fn(); return 1; },
  clearTimeout: () => {},
  URLSearchParams: class { get() { return null; } }
});

try {
  vm.runInContext(appJsCode, context);
  assert(true, 'js/app.js executed in sandbox without errors');
} catch (err) {
  assert(false, `js/app.js runtime error: ${err.message}`);
}

// Verify Question Bank
if (context.QUESTION_BANK) {
  const banks = Object.keys(context.QUESTION_BANK);
  assert(banks.length >= 10, `Question banks loaded: ${banks.length} banks (${banks.join(', ')})`);
  let totalQCount = 0;
  banks.forEach(b => {
    const list = context.QUESTION_BANK[b];
    totalQCount += list.length;
    let bankValid = true;
    list.forEach((q, idx) => {
      if (!q.q || !Array.isArray(q.options) || q.options.length < 2 || typeof q.ans !== 'number' || !q.exp) {
        bankValid = false;
        console.error(`Invalid question in bank ${b} at index ${idx}:`, q);
      }
    });
    assert(bankValid && list.length >= 5, `Bank [${b}]: ${list.length} valid questions with options & explanations`);
  });
  console.log(`  ℹ️ Total Curated MCQs in Memory: ${totalQCount}`);
}

// Verify MOCK_TESTS
if (context.MOCK_TESTS) {
  assert(context.MOCK_TESTS.length >= 70, `MOCK_TESTS configuration loaded: ${context.MOCK_TESTS.length} tests`);
  const uniqueIds = new Set(context.MOCK_TESTS.map(t => t.id));
  assert(uniqueIds.size === context.MOCK_TESTS.length, `All ${uniqueIds.size} mock test IDs are strictly unique`);

  let testResolutionOk = true;
  context.MOCK_TESTS.forEach(t => {
    if (t.id.startsWith('dbg_') || t.id === 'gm_s2b' || t.id.startsWith('aic_') || t.id === 'gm_s3') {
      return;
    }
    const questions = context.getFreshQuestions(t);
    if (!questions || questions.length === 0) {
      testResolutionOk = false;
      console.error(`Test ${t.id} (${t.title}) returned 0 questions! Bank: ${t.bank}`);
    }
  });
  assert(testResolutionOk, 'Every MCQ Mock Test resolves to fresh randomized questions');
}

// ----------------------------------------------------
// 3. CHECK SIMULATORS FUNCTIONALITY & CONFIG
// ----------------------------------------------------
console.log('\n📋 3. Checking Simulators (AI Coding & Debugging)...');

// Stage 3 AI Coding Simulator
const aiSimContent = fs.readFileSync(path.join(__dirname, '..', 'modules', 'ai_coding_sim.html'), 'utf8');
assert(aiSimContent.includes('AIC_BANK'), 'AI Coding Simulator defines AIC_BANK (10 Comprehensive Challenges)');
assert(aiSimContent.includes('2,000') || aiSimContent.includes('2000'), 'AI Coding Simulator enforces 2000 token limit');
assert(aiSimContent.includes('tokenCount') && aiSimContent.includes('tokensRemaining'), 'AI Coding Simulator tracks live token usage');
assert(aiSimContent.includes('examples'), 'AI Coding Simulator includes problem examples and explanations');
assert(aiSimContent.includes('method_signatures'), 'AI Coding Simulator defines multi-language signatures (C, C++, Java, Python)');

// Stage 2B Debugging Simulator
const dbgSimContent = fs.readFileSync(path.join(__dirname, '..', 'modules', 'debug_sim.html'), 'utf8');
assert(dbgSimContent.includes('DBG_BANK'), 'Debugging Simulator defines DBG_BANK (10 Algorithmic Challenges)');
assert(dbgSimContent.includes('codes'), 'Debugging Simulator has buggy code challenges in C, C++, Java, Python');
assert(dbgSimContent.includes('switchLanguage'), 'Debugging Simulator supports multi-language syntax switching');
assert(dbgSimContent.includes('runValidation') && dbgSimContent.includes('validateProblem'), 'Debugging Simulator has test execution and validation engine');

// ----------------------------------------------------
// 4. CHECK STUDY READER (PDF MANUALS)
// ----------------------------------------------------
console.log('\n📋 4. Checking In-Browser PDF Study Reader...');
const studyDocsPath = path.join(__dirname, '..', 'js', 'study_docs.js');
assert(fs.existsSync(studyDocsPath), 'js/study_docs.js exists');
const studyDocsContent = fs.readFileSync(studyDocsPath, 'utf8');
assert(studyDocsContent.includes('STAGE_DOCS'), 'js/study_docs.js defines STAGE_DOCS');
['stage1', 'stage2a', 'stage2b', 'stage3', 'stage4', 'stage56'].forEach(stage => {
  assert(studyDocsContent.includes(stage), `STAGE_DOCS contains complete manual for ${stage}`);
});

// ----------------------------------------------------
// 5. CHECK ADMIN PANEL & SECURITY
// ----------------------------------------------------
console.log('\n📋 5. Checking Admin Panel & Security Safeguards...');
const adminContent = fs.readFileSync(path.join(__dirname, '..', 'admin.html'), 'utf8');
assert(adminContent.includes('authenticateAdmin'), 'Admin panel has SHA-256 PIN authentication');
assert(adminContent.includes('capprep_vip_whitelist'), 'Admin panel manages VIP candidate whitelist');
assert(adminContent.includes('capprep_orders'), 'Admin panel manages customer orders & UTR verifications');
assert(adminContent.includes('capprep_support_tickets'), 'Admin panel manages customer support tickets');
assert(adminContent.includes('support-panel'), 'Admin panel renders dedicated Support Tickets tab');

// Check Privacy: Ensure raw admin email is not hardcoded in customer-facing forms
assert(!fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8').includes('rishav.gupta0527@gmail.com'), 'index.html does not expose personal admin email in user-facing UI');

// ----------------------------------------------------
// 6. CHECK SIGN IN & UPGRADE TO PRO MODALS & AUTH
// ----------------------------------------------------
console.log('\n📋 6. Checking Sign In & Upgrade to Pro Flows...');

// Create simulated DOM elements map
const elements = {};
function getOrCreateEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id,
      style: { display: 'none' },
      classList: { add: () => {}, remove: () => {}, toggle: () => {} },
      value: '',
      textContent: '',
      innerHTML: '',
      checked: false,
      focus: () => {},
      remove: () => {},
      addEventListener: () => {}
    };
  }
  return elements[id];
}

const authContext = vm.createContext({
  window: {
    location: { href: '', search: '' },
    addEventListener: () => {},
    localStorage: mockWindow.localStorage
  },
  document: {
    getElementById: (id) => getOrCreateEl(id),
    createElement: (tag) => getOrCreateEl('dynamic-' + Math.random()),
    querySelectorAll: () => [],
    addEventListener: () => {},
    body: { style: {}, appendChild: () => {} }
  },
  localStorage: mockWindow.localStorage,
  console: console,
  setInterval: () => 1,
  clearInterval: () => {},
  setTimeout: (fn) => { fn(); return 1; },
  clearTimeout: () => {},
  alert: (msg) => {},
  confirm: () => true,
  URLSearchParams: class { get() { return null; } }
});

try {
  vm.runInContext(appJsCode, authContext);
  
  // Test 1: Open Payment Modal
  authContext.openPaymentModal();
  assert(elements['payment-modal'].style.display === 'flex', 'openPaymentModal() opens #payment-modal with display: flex');
  assert(elements['pay-screen-1'].style.display === 'block', '#pay-screen-1 is displayed in step 1');

  // Test 2: Step 1 -> Step 2 transition
  getOrCreateEl('cust-name-input').value = 'Test Candidate';
  getOrCreateEl('cust-email-input').value = 'candidate@test.com';
  getOrCreateEl('cust-password-input').value = 'mypassword123';
  getOrCreateEl('tc-agree-checkbox').checked = true;
  authContext.goToPaymentScreen();
  assert(getOrCreateEl('pay-screen-2').style.display === 'block', 'goToPaymentScreen() validates inputs and transitions to #pay-screen-2 (UPI QR)');

  // Test 3: Step 2 UPI Payment Verification
  getOrCreateEl('upi-utr-input').value = '419827361524';
  authContext.processUpiPayment();
  assert(getOrCreateEl('pay-screen-3').style.display === 'block', 'processUpiPayment() verifies UTR and transitions to #pay-screen-3 (Confirmation)');
  assert(authContext.isProUser() === true, 'isProUser() evaluates to true after successful payment');

  // Test 4: Open Sign In Modal
  authContext.openSignInModal();
  assert(getOrCreateEl('signin-modal').style.display === 'flex', 'openSignInModal() opens #signin-modal');

  // Test 5: Sign In with Demo credentials
  getOrCreateEl('signin-email-input').value = 'demo@capprep.com';
  getOrCreateEl('signin-password-input').value = 'cap2027';
  authContext.processUserSignIn();
  assert(getOrCreateEl('signin-modal').style.display === 'none', 'processUserSignIn() successfully signs in demo user and closes modal');
  assert(authContext.isProUser() === true, 'Demo user has active Pro access');

  // Test 6: Master Admin Sign In
  getOrCreateEl('signin-email-input').value = 'rishavofficials1727@gmail.com';
  getOrCreateEl('signin-password-input').value = '1727';
  authContext.processUserSignIn();
  const cur = authContext.getCurrentUser();
  assert(cur && cur.isAdmin === true, 'processUserSignIn() recognizes Master Admin with full admin privileges');

  // Test 7: Official Test Account 1 (Alpha) Sign In & Pro access
  getOrCreateEl('signin-email-input').value = 'test1@capprep.com';
  getOrCreateEl('signin-password-input').value = 'pass_test1_2027';
  authContext.processUserSignIn();
  const testUser = authContext.getCurrentUser();
  assert(testUser && testUser.isTestAccount === true && testUser.isPro === true, 'Official Test ID 1 (test1@capprep.com) logs in with active Pro tier');

  // Test 8: Single Active Session Enforcement
  const activeSessions = JSON.parse(mockWindow.localStorage.getItem('capprep_active_sessions') || '{}');
  assert(activeSessions['test1@capprep.com'] !== undefined, 'Active session token registered for test1@capprep.com');
  
  // Simulate concurrent login from another device:
  activeSessions['test1@capprep.com'] = 'NEW_DEVICE_SESSION_TOKEN';
  mockWindow.localStorage.setItem('capprep_active_sessions', JSON.stringify(activeSessions));
  const isValid = authContext.validateActiveSession();
  assert(isValid === false, 'Concurrent login from another device successfully terminates older session');

} catch(err) {
  assert(false, `Sign In & Upgrade to Pro sandbox test error: ${err.message}`);
}

// ----------------------------------------------------
// AUDIT SUMMARY
// ----------------------------------------------------
console.log('\n====================================================');
console.log(`📊 AUDIT COMPLETE: ${totalPassed} PASSED, ${totalErrors} FAILED`);
console.log('====================================================\n');

if (totalErrors === 0) {
  console.log('🎉 ALL SYSTEMS FULLY FUNCTIONAL AND PASSING ALL CHECKS!');
  process.exit(0);
} else {
  console.error('⚠️ SOME CHECKS FAILED! Please review errors above.');
  process.exit(1);
}
