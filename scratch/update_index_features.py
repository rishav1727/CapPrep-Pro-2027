import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navbar buttons
navbar_old = """    <li><button id="nav-signin-btn" class="nav-signin-btn" onclick="handleNavAuthClick()" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#fff; padding:0.4rem 0.85rem; border-radius:6px; font-size:0.8rem; font-weight:600; cursor:pointer; margin-right:0.35rem;">🔑 Sign In</button></li>
    <li><button id="nav-pro-btn" class="nav-pro-badge" onclick="handleNavProClick()">⚡ Upgrade to Pro (₹51)</button></li>
    <!-- Dynamic Admin Control link (Only visible when registered administrator signs in) -->
    <li id="nav-admin-link-item" style="display:none;"><a href="admin.html" style="color:#fbbf24; font-size:0.8rem; font-weight:800; text-decoration:none; padding:0.35rem 0.65rem; border:1px solid rgba(245,158,11,0.4); border-radius:6px; background:rgba(245,158,11,0.15);">👑 Admin Panel</a></li>"""

navbar_new = """    <li><button id="nav-signin-btn" class="nav-signin-btn" onclick="openSignInModal()" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#fff; padding:0.4rem 0.85rem; border-radius:6px; font-size:0.8rem; font-weight:600; cursor:pointer;">🔑 Sign In</button></li>
    <li id="nav-user-item" style="display:none;"><span id="nav-user-pill" style="font-size:0.8rem; color:#a5b4fc; font-weight:700; background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.3); padding:0.35rem 0.75rem; border-radius:6px; display:inline-flex; align-items:center; gap:0.4rem;"><span id="nav-user-name">👤 User</span></span></li>
    <li id="nav-logout-item" style="display:none;"><button id="nav-logout-btn" onclick="userSignOut()" style="background:rgba(239,68,68,0.15); color:#f87171; border:1px solid rgba(239,68,68,0.4); border-radius:6px; padding:0.35rem 0.75rem; font-weight:700; cursor:pointer; font-size:0.8rem;">🚪 Logout</button></li>
    <li><button id="nav-pro-btn" class="nav-pro-badge" onclick="handleNavProClick()">⚡ Upgrade to Pro (₹51)</button></li>
    <!-- Dynamic Admin Control link (Only visible when registered administrator signs in) -->
    <li id="nav-admin-link-item" style="display:none;"><a href="admin.html" style="color:#fbbf24; font-size:0.8rem; font-weight:800; text-decoration:none; padding:0.35rem 0.65rem; border:1px solid rgba(245,158,11,0.4); border-radius:6px; background:rgba(245,158,11,0.15);">👑 Admin Panel</a></li>"""

if navbar_old in html:
    html = html.replace(navbar_old, navbar_new)
    print("Updated Navbar with explicit user pill and logout button")

# 2. Add show/hide password toggle to cust-password-input
cust_pass_old = """      <div style="margin-bottom:0.75rem;">
        <input type="password" id="cust-password-input" class="customer-input" placeholder="Create Account Password (min 6 characters for future sign-in)" required />
        <div style="font-size:0.72rem; color:#94a3b8; margin-top:0.25rem;">🔒 You will use this password to sign back in anytime from any device.</div>
      </div>"""

cust_pass_new = """      <div style="margin-bottom:0.75rem;">
        <div style="position:relative; display:flex; align-items:center;">
          <input type="password" id="cust-password-input" class="customer-input" style="padding-right:45px; width:100%;" placeholder="Create Account Password (min 6 characters for future sign-in)" required />
          <button type="button" onclick="togglePasswordVisibility('cust-password-input', this)" style="position:absolute; right:10px; background:none; border:none; color:#94a3b8; cursor:pointer; font-size:1.1rem; padding:4px;" title="Show/Hide Password" aria-label="Toggle password visibility">👁️</button>
        </div>
        <div style="font-size:0.72rem; color:#94a3b8; margin-top:0.25rem;">🔒 You will use this password to sign back in anytime from any device.</div>
      </div>"""

if cust_pass_old in html:
    html = html.replace(cust_pass_old, cust_pass_new)
    print("Updated cust-password-input with show password toggle")

# 3. Add show/hide password toggle to signin-password-input
signin_pass_old = """      <div style="margin-bottom:0.75rem;">
        <label style="font-size:0.78rem; font-weight:600; color:#cbd5e1; display:block; margin-bottom:0.3rem;">Password</label>
        <input type="password" id="signin-password-input" class="customer-input" placeholder="Enter your account password" onkeydown="if(event.key==='Enter') processUserSignIn()" />
      </div>"""

