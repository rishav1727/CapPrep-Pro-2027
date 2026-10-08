import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_dbg_aic_tests = '''  // ==========================================
  // STAGE 2B: DEBUGGING ASSESSMENT (10 TESTS)
  // ==========================================
  { id:"dbg_1", title:"Debugging Test 1 — Tree Recursion Bugs", category:"Stage 2B Debugging", bank:"debugging", icon:"🐛", difficulty:"hard", questions:10, duration:18, isPremium:false },
  { id:"dbg_2", title:"Debugging Test 2 — Graph Visited State Bugs", category:"Stage 2B Debugging", bank:"debugging", icon:"🕸️", difficulty:"hard", questions:10, duration:18, isPremium:false },
  { id:"dbg_3", title:"Debugging Test 3 — 2D DP Boundary Bugs", category:"Stage 2B Debugging", bank:"debugging", icon:"🧮", difficulty:"hard", questions:10, duration:18, isPremium:true },
  { id:"dbg_4", title:"Debugging Test 4 — Pointer & NULL Traps", category:"Stage 2B Debugging", bank:"debugging", icon:"🔍", difficulty:"hard", questions:10, duration:15, isPremium:true },
  { id:"dbg_5", title:"Debugging Test 5 — Memory Leak & Arrays", category:"Stage 2B Debugging", bank:"debugging", icon:"💾", difficulty:"hard", questions:10, duration:15, isPremium:true },
  { id:"dbg_6", title:"Debugging Test 6 — Loop Condition Errors", category:"Stage 2B Debugging", bank:"debugging", icon:"🔄", difficulty:"medium", questions:10, duration:15, isPremium:true },
  { id:"dbg_7", title:"Debugging Test 7 — Pass-by-Value Swap Bugs", category:"Stage 2B Debugging", bank:"debugging", icon:"🧩", difficulty:"medium", questions:10, duration:15, isPremium:true },
  { id:"dbg_8", title:"Debugging Test 8 — String Null-Terminator Bugs", category:"Stage 2B Debugging", bank:"debugging", icon:"🔤", difficulty:"medium", questions:10, duration:15, isPremium:true },
  { id:"dbg_9", title:"Debugging Test 9 — Linked List Pointer Jumps", category:"Stage 2B Debugging", bank:"debugging", icon:"🔗", difficulty:"hard", questions:10, duration:15, isPremium:true },
  { id:"dbg_10", title:"Debugging Test 10 — Stage 2B Full Mock", category:"Stage 2B Debugging", bank:"debugging", icon:"🎖️", difficulty:"hard", questions:12, duration:20, isPremium:true },

  // ==========================================
  // STAGE 3: AI-ASSISTED CODING (10 TESTS)
  // ==========================================
  { id:"aic_1", title:"AI Coding Test 1 — Prompt Quality Strategy", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"💡", difficulty:"medium", questions:10, duration:12, isPremium:false },
  { id:"aic_2", title:"AI Coding Test 2 — Review & Adapt Code", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"🔄", difficulty:"medium", questions:10, duration:12, isPremium:false },
  { id:"aic_3", title:"AI Coding Test 3 — Edge Case Directives", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"🛡️", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"aic_4", title:"AI Coding Test 4 — Time Complexity Prompts", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"⚡", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"aic_5", title:"AI Coding Test 5 — Tree & Graph Framing", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"🌳", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"aic_6", title:"AI Coding Test 6 — Iterative Refinement", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"🎯", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"aic_7", title:"AI Coding Test 7 — Zero-Shot vs Few-Shot", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"🧠", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"aic_8", title:"AI Coding Test 8 — Struct & Pointer Prompts", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"📐", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"aic_9", title:"AI Coding Test 9 — Capgemini Rubrics Test", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"📋", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"aic_10", title:"AI Coding Test 10 — Stage 3 Grand Mock", category:"Stage 3 AI Coding", bank:"ai_coding", icon:"🌟", difficulty:"hard", questions:10, duration:15, isPremium:true },'''

