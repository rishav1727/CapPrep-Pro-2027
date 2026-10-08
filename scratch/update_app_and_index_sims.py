import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Stage 2B update in index.html
old_stage2b_grid = '''        <div class="test-grid-10">
          <button class="test-pill-btn" onclick="startTest('dbg_1')"><span>🐛 Test 1: Tree Recursion</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_2')"><span>🕸️ Test 2: Graph Cycles</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_3')"><span>🧮 Test 3: 2D DP Bounds</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_4')"><span>🔍 Test 4: NULL Pointers</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_5')"><span>💾 Test 5: Memory Leaks</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_6')"><span>🔄 Test 6: Loop Errors</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_7')"><span>🧩 Test 7: Swap By-Value</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_8')"><span>🔤 Test 8: String Null Term</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_9')"><span>🔗 Test 9: Linked List Jumps</span><span class="tp-tag tag-orange">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_10')"><span>🎖️ Test 10: Stage 2B Full Mock</span><span class="tp-tag tag-green">12Q</span></button>
        </div>'''

new_stage2b_grid = '''        <div class="test-grid-10">
          <button class="test-pill-btn" onclick="startTest('dbg_1')"><span>🐛 Test 1: Knapsack-C (Aon)</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_2')"><span>🌳 Test 2: Tree Max Path</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_3')"><span>🕸️ Test 3: Graph Cycles</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_4')"><span>🧮 Test 4: 2D Grid DP</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_5')"><span>🔗 Test 5: List Cycle & Traps</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_6')"><span>🔍 Test 6: Binary Search Bounds</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_7')"><span>🔤 Test 7: String Palindrome</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_8')"><span>🧩 Test 8: Pointer Swaps</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_9')"><span>💾 Test 9: Double Free Fix</span><span class="tp-tag tag-orange">Code</span></button>
          <button class="test-pill-btn" onclick="startTest('dbg_10')"><span>🎖️ Test 10: LIS DP Marathon</span><span class="tp-tag tag-green">Code</span></button>
        </div>'''

# Stage 3 update in index.html
old_stage3_grid = '''        <div class="test-grid-10">
          <button class="test-pill-btn" onclick="startTest('aic_1')"><span>💡 Test 1: Prompt Quality</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_2')"><span>🔄 Test 2: Review & Adapt</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_3')"><span>🛡️ Test 3: Edge Cases</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_4')"><span>⚡ Test 4: Complexity Directives</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_5')"><span>🌳 Test 5: Tree/Graph Prompts</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_6')"><span>🎯 Test 6: Iterative Refinement</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_7')"><span>🧠 Test 7: Zero vs Few-Shot</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_8')"><span>📐 Test 8: Struct Framing</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_9')"><span>📋 Test 9: Capgemini Rubrics</span><span class="tp-tag tag-green">10Q</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_10')"><span>🌟 Test 10: Stage 3 Grand Mock</span><span class="tp-tag tag-purple">10Q</span></button>
        </div>'''

new_stage3_grid = '''        <div class="test-grid-10">
          <button class="test-pill-btn" onclick="startTest('aic_1')"><span>💡 Test 1: LCM of 2 Trees (Aon)</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_2')"><span>🔄 Test 2: Reverse Linked List</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_3')"><span>🛡️ Test 3: Longest Substring</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_4')"><span>⚡ Test 4: LCA in Binary Tree</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_5')"><span>🌳 Test 5: Course Schedule DAG</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_6')"><span>🎯 Test 6: Merge K Sorted Lists</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_7')"><span>🧠 Test 7: Subarray Sum = K</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_8')"><span>📐 Test 8: Coin Change DP</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_9')"><span>📋 Test 9: Valid Parentheses *</span><span class="tp-tag tag-green">Vibe Code</span></button>
          <button class="test-pill-btn" onclick="startTest('aic_10')"><span>🌟 Test 10: Word Search 2D</span><span class="tp-tag tag-purple">Vibe Code</span></button>
        </div>'''

html = html.replace(old_stage2b_grid, new_stage2b_grid)
html = html.replace(old_stage3_grid, new_stage3_grid)

# Update stage headers / desc to emphasize NO MCQs (Hands-on)
html = html.replace('<h2 class="section-title">🐛 Stage 2B: Debugging Assessment (10 Tests + Simulator)</h2>',
                    '<h2 class="section-title">🐛 Stage 2B: Debugging Assessment (10 Hands-On Code Challenges — No MCQs)</h2>')
html = html.replace('<h2 class="section-title">💡 Stage 3: AI-Assisted Coding (10 Tests + Simulator)</h2>',
                    '<h2 class="section-title">💡 Stage 3: AI-Assisted Coding (10 Interactive Challenges — No MCQs)</h2>')

html = html.replace('<div style="font-weight:700; font-size:0.88rem; color:#fff; margin-bottom:0.5rem;">🐛 Stage 2B Dedicated Practice Tests (10 Tests):</div>',
                    '<div style="font-weight:700; font-size:0.88rem; color:#fff; margin-bottom:0.5rem;">🐛 Stage 2B Dedicated Hands-On Debug Tests (10 Challenges — Direct Code Fixing):</div>')

html = html.replace('<div style="font-weight:700; font-size:0.88rem; color:#fff; margin-bottom:0.5rem;">💡 Stage 3 Dedicated Prompt & Strategy Tests (10 Tests):</div>',
                    '<div style="font-weight:700; font-size:0.88rem; color:#fff; margin-bottom:0.5rem;">💡 Stage 3 Dedicated AI-Assisted Coding Tests (10 Scaffolding Vibe Coding Challenges):</div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")

# 2. Update js/app.js
with open('js/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Update startTest in app.js
old_start_test = '''function startTest(testId) {
  const test = MOCK_TESTS.find(t => t.id === testId);
  if (!test) {
    showSecurityToast("Test configuration not found: " + testId);
    return;
  }

  // Payment Wall Guard: Only Test 1 (vb_1) is free! All other tests require Pro
  if (test.isPremium && !isProUser()) {
    openLockedTestModal(test);
    return;
  }

  currentTest = test;'''

new_start_test = '''function startTest(testId) {
  const test = MOCK_TESTS.find(t => t.id === testId);
  if (!test) {
    showSecurityToast("Test configuration not found: " + testId);
    return;
  }

  // Payment Wall Guard
  if (test.isPremium && !isProUser()) {
    openLockedTestModal(test);
    return;
  }

  // Route Stage 2B Debugging Tests directly to Hands-On Debugging Simulator (No MCQs)
  if (testId.startsWith('dbg_') || testId === 'gm_s2b') {
    window.location.href = 'modules/debug_sim.html?id=' + testId;
    return;
  }

  // Route Stage 3 AI-Assisted Coding Tests directly to Hands-On AI Coding Simulator (No MCQs)
  if (testId.startsWith('aic_') || testId === 'gm_s3') {
    window.location.href = 'modules/ai_coding_sim.html?id=' + testId;
    return;
  }

  currentTest = test;'''

app_js = app_js.replace(old_start_test, new_start_test)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Updated js/app.js successfully!")