signin_pass_new = """      <div style="margin-bottom:0.75rem;">
        <label style="font-size:0.78rem; font-weight:600; color:#cbd5e1; display:block; margin-bottom:0.3rem;">Password</label>
        <div style="position:relative; display:flex; align-items:center;">
          <input type="password" id="signin-password-input" class="customer-input" style="padding-right:45px; width:100%;" placeholder="Enter your account password" onkeydown="if(event.key==='Enter') processUserSignIn()" />
          <button type="button" onclick="togglePasswordVisibility('signin-password-input', this)" style="position:absolute; right:10px; background:none; border:none; color:#94a3b8; cursor:pointer; font-size:1.1rem; padding:4px;" title="Show/Hide Password" aria-label="Toggle password visibility">👁️</button>
        </div>
      </div>"""

if signin_pass_old in html:
    html = html.replace(signin_pass_old, signin_pass_new)
    print("Updated signin-password-input with show password toggle")

# 4. Enhance Grand Mock section with Live Stage 2 Choice Banner & Stage-Wise Grand Mocks
grand_mock_old_header = """    <div class="section-header fade-in">
      <div class="section-badge">Full Assessment Suite</div>
      <h2 class="section-title">🏆 10 Grand Mock Marathons (All Stages Combined)</h2>
      <p class="section-desc">Full-length replicas simulating the complete Stage 2 and mixed assessment pattern in one continuous sitting.</p>
    </div>"""

grand_mock_new_header = """    <div class="section-header fade-in">
      <div class="section-badge">Full Assessment Suite</div>
      <h2 class="section-title">🏆 Grand Mock Marathons & Stage-Wise Simulations</h2>
      <p class="section-desc">Full-length replicas simulating the complete Stage 2 and mixed assessment patterns in continuous proctored sittings.</p>
    </div>

    <!-- Candidate Choice Banner: Stage 2 Live Focus vs Complete All Stages -->
    <div class="gm-choice-banner fade-in">
      <div class="gm-choice-header">
        <div>
          <span class="gm-live-badge">🔴 STAGE 2 ASSESSMENT DRIVE IS LIVE</span>
          <h3 style="color:#fff; font-size:1.1rem; margin-top:0.4rem;">Choose Your Grand Mock Testing Pattern:</h3>
        </div>
      </div>
      <div class="gm-toggle-container">
        <button class="gm-toggle-btn active" id="btn-mode-stage2" onclick="setGrandMockMode('stage2_only')">
          ⚡ Skip Stage 1 (Focus on Live Stage 2A to 6 Drive)
        </button>
        <button class="gm-toggle-btn" id="btn-mode-allstages" onclick="setGrandMockMode('all_stages')">
          🌐 Include Stage 1 (Full 6 Stages with English Communication)
        </button>
      </div>
      <div id="gm-mode-desc" style="font-size:0.85rem; color:#cbd5e1; line-height:1.5;">
        ⚡ <strong>Currently Active Pattern:</strong> Stage 2A + 2B + 3 + 4 + 5/6 (Stage 1 English Communication skipped as Stage 2 is currently live).
      </div>
    </div>

    <!-- STAGE-WISE GRAND MOCKS SUB-SECTION -->
    <div style="margin-bottom:2rem;" class="fade-in">
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.6rem;">
        <h3 style="font-size:1.15rem; color:#fff; display:flex; align-items:center; gap:0.5rem;">
          <span>🎯</span> Dedicated Stage-Wise Grand Mocks
        </h3>
        <span style="font-size:0.75rem; color:var(--text-muted);">One Grand Comprehensive Exam Per Recruitment Stage</span>
      </div>
      <div class="grid-3" style="gap:1rem;">
        <div class="test-card" onclick="startTest('gm_s1')">
          <div class="test-header"><div class="test-icon">🎙️</div><span class="test-difficulty diff-medium">Medium</span></div>
          <div class="test-title">Stage 1 Grand Mock — Verbal & English</div>
          <div class="test-meta">Grammar + Reading + Voice + Jumbles + Idioms</div>
          <div class="test-stats"><div class="ts-item"><div class="ts-val">25</div>Questions</div><div class="ts-item"><div class="ts-val">25</div>Minutes</div></div>
        </div>
        <div class="test-card" onclick="startTest('gm_s2a')">
          <div class="test-header"><div class="test-icon">💻</div><span class="test-difficulty diff-hard">Hard</span></div>
          <div class="test-title">Stage 2A Grand Mock — Technical & Coding</div>
          <div class="test-meta">AI Literacy + Pseudocode + DSA + Core CS</div>
          <div class="test-stats"><div class="ts-item"><div class="ts-val">30</div>Questions</div><div class="ts-item"><div class="ts-val">35</div>Minutes</div></div>
        </div>
        <div class="test-card" onclick="startTest('gm_s2b')">
          <div class="test-header"><div class="test-icon">🐛</div><span class="test-difficulty diff-hard">Hard</span></div>
          <div class="test-title">Stage 2B Grand Mock — Debugging Marathon</div>
          <div class="test-meta">Algorithmic bugs in Trees, Graphs, DP, Pointers</div>
          <div class="test-stats"><div class="ts-item"><div class="ts-val">15</div>Questions</div><div class="ts-item"><div class="ts-val">25</div>Minutes</div></div>
        </div>
        <div class="test-card" onclick="startTest('gm_s3')">
          <div class="test-header"><div class="test-icon">🤖</div><span class="test-difficulty diff-hard">Hard</span></div>
          <div class="test-title">Stage 3 Grand Mock — AI-Assisted Coding</div>
          <div class="test-meta">Prompt Quality + Edge Cases + Lab 27 Rubrics</div>
          <div class="test-stats"><div class="ts-item"><div class="ts-val">15</div>Questions</div><div class="ts-item"><div class="ts-val">20</div>Minutes</div></div>
        </div>
        <div class="test-card" onclick="startTest('gm_s4')">
          <div class="test-header"><div class="test-icon">🧠</div><span class="test-difficulty diff-medium">Medium</span></div>
          <div class="test-title">Stage 4 Grand Mock — Cognitive & ADEPT-15</div>
          <div class="test-meta">Motion + Grid Memory + Situational Judgment</div>
          <div class="test-stats"><div class="ts-item"><div class="ts-val">20</div>Questions</div><div class="ts-item"><div class="ts-val">25</div>Minutes</div></div>
        </div>
        <div class="test-card" onclick="startTest('gm_s56')">
          <div class="test-header"><div class="test-icon">🏆</div><span class="test-difficulty diff-hard">Hard</span></div>
          <div class="test-title">Stages 5 & 6 Grand Mock — Tech & HR Defense</div>
          <div class="test-meta">Architecture + Security + STAR Stories + 7 Values</div>
          <div class="test-stats"><div class="ts-item"><div class="ts-val">15</div>Questions</div><div class="ts-item"><div class="ts-val">20</div>Minutes</div></div>
        </div>
      </div>
    </div>

    <!-- ALL-STAGES COMBINED MEGA MOCKS SUB-SECTION -->
    <div style="margin-bottom:1rem;" class="fade-in">
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:0.6rem;">
        <h3 style="font-size:1.15rem; color:#fff; display:flex; align-items:center; gap:0.5rem;">
          <span>⚡</span> Full Multi-Stage Combined Mega Mocks
        </h3>
        <span style="font-size:0.75rem; color:var(--text-muted);">Tests 1 & 2 Available for Free Trial</span>
      </div>
    </div>"""