new_dbg_aic_tests = '''  // ==========================================
  // STAGE 2B: DEBUGGING ASSESSMENT (10 HANDS-ON TESTS — NO MCQS)
  // ==========================================
  { id:"dbg_1", title:"Debugging Challenge 1 — 01. Knapsack-C (Aon Replica)", category:"Stage 2B Debugging", icon:"🐛", difficulty:"hard", questions:1, duration:20, isPremium:false },
  { id:"dbg_2", title:"Debugging Challenge 2 — 02. Binary Tree Max Path Sum", category:"Stage 2B Debugging", icon:"🌳", difficulty:"hard", questions:1, duration:20, isPremium:false },
  { id:"dbg_3", title:"Debugging Challenge 3 — 03. Graph Cycle in DAG (Java)", category:"Stage 2B Debugging", icon:"🕸️", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_4", title:"Debugging Challenge 4 — 04. 2D DP Grid Obstacles (C)", category:"Stage 2B Debugging", icon:"🧮", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_5", title:"Debugging Challenge 5 — 05. List Cycle Traps (C++)", category:"Stage 2B Debugging", icon:"🔗", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_6", title:"Debugging Challenge 6 — 06. Binary Search Overflow", category:"Stage 2B Debugging", icon:"🔍", difficulty:"medium", questions:1, duration:20, isPremium:true },
  { id:"dbg_7", title:"Debugging Challenge 7 — 07. String Palindrome & '\\0'", category:"Stage 2B Debugging", icon:"🔤", difficulty:"medium", questions:1, duration:20, isPremium:true },
  { id:"dbg_8", title:"Debugging Challenge 8 — 08. Pass-by-Reference & Swaps", category:"Stage 2B Debugging", icon:"🧩", difficulty:"medium", questions:1, duration:20, isPremium:true },
  { id:"dbg_9", title:"Debugging Challenge 9 — 09. Double Free & Dangling Pointer", category:"Stage 2B Debugging", icon:"💾", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_10", title:"Debugging Challenge 10 — 10. Longest Increasing Subsequence DP", category:"Stage 2B Debugging", icon:"🎖️", difficulty:"hard", questions:1, duration:20, isPremium:true },

  // ==========================================
  // STAGE 3: AI-ASSISTED CODING (10 HANDS-ON CHALLENGES — NO MCQS)
  // ==========================================
  { id:"aic_1", title:"AI Coding Challenge 1 — 01. LCM of Two Trees (Official Capgemini)", category:"Stage 3 AI Coding", icon:"💡", difficulty:"medium", questions:1, duration:45, isPremium:false },
  { id:"aic_2", title:"AI Coding Challenge 2 — 02. In-Place Reversal of Linked List", category:"Stage 3 AI Coding", icon:"🔄", difficulty:"medium", questions:1, duration:45, isPremium:false },
  { id:"aic_3", title:"AI Coding Challenge 3 — 03. Longest Substring Without Repeating", category:"Stage 3 AI Coding", icon:"🛡️", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_4", title:"AI Coding Challenge 4 — 04. Lowest Common Ancestor (LCA)", category:"Stage 3 AI Coding", icon:"⚡", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_5", title:"AI Coding Challenge 5 — 05. Course Schedule / DAG Cycle", category:"Stage 3 AI Coding", icon:"🌳", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_6", title:"AI Coding Challenge 6 — 06. Merge K Sorted Linked Lists", category:"Stage 3 AI Coding", icon:"🎯", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_7", title:"AI Coding Challenge 7 — 07. Subarray Sum Equals K", category:"Stage 3 AI Coding", icon:"🧠", difficulty:"medium", questions:1, duration:45, isPremium:true },
  { id:"aic_8", title:"AI Coding Challenge 8 — 08. Coin Change (Minimum Coins DP)", category:"Stage 3 AI Coding", icon:"📐", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_9", title:"AI Coding Challenge 9 — 09. Valid Parentheses with Wildcards", category:"Stage 3 AI Coding", icon:"📋", difficulty:"medium", questions:1, duration:45, isPremium:true },
  { id:"aic_10", title:"AI Coding Challenge 10 — 10. Word Search on 2D Matrix", category:"Stage 3 AI Coding", icon:"🌟", difficulty:"hard", questions:1, duration:45, isPremium:true },'''

text = text.replace(old_dbg_aic_tests, new_dbg_aic_tests)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated MOCK_TESTS in js/app.js successfully!")
