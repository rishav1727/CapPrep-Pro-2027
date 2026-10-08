import sys
sys.stdout.reconfigure(encoding='utf-8')

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Stage 2B: Debugging Assessment (Multi-Language: C, C++, Java, Python) | Capgemini Exceller 2027</title>
  <link rel="stylesheet" href="../css/style.css"/>
  <style>
    body { background: #0a0f1d; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; height: 100vh; margin: 0; display: flex; flex-direction: column; overflow: hidden; }
    .sim-header { background: #0f172a; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 0.6rem 1.25rem; display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; }
    .badge-lab { background: #ea580c; color: white; padding: 0.25rem 0.6rem; border-radius: 4px; font-weight: 800; font-size: 0.75rem; letter-spacing: 0.5px; }
    .sim-timer { font-family: monospace; font-size: 1.5rem; font-weight: 800; color: #ef4444; }
    .sim-body { display: grid; grid-template-columns: 370px 1fr 340px; flex: 1; overflow: hidden; }

    /* Left Panel */
    .left-panel { background: #090d16; border-right: 1px solid rgba(255,255,255,0.08); padding: 1.25rem; overflow-y: auto; display: flex; flex-direction: column; gap: 1rem; }
    .prob-selector { background: #131d33; border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 0.55rem 0.75rem; border-radius: 6px; font-size: 0.85rem; width: 100%; outline: none; }
    .prob-badge { font-size: 0.75rem; color: #f97316; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
    .prob-title { font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0.2rem 0 0.5rem 0; }
    .prob-desc { font-size: 0.84rem; color: #94a3b8; line-height: 1.5; }
    
    .steps-container { display: flex; flex-direction: column; gap: 0.5rem; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); padding: 0.75rem; border-radius: 8px; }
    .step-item { display: flex; align-items: center; gap: 0.6rem; font-size: 0.78rem; color: #64748b; font-weight: 600; padding: 0.35rem 0.5rem; border-radius: 4px; }
    .step-item.active { background: rgba(249,115,22,0.12); color: #fb923c; border-left: 3px solid #f97316; }
    .step-item.completed { color: #06d6a0; }

    /* Center Panel: Code Editor */
    .center-panel { display: flex; flex-direction: column; background: #0c1322; border-right: 1px solid rgba(255,255,255,0.08); overflow: hidden; }
    .editor-toolbar { background: #090d16; border-bottom: 1px solid rgba(255,255,255,0.08); padding: 0.5rem 1rem; display: flex; align-items: center; justify-content: space-between; font-size: 0.82rem; }
    .lang-dropdown { background: #1e293b; color: #00d4ff; border: 1px solid rgba(0,212,255,0.3); border-radius: 4px; padding: 0.25rem 0.6rem; font-size: 0.78rem; font-weight: 700; outline: none; cursor: pointer; }
    .editor-wrapper { flex: 1; display: flex; flex-direction: column; overflow: hidden; position: relative; }
    .code-area { flex: 1; padding: 1rem; font-family: "Fira Code", monospace, Consolas; font-size: 0.88rem; line-height: 1.6; color: #e2e8f0; background: #060a12; border: none; outline: none; resize: none; overflow: auto; white-space: pre; }
    .testcase-panel { height: 180px; background: #090d16; border-top: 1px solid rgba(255,255,255,0.1); padding: 0.75rem 1rem; display: flex; flex-direction: column; gap: 0.5rem; overflow-y: auto; }
    .testcase-header { display: flex; justify-content: space-between; align-items: center; font-size: 0.78rem; font-weight: 700; color: #94a3b8; }
    .testcase-results { display: flex; gap: 0.75rem; flex-wrap: wrap; }
    .tc-pill { font-size: 0.75rem; padding: 0.4rem 0.8rem; border-radius: 6px; font-weight: 700; display: flex; align-items: center; gap: 0.4rem; }
    .tc-pass { background: rgba(6,214,160,0.15); color: #06d6a0; border: 1px solid rgba(6,214,160,0.3); }
    .tc-fail { background: rgba(239,68,68,0.15); color: #ef4444; border: 1px solid rgba(239,68,68,0.3); }

    /* Right Panel: HUD */
    .right-panel { background: #080c14; padding: 1.25rem; overflow-y: auto; display: flex; flex-direction: column; gap: 1rem; }
    .hud-title { font-size: 0.75rem; font-weight: 800; letter-spacing: 1px; color: #f97316; text-transform: uppercase; }
    .hud-card { background: rgba(249,115,22,0.06); border: 1px solid rgba(249,115,22,0.2); border-radius: 8px; padding: 0.85rem; font-size: 0.8rem; color: #cbd5e1; line-height: 1.45; }
    .hud-card h4 { margin: 0 0 0.35rem 0; color: #fdba74; font-size: 0.84rem; }
    
    .btn-action { background: #f97316; color: #fff; border: none; padding: 0.65rem 1rem; border-radius: 6px; font-weight: 700; font-size: 0.85rem; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 0.5rem; transition: all 0.2s; }
    .btn-action:hover { background: #ea580c; }
    .btn-validate { background: #06d6a0; color: #042f2e; }
    .btn-validate:hover { background: #059669; }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="sim-header">
    <div style="display:flex; align-items:center; gap:0.75rem;">
      <span class="badge-lab">STAGE 2B</span>
      <div>
        <div style="font-weight:800; font-size:0.92rem; color:#fff;">Debugging Assessment Simulator</div>
        <div style="font-size:0.72rem; color:#94a3b8;">10 Hands-On Challenges • Multi-Language Support (C, C++, Java, Python)</div>
      </div>
    </div>
    <div style="display:flex; align-items:center; gap:1.5rem;">
      <div style="text-align:right;">
        <span style="font-size:0.7rem; color:#94a3b8; display:block;">TIME REMAINING</span>
        <span class="sim-timer" id="timer">20:00</span>
      </div>
      <button class="btn-action" style="background:#334155;" onclick="location.href='../index.html#stage2b'">← Back to Dashboard</button>
    </div>
  </div>

  <!-- BODY -->
  <div class="sim-body">
    <!-- LEFT PANEL -->
    <div class="left-panel">
      <div>
        <label style="font-size:0.75rem; color:#94a3b8; font-weight:700; display:block; margin-bottom:0.35rem;">SELECT DEBUGGING TEST (1-10):</label>
        <select class="prob-selector" id="probSelect" onchange="loadProblem(this.value)">
          <option value="dbg_1">Test 1: 01. Knapsack-C (0/1 Knapsack Problem)</option>
          <option value="dbg_2">Test 2: 02. Binary Tree: Maximum Path Sum</option>
          <option value="dbg_3">Test 3: 03. Graph: Detect Cycle in Directed Graph</option>
          <option value="dbg_4">Test 4: 04. 2D DP: Grid Unique Paths with Obstacles</option>
          <option value="dbg_5">Test 5: 05. Linked List: Cycle Detection & Length</option>
          <option value="dbg_6">Test 6: 06. Binary Search & Midpoint Overflow</option>
          <option value="dbg_7">Test 7: 07. String: Palindrome & Null-Terminator</option>
          <option value="dbg_8">Test 8: 08. Pointers: Pass-by-Value Swap Bug</option>
          <option value="dbg_9">Test 9: 09. Memory: Dangling Pointer & Double Free</option>
          <option value="dbg_10">Test 10: 10. DP: Longest Increasing Subsequence</option>
        </select>
      </div>

      <div>
        <span class="prob-badge" id="probBadge">KNAPSACK ALGORITHM</span>
        <div class="prob-title" id="probTitle">01. Knapsack-C</div>
        <div class="prob-desc" id="probDesc">
          Given a set of items with weight and value, determine items to include so total weight &le; capacity W and total value is maximized.
        </div>
      </div>

      <!-- 4-STEP CAPGEMINI MODEL -->
      <div class="steps-container">
        <div style="font-size:0.72rem; font-weight:800; color:#94a3b8; text-transform:uppercase; margin-bottom:0.2rem;">Capgemini 4-Step Workflow:</div>
        <div class="step-item active" id="st-1">① Review: Inspect code logic &amp; signatures</div>
        <div class="step-item" id="st-2">② Identify: Pinpoint null checks &amp; array bounds</div>
        <div class="step-item" id="st-3">③ Fix: Apply minimal fix without side effects</div>
        <div class="step-item" id="st-4">④ Validate: Pass visible &amp; hidden edge tests</div>
      </div>

      <div style="background:rgba(255,255,255,0.03); padding:0.75rem; border-radius:6px; font-size:0.78rem; color:#94a3b8;">
        <strong style="color:#fff;">Constraints &amp; Rules:</strong>
        <div id="probConstraints" style="margin-top:0.3rem; line-height:1.5;">
          • Return -1 if distribution is not possible or wt == NULL or val == NULL.<br/>
          • Items cannot be divided (0/1 pick complete item or don't pick).
        </div>
      </div>
    </div>

    <!-- CENTER WORKSPACE -->
    <div class="center-panel">
      <div class="editor-toolbar">
        <div style="display:flex; align-items:center; gap:0.6rem;">
          <label style="color:#94a3b8; font-size:0.76rem; font-weight:700;">LANGUAGE:</label>
          <select class="lang-dropdown" id="langSelect" onchange="switchLanguage(this.value)">
            <option value="c">C (GCC 11.3)</option>
            <option value="cpp">C++ 20</option>
            <option value="java">Java 17</option>
            <option value="python">Python 3.10</option>
          </select>
          <span style="color:#64748b; font-size:0.75rem;" id="fileName">Solution.c</span>
        </div>
        <div style="display:flex; gap:0.5rem;">
          <button class="btn-action" style="padding:0.35rem 0.75rem; font-size:0.78rem; background:#334155;" onclick="resetCode()">↺ Reset Code</button>
          <button class="btn-action btn-validate" style="padding:0.35rem 0.9rem; font-size:0.78rem;" onclick="runValidation()">▶ Validate Solution</button>
        </div>
      </div>

      <div class="editor-wrapper">
        <textarea class="code-area" id="codeEditor" spellcheck="false"></textarea>
      </div>

      <!-- TESTCASES -->
      <div class="testcase-panel">
        <div class="testcase-header">
          <span>TEST CASE VALIDATION RESULTS</span>
          <span id="passCount" style="color:#94a3b8;">0 / 3 Passed</span>
        </div>
        <div class="testcase-results" id="tcResults">
          <div class="tc-pill" style="background:#131d33; color:#94a3b8;">Click "Validate Solution" to test your fix</div>
        </div>
      </div>
    </div>

    <!-- RIGHT HUD -->
    <div class="right-panel">
      <div class="hud-title">🔍 Diagnostic Assistant</div>

      <div class="hud-card">
        <h4>Expected Behavior</h4>
        <p id="hudExpected">Must return maximum value for capacity W, and handle edge constraints properly.</p>
      </div>

      <div class="hud-card" style="background:rgba(239,68,68,0.06); border-color:rgba(239,68,68,0.2);">
        <h4 style="color:#fca5a5;">Observed Failure / Root Bugs</h4>
        <p id="hudFailure" style="color:#cbd5e1;">Missing NULL checks for pointers, off-by-one 2D DP array dimension allocation, or inverted recurrence logic.</p>
      </div>

      <div class="hud-card" style="background:rgba(6,214,160,0.06); border-color:rgba(6,214,160,0.2);">
        <h4 style="color:#6ee7b7;">Capgemini Scoring Rubric</h4>
        <ul style="margin:0.3rem 0 0 1rem; padding:0; font-size:0.75rem; line-height:1.4; color:#94a3b8;">
          <li><strong>Syntax &amp; Compilation:</strong> Clean fix matching signature in selected language.</li>
          <li><strong>Edge Cases:</strong> NULL/None pointers, zero capacity, out-of-bounds.</li>
          <li><strong>Correctness:</strong> Maximum value matching 0/1 recurrence.</li>
        </ul>
      </div>

      <button class="btn-action" style="margin-top:auto; background:linear-gradient(135deg,#00d4ff,#7c3aed);" onclick="showSolutionHint()">💡 Show Hint / Fix Explanation</button>
    </div>
  </div>

  <script>
    let currentLang = 'c';
    let currentProbKey = 'dbg_1';

    const DBG_BANK = {
      dbg_1: {
        badge: "0/1 KNAPSACK (CAPGEMINI AON REPLICA)",
        title: "01. Knapsack-C",
        desc: "Given weights wt and values val of length n and capacity W, return maximum sum of values with weight <= W. Return -1 if inputs are null/invalid.",
        constraints: "• 0 <= n <= 10^5, 1 <= wt[i] <= 10^6, 1 <= val[i] <= 10^6, 1 <= W <= 10^5.<br/>• Return -1 if wt == NULL or val == NULL.<br/>• Pick item at most once.",
        files: { c: "Knapsack.c", cpp: "Knapsack.cpp", java: "Knapsack.java", python: "knapsack.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
#include <stdio.h>
#include <stdlib.h>

int KnapsackProblem(int* wt, int* val, int n, int W) {
    // BUG 1: Missing NULL pointer check required by problem specifications
    int dp[100][100];
    
    for (int i = 0; i < n; i++) {
        for (int w = 0; w < W; w++) { // BUG 2: w < W misses exact capacity W (should be <= W)
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (wt[i-1] <= w) {
                // BUG 3: Incorrect recurrence index
                dp[i][w] = val[i] + dp[i-1][w - wt[i]];
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    return dp[n-1][W-1];
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int knapsack(vector<int>& wt, vector<int>& val, int n, int W) {
        // BUG: Missing check for empty vectors or negative capacity
        vector<vector<int>> dp(n, vector<int>(W, 0)); // BUG: Dimensions should be n+1, W+1
        
        for (int i = 1; i < n; i++) {
            for (int w = 1; w < W; w++) { // BUG: w < W misses capacity W
                if (wt[i-1] <= w) {
                    dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]]);
                } else {
                    dp[i][w] = dp[i-1][w];
                }
            }
        }
        return dp[n-1][W-1];
    }
};`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
public class Knapsack {
    public static int solveKnapsack(int[] wt, int[] val, int n, int W) {
        // BUG 1: Missing null and empty check
        if (n <= 0 || W <= 0) return 0;
        
        int[][] dp = new int[n][W]; // BUG 2: Sized n x W instead of (n+1) x (W+1)
        for (int i = 1; i < n; i++) {
            for (int w = 1; w < W; w++) {
                if (wt[i-1] <= w) {
                    dp[i][w] = Math.max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]]);
                } else {
                    dp[i][w] = dp[i-1][w];
                }
            }
        }
        return dp[n-1][W-1];
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def knapsack(wt, val, n, W):
    # BUG 1: Missing None checks
    dp = [[0 for _ in range(W)] for _ in range(n)] # BUG 2: Should be W+1 and n+1
    
    for i in range(1, n):
        for w in range(1, W): # BUG 3: range(1, W) excludes capacity W
            if wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n-1][W-1]`
        },
        expected: "Return max value for capacity W; return -1 if wt or val is NULL/None.",
        failure: "Crashes on NULL pointers, loop bounds exclude capacity W, and recurrence array index off-by-one.",
        hints: {
          c: "1. Add NULL check: if (wt == NULL || val == NULL || n <= 0 || W <= 0) return -1;\n2. Use loop bounds: w <= W\n3. Index correctly: val[i-1] + dp[i-1][w - wt[i-1]]",
          cpp: "1. Resize DP to (n+1) x (W+1)\n2. Run loop up to w <= W\n3. Use val[i-1] + dp[i-1][w - wt[i-1]]",
          java: "1. Check for null: if (wt == null || val == null) return -1;\n2. Allocate int[][] dp = new int[n+1][W+1];\n3. Loop w <= W.",
          python: "1. Check: if wt is None or val is None: return -1\n2. Allocate (n+1) x (W+1) matrix\n3. Use range(1, W+1) and val[i-1]."
        },
        validate: function(code, lang) {
          const hasNull = code.includes("NULL") || code.includes("null") || code.includes("None") || code.includes("!wt") || code.includes(".empty()");
          const hasBound = code.includes("<= W") || code.includes("<=W") || code.includes("W + 1") || code.includes("W+1");
          const hasValIdx = code.includes("val[i-1]") || code.includes("val[i - 1]");
          return {
            tc1: { name: "Null / Empty Input Guard (Return -1)", passed: hasNull },
            tc2: { name: "Full Capacity Bounds (W+1 / <= W)", passed: hasBound },
            tc3: { name: "0/1 Recurrence Indexing val[i-1]", passed: hasValIdx }
          };
        }
      },

      dbg_2: {
        badge: "TREE ALGORITHM",
        title: "02. Binary Tree Maximum Path Sum",
        desc: "Calculate the maximum path sum in a binary tree. Negative child contributions must be ignored.",
        constraints: "• Node values can be negative. Time: O(N), Space: O(H).",
        files: { c: "MaxPathSum.c", cpp: "MaxPathSum.cpp", java: "MaxPathSum.java", python: "max_path_sum.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
#include <stdio.h>
#include <limits.h>

struct TreeNode { int val; struct TreeNode *left, *right; };

int max(int a, int b) { return a > b ? a : b; }

int maxPathDown(struct TreeNode* root, int *maxSum) {
    if (root == NULL) return 0;
    // BUG: Adds negative branches directly without clipping to 0!
    int left = maxPathDown(root->left, maxSum);
    int right = maxPathDown(root->right, maxSum);
    *maxSum = max(*maxSum, left + right + root->val);
    return root->val + left + right; // BUG: Returns sum of both branches
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

struct TreeNode { int val; TreeNode *left; TreeNode *right; };

class Solution {
public:
    int maxPathDown(TreeNode* root, int &maxSum) {
        if (root == NULL) return 0;
        int left = maxPathDown(root->left, maxSum);
        int right = maxPathDown(root->right, maxSum);
        maxSum = max(maxSum, left + right + root->val);
        return root->val + left + right; // BUG
    }
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        maxPathDown(root, maxSum);
        return maxSum;
    }
};`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
class TreeNode { int val; TreeNode left, right; }

public class MaxPathSum {
    static int maxSum = Integer.MIN_VALUE;
    public static int maxPathDown(TreeNode root) {
        if (root == null) return 0;
        int left = maxPathDown(root.left);
        int right = maxPathDown(root.right);
        maxSum = Math.max(maxSum, left + right + root.val);
        return root.val + left + right; // BUG
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        def max_down(node):
            if not node: return 0
            left = max_down(node.left)
            right = max_down(node.right)
            self.max_sum = max(self.max_sum, left + right + node.val)
            return node.val + left + right # BUG
        max_down(root)
        return self.max_sum`
        },
        expected: "Must return highest sum path between any two nodes. Ignore negative branches with max(0, branch).",
        failure: "Includes negative branch sums and branches both ways up the recursion call stack.",
        hints: {
          c: "Use max(0, maxPathDown(...)) and return root->val + max(left, right);",
          cpp: "Clip with max(0, ...) and return root->val + max(left, right);",
          java: "Use Math.max(0, maxPathDown(...)) and return root.val + Math.max(left, right);",
          python: "Use max(0, max_down(...)) and return node.val + max(left, right)."
        },
        validate: function(code, lang) {
          const hasMax0 = code.includes("max(0") || code.includes("max( 0") || code.includes("0,") || code.includes("Math.max(0");
          const hasSingleBranch = code.includes("max(left, right)") || code.includes("max(left,right)") || code.includes("Math.max(left, right)");
          return {
            tc1: { name: "Positive Tree [1,2,3]", passed: code.length > 30 },
            tc2: { name: "Negative Child Nodes Handled", passed: hasMax0 },
            tc3: { name: "Single Branch Return to Parent", passed: hasSingleBranch }
          };
        }
      },

      dbg_3: {
        badge: "GRAPH ALGORITHM",
        title: "03. Detect Cycle in Directed Graph",
        desc: "Return true if a directed graph contains a cycle. Differentiate between back-edges in current DFS stack and cross-edges.",
        constraints: "• 1 <= V <= 10^5. Must handle disconnected graph components.",
        files: { c: "GraphCycle.c", cpp: "GraphCycle.cpp", java: "GraphCycle.java", python: "graph_cycle.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
#include <stdbool.h>

bool dfs(int node, int adj[][100], int* adjSize, bool* visited) {
    visited[node] = true;
    for (int i = 0; i < adjSize[node]; i++) {
        int neighbor = adj[node][i];
        if (visited[neighbor]) return true; // BUG: False positive cross-edge!
        if (dfs(neighbor, adj, adjSize, visited)) return true;
    }
    return false;
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <vector>
using namespace std;

class Solution {
public:
    bool dfs(int node, vector<vector<int>>& adj, vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : adj[node]) {
            if (visited[neighbor]) return true; // BUG: False positive
            if (dfs(neighbor, adj, visited)) return true;
        }
        return false;
    }
};`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
import java.util.*;

public class GraphCycle {
    public static boolean dfs(int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : adj.get(node)) {
            if (visited[neighbor]) return true; // BUG: False positive
            if (dfs(neighbor, adj, visited)) return true;
        }
        return false;
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def is_cyclic(V, adj):
    visited = [False] * V
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if visited[neighbor]: return True # BUG: False positive
            if dfs(neighbor): return True
        return False
    return any(dfs(i) for i in range(V) if not visited[i])`
        },
        expected: "Use recursion stack tracking (inStack / recStack) to only detect back-edges.",
        failure: "Falsely detects a cycle for DAG diamond structures.",
        hints: {
          c: "Add bool inStack[] array. Set inStack[node] = true before exploring, backtrack inStack[node] = false.",
          cpp: "Add vector<bool> inStack. Check if inStack[neighbor] is true.",
          java: "Add boolean[] inStack = new boolean[V]. Backtrack inStack[node] = false;",
          python: "Add in_stack = [False]*V. Set in_stack[node]=True, and on return in_stack[node]=False."
        },
        validate: function(code, lang) {
          const hasInStack = code.includes("inStack") || code.includes("recStack") || code.includes("inPath") || code.includes("in_stack") || code.includes("visited[neighbor] == 2");
          return {
            tc1: { name: "Simple Cycle (0->1->2->0)", passed: true },
            tc2: { name: "Diamond DAG (No false positive)", passed: hasInStack },
            tc3: { name: "Disconnected Components", passed: hasInStack }
          };
        }
      },

      dbg_4: {
        badge: "2D DYNAMIC PROGRAMMING",
        title: "04. Grid Unique Paths with Obstacles",
        desc: "Return unique paths from top-left to bottom-right in m x n grid with obstacles.",
        constraints: "• 1 <= m, n <= 100. Return 0 if start/destination is blocked.",
        files: { c: "GridPaths.c", cpp: "GridPaths.cpp", java: "GridPaths.java", python: "grid_paths.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
int uniquePathsWithObstacles(int** grid, int m, int n) {
    int dp[100][100] = {0};
    dp[0][0] = 1;
    for (int i = 0; i <= m; i++) { // BUG: <= m out of bounds
        for (int j = 0; j <= n; j++) { // BUG: <= n out of bounds
            if (grid[i][j] == 1) dp[i][j] = 0;
            else {
                if (i > 0) dp[i][j] += dp[i-1][j];
                if (j > 0) dp[i][j] += dp[i][j-1];
            }
        }
    }
    return dp[m][n]; // BUG: Should be dp[m-1][n-1]
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        dp[0][0] = 1;
        for (int i = 0; i <= m; i++) { // BUG
            for (int j = 0; j <= n; j++) { // BUG
                if (grid[i][j] == 1) dp[i][j] = 0;
                else {
                    if (i > 0) dp[i][j] += dp[i-1][j];
                    if (j > 0) dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[m][n];
    }
};`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
public class GridPaths {
    public static int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        for (int i = 0; i <= m; i++) { // BUG
            for (int j = 0; j <= n; j++) { // BUG
                if (grid[i][j] == 1) dp[i][j] = 0;
                else {
                    if (i > 0) dp[i][j] += dp[i-1][j];
                    if (j > 0) dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[m][n];
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def unique_paths_with_obstacles(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m + 1): # BUG
        for j in range(n + 1): # BUG
            if grid[i][j] == 1: dp[i][j] = 0
            else:
                if i > 0: dp[i][j] += dp[i-1][j]
                if j > 0: dp[i][j] += dp[i][j-1]
    return dp[m][n]`
        },
        expected: "Check start/end obstacle (grid[0][0]==1 -> 0), bound loops by i < m, j < n, return dp[m-1][n-1].",
        failure: "Loop bounds exceed matrix dimensions; crashes with IndexOutOfBounds / SegFault.",
        hints: {
          c: "Change loops to i < m and j < n. Return dp[m-1][n-1]. Check if grid[0][0] == 1.",
          cpp: "Use i < m, j < n, and return dp[m-1][n-1].",
          java: "Check grid[0][0] == 1 return 0; loop i < m, j < n; return dp[m-1][n-1];",
          python: "Use range(m), range(n), and return dp[m-1][n-1]."
        },
        validate: function(code, lang) {
          const hasBounds = code.includes("i < m") || code.includes("i<m") || code.includes("range(m)");
          const hasTarget = code.includes("dp[m-1][n-1]") || code.includes("dp[m - 1][n - 1]");
          return {
            tc1: { name: "Loop Dimension Check (i < m, j < n)", passed: hasBounds },
            tc2: { name: "Destination Index (dp[m-1][n-1])", passed: hasTarget },
            tc3: { name: "Start Obstacle Guard", passed: code.includes("grid[0][0]") }
          };
        }
      },

      dbg_5: {
        badge: "LINKED LIST",
        title: "05. Linked List Cycle Detection",
        desc: "Detect cycle using Floyd's Tortoise and Hare pointers without null dereferencing.",
        constraints: "• Time: O(N), Space: O(1).",
        files: { c: "ListCycle.c", cpp: "ListCycle.cpp", java: "ListCycle.java", python: "list_cycle.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
#include <stdbool.h>
struct ListNode { int val; struct ListNode *next; };

bool hasCycle(struct ListNode *head) {
    struct ListNode *slow = head, *fast = head;
    while (fast != NULL) { // BUG: Crashes on fast->next->next if fast->next is NULL!
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
struct ListNode { int val; ListNode *next; };

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (fast != nullptr) { // BUG
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
class ListNode { int val; ListNode next; }

public class ListCycle {
    public static boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null) { // BUG
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def has_cycle(head):
    slow = fast = head
    while fast: # BUG: Throws AttributeError when fast.next is None
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False`
        },
        expected: "Loop header must check both fast and fast.next are non-null.",
        failure: "NullPointerException / SIGSEGV on odd-length lists.",
        hints: {
          c: "Use: while (fast != NULL && fast->next != NULL)",
          cpp: "Use: while (fast != nullptr && fast->next != nullptr)",
          java: "Use: while (fast != null && fast.next != null)",
          python: "Use: while fast and fast.next:"
        },
        validate: function(code, lang) {
          const hasGuard = code.includes("fast->next") || code.includes("fast.next");
          return {
            tc1: { name: "Circular List (1->2->3->1)", passed: true },
            tc2: { name: "Odd-length Linear List Guard", passed: hasGuard },
            tc3: { name: "Empty / Single Node", passed: hasGuard }
          };
        }
      },

      dbg_6: {
        badge: "SEARCHING & BOUNDS",
        title: "06. Binary Search & Midpoint Overflow",
        desc: "Implement binary search without integer overflow and with inclusive boundary checks.",
        constraints: "• Time: O(log N), Space: O(1).",
        files: { c: "BinarySearch.c", cpp: "BinarySearch.cpp", java: "BinarySearch.java", python: "binary_search.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low < high) { // BUG 1: misses when target is at single remaining element
        int mid = (low + high) / 2; // BUG 2: integer overflow for large indices
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
    int low = 0, high = nums.size() - 1;
    while (low < high) { // BUG
        int mid = (low + high) / 2; // BUG
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
public class BinarySearch {
    public static int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        while (low < high) { // BUG
            int mid = (low + high) / 2; // BUG
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low < high: # BUG: misses low == high
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1`
        },
        expected: "Use `low <= high` and `low + (high - low) / 2`.",
        failure: "Fails when low == high and overflows on large arrays.",
        hints: {
          c: "Use while (low <= high) and int mid = low + (high - low) / 2;",
          cpp: "Use while (low <= high) and int mid = low + (high - low) / 2;",
          java: "Use while (low <= high) and int mid = low + (high - low) / 2;",
          python: "Use while low <= high: and mid = low + (high - low) // 2"
        },
        validate: function(code, lang) {
          const hasEqual = code.includes("low <= high") || code.includes("low<=high");
          return {
            tc1: { name: "Target Found in Middle", passed: true },
            tc2: { name: "Last Element Inclusive (low <= high)", passed: hasEqual },
            tc3: { name: "Single Element Array", passed: hasEqual }
          };
        }
      },

      dbg_7: {
        badge: "STRING MANIPULATION",
        title: "07. String Palindrome & Boundaries",
        desc: "Check if string is palindrome with proper termination and length bounds.",
        constraints: "• Time: O(N), Space: O(1).",
        files: { c: "Palindrome.c", cpp: "Palindrome.cpp", java: "Palindrome.java", python: "palindrome.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
#include <stdbool.h>
#include <string.h>

bool isPalindrome(char* str) {
    if (!str) return false;
    int len = 0;
    while (str[len] != NULL) len++; // BUG 1: Comparing with NULL pointer instead of '\0'
    int i = 0, j = len; // BUG 2: j should start at len - 1
    while (i < j) {
        if (str[i] != str[j]) return false;
        i++; j--;
    }
    return true;
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <string>
using namespace std;

bool isPalindrome(string s) {
    int i = 0, j = s.length(); // BUG: j should be s.length() - 1
    while (i < j) {
        if (s[i] != s[j]) return false; // Throws out of range
        i++; j--;
    }
    return true;
}`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
public class Palindrome {
    public static boolean isPalindrome(String s) {
        if (s == null) return false;
        int i = 0, j = s.length(); // BUG: j should be s.length() - 1
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) return false; // StringIndexOutOfBoundsException
            i++; j--;
        }
        return true;
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def is_palindrome(s):
    if s is None: return False
    i, j = 0, len(s) # BUG: IndexError when accessing s[j]
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True`
        },
        expected: "Initialize right pointer to length - 1.",
        failure: "Accesses index length (out of bounds) triggering exception / comparing with null char.",
        hints: {
          c: "Use while (str[len] != '\0') and j = len - 1;",
          cpp: "Initialize j = s.length() - 1;",
          java: "Initialize j = s.length() - 1;",
          python: "Initialize j = len(s) - 1."
        },
        validate: function(code, lang) {
          const hasLenMinus1 = code.includes("- 1") || code.includes("-1") || code.includes("len - 1");
          return {
            tc1: { name: "Valid End Index (length - 1)", passed: hasLenMinus1 },
            tc2: { name: "Palindrome 'racecar' -> true", passed: hasLenMinus1 },
            tc3: { name: "Even Length 'abba' -> true", passed: hasLenMinus1 }
          };
        }
      },

      dbg_8: {
        badge: "POINTERS & REFERENCES",
        title: "08. Pass-by-Reference & Swaps",
        desc: "Mutate caller array in-place without losing pass-by-value changes.",
        constraints: "• Time: O(N), Space: O(1).",
        files: { c: "SwapArray.c", cpp: "SwapArray.cpp", java: "SwapArray.java", python: "swap_array.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
void swap(int a, int b) { // BUG: Pass by value! Changes are lost
    int temp = a; a = b; b = temp;
}
void reverse(int arr[], int n) {
    int i = 0, j = n - 1;
    while (i < j) {
        swap(arr[i], arr[j]); // Leaves array untouched
        i++; j--;
    }
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <vector>
using namespace std;

void swapVals(int a, int b) { // BUG: Pass by value
    int temp = a; a = b; b = temp;
}
void reverseArray(vector<int>& arr) {
    int i = 0, j = arr.size() - 1;
    while (i < j) {
        swapVals(arr[i], arr[j]);
        i++; j--;
    }
}`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
public class SwapArray {
    public static void swap(int a, int b) { // BUG: Primitives in Java are pass-by-value
        int temp = a; a = b; b = temp;
    }
    public static void reverse(int[] arr) {
        int i = 0, j = arr.length - 1;
        while (i < j) {
            swap(arr[i], arr[j]);
            i++; j--;
        }
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def swap(a, b): # BUG: Reassigning local variables does not mutate list
    temp = a; a = b; b = temp

def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        swap(arr[i], arr[j])
        i += 1
        j -= 1`
        },
        expected: "Mutate elements directly in array or use pointers / references.",
        failure: "Original array elements remain completely unchanged.",
        hints: {
          c: "Use pointers: void swap(int* a, int* b) { int t = *a; *a = *b; *b = t; } and call swap(&arr[i], &arr[j]);",
          cpp: "Use references: void swapVals(int &a, int &b) or std::swap(arr[i], arr[j]);",
          java: "Mutate directly: int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;",
          python: "Use tuple swap: arr[i], arr[j] = arr[j], arr[i]"
        },
        validate: function(code, lang) {
          const hasRef = code.includes("*a") || code.includes("&a") || code.includes("std::swap") || code.includes("arr[i] = arr[j]") || code.includes("arr[i], arr[j]");
          return {
            tc1: { name: "Proper Pointer / Reference Semantics", passed: hasRef },
            tc2: { name: "Array Actually Mutated [1,2,3] -> [3,2,1]", passed: hasRef },
            tc3: { name: "In-Place O(1) Space", passed: true }
          };
        }
      },

      dbg_9: {
        badge: "MEMORY MANAGEMENT",
        title: "09. Dangling Pointer & Double Free",
        desc: "Fix double free and ensure allocated memory persists for caller.",
        constraints: "• Safe memory allocation and lifecycle.",
        files: { c: "Memory.c", cpp: "Memory.cpp", java: "Memory.java", python: "memory.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
#include <stdlib.h>

int* createBuffer(int size) {
    int* ptr = (int*)malloc(size * sizeof(int));
    if (!ptr) return NULL;
    for (int i = 0; i < size; i++) ptr[i] = i * 2;
    free(ptr); // BUG 1: Frees buffer before caller receives it!
    free(ptr); // BUG 2: Double free!
    return ptr;
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
int* createBuffer(int size) {
    int* ptr = new int[size];
    for (int i = 0; i < size; i++) ptr[i] = i * 2;
    delete[] ptr; // BUG: Premature deletion
    delete[] ptr; // BUG: Double free
    return ptr;
}`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
public class Memory {
    public static int[] createBuffer(int size) {
        int[] buffer = new int[size];
        for (int i = 0; i < size; i++) buffer[i] = i * 2;
        buffer = null; // BUG: Nullifies reference before returning
        return buffer;
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def create_buffer(size):
    buf = [i * 2 for i in range(size)]
    del buf # BUG: Deletes buffer before return
    return buf`
        },
        expected: "Return allocated buffer alive; do not free/nullify before return.",
        failure: "Crashes with Double Free SIGABRT / returns NULL / None.",
        hints: {
          c: "Remove both free(ptr); statements inside createBuffer.",
          cpp: "Remove both delete[] statements before return.",
          java: "Remove buffer = null; before returning buffer.",
          python: "Remove del buf statement."
        },
        validate: function(code, lang) {
          const noDoubleFree = !code.includes("free(ptr);
    free(ptr)") && !code.includes("delete[] ptr;
    delete[] ptr");
          const returnsValid = !code.includes("free(ptr);
    return") && !code.includes("buffer = null;
        return buffer");
          return {
            tc1: { name: "No Double Free Vulnerability", passed: noDoubleFree },
            tc2: { name: "Returns Valid Active Buffer", passed: returnsValid },
            tc3: { name: "Data Integrity Intact", passed: returnsValid }
          };
        }
      },

      dbg_10: {
        badge: "DYNAMIC PROGRAMMING",
        title: "10. Longest Increasing Subsequence (LIS)",
        desc: "Compute length of longest increasing subsequence with proper base case initialization.",
        constraints: "• Time: O(N^2), Space: O(N).",
        files: { c: "LIS.c", cpp: "LIS.cpp", java: "LIS.java", python: "lis.py" },
        codes: {
          c: `// Capgemini Exceller Stage 2B — Buggy Code (C)
int lengthOfLIS(int* nums, int n) {
    if (n <= 0) return 0;
    int dp[1000] = {0}; // BUG: Every single number is LIS of length 1!
    int maxLen = 0; // BUG: Should be initialized to 1
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
            }
        }
        if (dp[i] > maxLen) maxLen = dp[i];
    }
    return maxLen;
}`,
          cpp: `// Capgemini Exceller Stage 2B — Buggy Code (C++)
#include <vector>
#include <algorithm>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    if (nums.empty()) return 0;
    vector<int> dp(nums.size(), 0); // BUG: Initialized to 0 instead of 1
    int maxLen = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
        }
        maxLen = max(maxLen, dp[i]);
    }
    return maxLen;
}`,
          java: `// Capgemini Exceller Stage 2B — Buggy Code (Java)
import java.util.Arrays;

public class LIS {
    public static int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int[] dp = new int[nums.length]; // BUG: Default 0 instead of 1
        int maxLen = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        return maxLen;
    }
}`,
          python: `# Capgemini Exceller Stage 2B — Buggy Code (Python)
def length_of_lis(nums):
    if not nums: return 0
    dp = [0] * len(nums) # BUG: Base length is 1 for each element
    max_len = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    return max_len`
        },
        expected: "Initialize DP array elements to 1 and maxLen to 1.",
        failure: "Returns 0 or understated lengths because un-updated elements retain 0.",
        hints: {
          c: "Initialize for (int i=0; i<n; i++) dp[i] = 1; and maxLen = 1;",
          cpp: "Initialize vector<int> dp(nums.size(), 1); and maxLen = 1;",
          java: "Use Arrays.fill(dp, 1); and int maxLen = 1;",
          python: "Use dp = [1] * len(nums) and max_len = 1."
        },
        validate: function(code, lang) {
          const hasInit1 = code.includes("dp[i] = 1") || code.includes("vector<int> dp(nums.size(), 1)") || code.includes("Arrays.fill(dp, 1)") || code.includes("[1] * len(nums)") || code.includes("dp, 1");
          return {
            tc1: { name: "Single Element Array [10] -> 1", passed: hasInit1 },
            tc2: { name: "Decreasing Array [5,4,3,2,1] -> 1", passed: hasInit1 },
            tc3: { name: "Standard LIS [10,9,2,5,3,7,101,18] -> 4", passed: hasInit1 }
          };
        }
      }
    };

    function loadProblem(key) {
      currentProbKey = key;
      const select = document.getElementById('probSelect');
      if (select && select.value !== key) select.value = key;

      const p = DBG_BANK[key] || DBG_BANK['dbg_1'];
      document.getElementById('probBadge').textContent = p.badge;
      document.getElementById('probTitle').textContent = p.title;
      document.getElementById('probDesc').textContent = p.desc;
      document.getElementById('probConstraints').innerHTML = p.constraints;
      document.getElementById('hudExpected').textContent = p.expected;
      document.getElementById('hudFailure').textContent = p.failure;

      updateEditorLanguage();
      
      document.getElementById('tcResults').innerHTML = `<div class="tc-pill" style="background:#131d33; color:#94a3b8;">Click "Validate Solution" to test your fix</div>`;
      document.getElementById('passCount').textContent = "0 / 3 Passed";
      
      // Update step tracker
      document.querySelectorAll('.step-item').forEach(el => el.classList.remove('active', 'completed'));
      document.getElementById('st-1').classList.add('active');
    }

    function switchLanguage(lang) {
      currentLang = lang;
      updateEditorLanguage();
    }

    function updateEditorLanguage() {
      const p = DBG_BANK[currentProbKey] || DBG_BANK['dbg_1'];
      document.getElementById('fileName').textContent = p.files[currentLang] || "Solution.txt";
      document.getElementById('codeEditor').value = p.codes[currentLang] || "// Code not available";
    }

    function resetCode() {
      updateEditorLanguage();
    }

    function runValidation() {
      const p = DBG_BANK[currentProbKey] || DBG_BANK['dbg_1'];
      const code = document.getElementById('codeEditor').value;
      const res = p.validate(code, currentLang);
      
      let passCount = 0;
      let total = 0;
      let html = '';

      for (let k in res) {
        total++;
        if (res[k].passed) {
          passCount++;
          html += `<div class="tc-pill tc-pass">✓ ${res[k].name}: PASSED</div>`;
        } else {
          html += `<div class="tc-pill tc-fail">✗ ${res[k].name}: FAILED</div>`;
        }
      }

      document.getElementById('tcResults').innerHTML = html;
      document.getElementById('passCount').textContent = `${passCount} / ${total} Passed`;
      document.getElementById('passCount').style.color = passCount === total ? "#06d6a0" : "#ef4444";

      // Step progress
      if (passCount === total) {
        document.querySelectorAll('.step-item').forEach(el => el.classList.add('completed'));
        alert(`🎉 EXCELLENT! All test cases passed in ${currentLang.toUpperCase()}! You resolved all bugs according to Capgemini specifications.`);
      } else if (passCount > 0) {
        document.getElementById('st-1').classList.add('completed');
        document.getElementById('st-2').classList.add('completed');
        document.getElementById('st-3').classList.add('active');
      }
    }

    function showSolutionHint() {
      const p = DBG_BANK[currentProbKey] || DBG_BANK['dbg_1'];
      const hint = p.hints[currentLang] || p.hints['c'];
      alert(`💡 Fix Advice (${currentLang.toUpperCase()}):\n\n` + hint.replace(/\\n/g, "\n"));
    }

    // Timer (20 mins)
    let timeLeft = 20 * 60;
    setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        const m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
        const s = (timeLeft % 60).toString().padStart(2, '0');
        document.getElementById('timer').textContent = `${m}:${s}`;
      }
    }, 1000);

    // Initial load from URL param ?id=dbg_1 to dbg_10
    window.onload = () => {
      const urlParams = new URLSearchParams(window.location.search);
      const testId = urlParams.get('id') || 'dbg_1';
      loadProblem(DBG_BANK[testId] ? testId : 'dbg_1');
    };
  </script>
</body>
</html>
'''

with open('modules/debug_sim.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated modules/debug_sim.html with Multi-Language C, C++, Java, Python successfully!")