if grand_mock_old_header in html:
    html = html.replace(grand_mock_old_header, grand_mock_new_header)
    print("Updated Grand Mock header with Live Stage 2 Choice Banner and Stage-Wise Grand Mocks")

# Update test-card descriptions for full_1 and full_2
full_1_old = """      <div class="test-card" onclick="startTest('full_1')">
        <div class="test-header"><div class="test-icon">🎯</div><span class="test-difficulty diff-medium">Medium</span></div>
        <div class="test-title">Full Mock Test 1 — Complete Pattern</div>
        <div class="test-meta">All modules • 7 Topics • Full Stage 2A Replica</div>
        <div class="test-stats"><div class="ts-item"><div class="ts-val">35</div>Questions</div><div class="ts-item"><div class="ts-val">45</div>Minutes</div></div>
      </div>"""

full_1_new = """      <div class="test-card" onclick="startTest('full_1')">
        <div class="test-header"><div class="test-icon">🎯</div><span class="test-difficulty diff-medium">Medium</span></div>
        <div class="test-title">Full Mock Test 1 — Main Assessment Drive (Stages 2A to 6)</div>
        <div class="test-meta">Stage 2 Live Pattern (Stage 1 Skipped) • 42 Questions</div>
        <div class="test-stats"><div class="ts-item"><div class="ts-val">42</div>Questions</div><div class="ts-item"><div class="ts-val">45</div>Minutes</div></div>
      </div>"""

full_2_old = """      <div class="test-card" onclick="startTest('full_2')">
        <div class="test-header"><div class="test-icon">🚀</div><span class="test-difficulty diff-hard">Hard</span></div>
        <div class="test-title">Full Mock Test 2 — Advanced Technical</div>
        <div class="test-meta">Heavy DSA + DBMS + AI Literacy focus</div>
        <div class="test-stats"><div class="ts-item"><div class="ts-val">35</div>Questions</div><div class="ts-item"><div class="ts-val">45</div>Minutes</div></div>
      </div>"""

full_2_new = """      <div class="test-card" onclick="startTest('full_2')">
        <div class="test-header"><div class="test-icon">🚀</div><span class="test-difficulty diff-hard">Hard</span></div>
        <div class="test-title">Full Mock Test 2 — All Stages Complete Marathon (Stage 1 Included)</div>
        <div class="test-meta">Full 6 Stages with English Communication • 50 Questions</div>
        <div class="test-stats"><div class="ts-item"><div class="ts-val">50</div>Questions</div><div class="ts-item"><div class="ts-val">55</div>Minutes</div></div>
      </div>"""

if full_1_old in html:
    html = html.replace(full_1_old, full_1_new)
    print("Updated full_1 card title and meta")

if full_2_old in html:
    html = html.replace(full_2_old, full_2_new)
    print("Updated full_2 card title and meta")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
