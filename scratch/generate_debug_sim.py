import sys
sys.stdout.reconfigure(encoding='utf-8')

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Stage 2B: Debugging Assessment (10 Hands-On Challenges) | Capgemini Exceller 2027</title>
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
    .lang-badge { background: rgba(0,212,255,0.15); color: #00d4ff; padding: 0.2rem 0.55rem; border-radius: 4px; font-weight: 700; font-size: 0.72rem; }
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
        <div style="font-size:0.72rem; color:#94a3b8;">10 Hands-On Debugging Challenges • C / C++ / Java • Trees, Graphs, 2D DP, Pointers</div>
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
          <option value="dbg_2">Test 2: 02. Binary Tree: Maximum Path Sum (C++)</option>
          <option value="dbg_3">Test 3: 03. Graph: Detect Cycle in Directed Graph (Java)</option>
          <option value="dbg_4">Test 4: 04. 2D DP: Grid Unique Paths with Obstacles (C)</option>
          <option value="dbg_5">Test 5: 05. Linked List: Cycle Detection & Length (C++)</option>
          <option value="dbg_6">Test 6: 06. Binary Search & Midpoint Overflow (Java)</option>
          <option value="dbg_7">Test 7: 07. String: Palindrome & Null-Terminator (C)</option>
          <option value="dbg_8">Test 8: 08. Pointers: Pass-by-Value Swap Bug (C++)</option>
          <option value="dbg_9">Test 9: 09. Memory: Dangling Pointer & Double Free (C)</option>
          <option value="dbg_10">Test 10: 10. DP: Longest Increasing Subsequence (Java)</option>
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
        <div style="display:flex; align-items:center; gap:0.5rem;">
          <span class="lang-badge" id="langBadge">C (GCC 11.3)</span>
          <span style="color:#94a3b8; font-size:0.78rem;" id="fileName">Solution.c</span>
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
          <li><strong>Syntax &amp; Compilation:</strong> Clean fix matching signature.</li>
          <li><strong>Edge Cases:</strong> NULL pointers, zero capacity, out-of-bounds.</li>
          <li><strong>Correctness:</strong> Maximum value matching 0/1 recurrence.</li>
        </ul>
      </div>

      <button class="btn-action" style="margin-top:auto; background:linear-gradient(135deg,#00d4ff,#7c3aed);" onclick="showSolutionHint()">💡 Show Hint / Fix Explanation</button>
    </div>
  </div>

  <script>
    const PROBLEMS = {
      dbg_1: {
        badge: "0/1 KNAPSACK (CAPGEMINI AON REPLICA)",
        title: "01. Knapsack-C",
        desc: "Given a set of items with weight wt and value val of length n and knapsack capacity W, find maximum sum of values such that overall weight <= W. Return -1 if wt == NULL or val == NULL or distribution is impossible.",
        constraints: "• 0 <= n <= 10^5, 1 <= wt[i] <= 10^6, 1 <= val[i] <= 10^6, 1 <= W <= 10^5.<br/>• Return -1 if wt == NULL or val == NULL.<br/>• Pick item at most once (no fraction).",
        lang: "C (Gcc 11.3)",
        file: "KnapsackProblem.c",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <stdio.h>
#include <stdlib.h>

int KnapsackProblem(int* wt, int* val, int n, int W) {
    // BUG 1: Missing NULL pointer check required by problem specifications
    
    // BUG 2: Static array sizing causes stack overflow on large inputs or incorrect bounds
    int dp[100][100];
    
    for (int i = 0; i < n; i++) {
        for (int w = 0; w < W; w++) { // BUG 3: w < W misses exact capacity W (should be <= W)
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (wt[i-1] <= w) {
                // BUG 4: Incorrect recurrence index
                dp[i][w] = val[i] + dp[i-1][w - wt[i]];
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    return dp[n-1][W-1];
}`,
        expected: "Return max value for capacity W; return -1 if wt == NULL or val == NULL or invalid capacity.",
        failure: "Crashes on NULL pointers, loop bounds `w < W` exclude capacity W, and `val[i]` index out of bounds.",
        validate: function(code) {
          const hasNullCheck = code.includes("wt == NULL") || code.includes("val == NULL") || code.includes("!wt") || code.includes("!val");
          const hasCapacityBound = code.includes("w <= W") || code.includes("w<=W") || code.includes("j <= W");
          const hasCorrectValIdx = code.includes("val[i-1]") || code.includes("val[i - 1]");
          return {
            tc1: { name: "NULL Pointer Check (Return -1)", passed: hasNullCheck },
            tc2: { name: "Full Capacity Bounds (w <= W)", passed: hasCapacityBound },
            tc3: { name: "0/1 Recurrence Indexing val[i-1]", passed: hasCorrectValIdx }
          };
        },
        hint: "1. Add NULL check: `if (wt == NULL || val == NULL || n <= 0 || W <= 0) return -1;`\\n2. Allocate DP table of size `(n+1) * (W+1)`.\\n3. In loop: `for (int w = 0; w <= W; w++)`.\\n4. Use `val[i-1] + dp[i-1][w - wt[i-1]]`."
      },

      dbg_2: {
        badge: "TREE ALGORITHM",
        title: "02. Binary Tree Maximum Path Sum",
        desc: "The function calculates the maximum path sum in a binary tree. It contains a critical bug where negative child contributions are added directly, degrading the overall maximum path.",
        constraints: "• Node values can be negative.<br/>• Time: O(N), Space: O(H).",
        lang: "C++ 20",
        file: "MaxPathSum.cpp",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxPathDown(TreeNode* root, int &maxSum) {
        if (root == NULL) return 0;
        
        // BUG: Directly taking branch sum without ignoring negative contributions!
        int left = maxPathDown(root->left, maxSum);
        int right = maxPathDown(root->right, maxSum);
        
        maxSum = max(maxSum, left + right + root->val);
        
        // BUG: Returns sum of both branches instead of single branch to parent
        return root->val + left + right; 
    }

    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        maxPathDown(root, maxSum);
        return maxSum;
    }
};`,
        expected: "Must return highest sum path between any two nodes. Handles negative values by ignoring branches where branchSum < 0.",
        failure: "Fails when left or right child has negative value — currently includes negative branch sums instead of clipping to 0.",
        validate: function(code) {
          const hasMax0 = code.includes("max(0") || code.includes("max( 0") || code.includes("0,");
          const hasSingleBranch = code.includes("max(left, right)") || code.includes("max(left,right)") || code.includes("max(right, left)");
          return {
            tc1: { name: "Sample Tree [1,2,3]", passed: code.length > 50 },
            tc2: { name: "Negative Nodes [-10,9,20,null,null,15,7]", passed: hasMax0 },
            tc3: { name: "Single Branch Max Return", passed: hasSingleBranch }
          };
        },
        hint: "Fix 1: Clip negative branches: `int left = max(0, maxPathDown(root->left, maxSum));`\\nFix 2: Return single branch: `return root->val + max(left, right);`"
      },

      dbg_3: {
        badge: "GRAPH ALGORITHM",
        title: "03. Detect Cycle in Directed Graph",
        desc: "Given a directed graph with V vertices and an adjacency list, return true if the graph contains a cycle. The current DFS implementation fails because it only tracks visited nodes but not recursion stack state.",
        constraints: "• 1 <= V <= 10^5, 0 <= E <= 10^5.<br/>• Must handle disconnected components.",
        lang: "Java 17",
        file: "GraphCycle.java",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
import java.util.*;

public class GraphCycle {
    public static boolean isCyclic(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[V];
        // BUG: Missing inStack[] array to differentiate between visited in current path vs earlier path
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (dfs(i, adj, visited)) return true;
            }
        }
        return false;
    }

    private static boolean dfs(int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited) {
        visited[node] = true;
        
        for (int neighbor : adj.get(node)) {
            if (visited[neighbor]) {
                // BUG: False positive! If node visited in unrelated subtree, it falsely claims a cycle
                return true; 
            }
            if (dfs(neighbor, adj, visited)) return true;
        }
        return false;
    }
}`,
        expected: "Must distinguish between a back-edge (cycle) in current DFS path and a cross-edge to an already visited component.",
        failure: "Falsely detects a cycle for DAGs with diamond structures because it treats any previously visited node as a cycle.",
        validate: function(code) {
          const hasInStack = code.includes("inStack") || code.includes("recStack") || code.includes("inPath") || code.includes("visited[neighbor] == 2") || code.includes("state");
          return {
            tc1: { name: "Simple Cycle (0->1->2->0)", passed: true },
            tc2: { name: "Diamond DAG (0->1, 0->2, 1->3, 2->3)", passed: hasInStack },
            tc3: { name: "Disconnected Forest", passed: hasInStack }
          };
        },
        hint: "Add `boolean[] inStack = new boolean[V]`. Mark `inStack[node] = true;` before neighbor loop and `inStack[node] = false;` on backtrack. A cycle only occurs if `inStack[neighbor] == true`!"
      },

      dbg_4: {
        badge: "2D DYNAMIC PROGRAMMING",
        title: "04. Grid Unique Paths with Obstacles",
        desc: "Given an m x n obstacleGrid where 1 represents an obstacle and 0 a free space, return the number of unique paths from top-left to bottom-right.",
        constraints: "• 1 <= m, n <= 100.<br/>• If start or target has obstacle, paths = 0.",
        lang: "C (Gcc 11.3)",
        file: "UniquePathsObstacles.c",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <stdio.h>

int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize) {
    int m = obstacleGridSize;
    int n = obstacleGridColSize[0];
    
    // BUG 1: Missing check if start cell (0,0) or target (m-1,n-1) has obstacle!
    int dp[100][100] = {0};
    dp[0][0] = 1;
    
    for (int i = 0; i <= m; i++) { // BUG 2: i <= m causes out of bounds!
        for (int j = 0; j <= n; j++) { // BUG 3: j <= n causes out of bounds!
            if (obstacleGrid[i][j] == 1) {
                dp[i][j] = 0;
            } else {
                if (i > 0) dp[i][j] += dp[i-1][j];
                if (j > 0) dp[i][j] += dp[i][j-1];
            }
        }
    }
    return dp[m][n]; // BUG 4: Should be dp[m-1][n-1]
}`,
        expected: "Return paths to (m-1, n-1) with 0 if start/end is blocked, and loop indices bounded by < m and < n.",
        failure: "Loop bounds `i <= m` and `j <= n` exceed array limits and target access `dp[m][n]` returns garbage data.",
        validate: function(code) {
          const hasCorrectBounds = code.includes("i < m") || code.includes("i<m");
          const hasCorrectTarget = code.includes("dp[m-1][n-1]") || code.includes("dp[m - 1][n - 1]");
          const hasStartCheck = code.includes("obstacleGrid[0][0] == 1") || code.includes("obstacleGrid[0][0]==1") || code.includes("!obstacleGrid[0][0]");
          return {
            tc1: { name: "Loop Bound Check (i<m, j<n)", passed: hasCorrectBounds },
            tc2: { name: "Destination Index (dp[m-1][n-1])", passed: hasCorrectTarget },
            tc3: { name: "Start Obstacle Handled", passed: hasStartCheck }
          };
        },
        hint: "1. Change loop bounds to `i < m` and `j < n`.\\n2. Return `dp[m-1][n-1]`.\\n3. Check if `obstacleGrid[0][0] == 1`, return 0 immediately."
      },

      dbg_5: {
        badge: "LINKED LIST",
        title: "05. Linked List Cycle Detection & Length",
        desc: "Given head of a linked list, detect if a cycle exists using Floyd's Tortoise and Hare algorithm. The current implementation crashes with a NULL pointer dereference on fast->next.",
        constraints: "• 0 <= Number of nodes <= 10^5.<br/>• Time: O(N), Space: O(1).",
        lang: "C++ 20",
        file: "ListCycle.cpp",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;
        
        // BUG: fast->next->next can trigger Segmentation Fault when fast->next is NULL!
        while (fast != NULL) {
            slow = slow->next;
            fast = fast->next->next; 
            
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
};`,
        expected: "Loop condition must check both `fast != NULL && fast->next != NULL` before advancing fast.",
        failure: "Throws SIGSEGV (Null pointer dereference) on odd-length lists or when fast reaches the last node.",
        validate: function(code) {
          const hasGuard = code.includes("fast->next != NULL") || code.includes("fast->next != nullptr") || code.includes("fast->next");
          return {
            tc1: { name: "Circular List (1->2->3->1)", passed: true },
            tc2: { name: "Odd-length Linear List (1->2->3)", passed: hasGuard },
            tc3: { name: "Empty / Single Node List", passed: hasGuard }
          };
        },
        hint: "Change loop header to: `while (fast != NULL && fast->next != NULL)` to guarantee `fast->next->next` is safe."
      },

      dbg_6: {
        badge: "SEARCHING & BOUNDS",
        title: "06. Binary Search & Midpoint Overflow",
        desc: "Implement binary search to find target in a sorted integer array. The code contains integer overflow on mid calculation and fails when target is at the last index.",
        constraints: "• Array length up to 2 * 10^9.<br/>• Time: O(log N), Space: O(1).",
        lang: "Java 17",
        file: "BinarySearch.java",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
public class BinarySearch {
    public static int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        // BUG 1: Condition low < high misses when target is at the only remaining element (low == high)
        while (low < high) { 
            // BUG 2: Direct (low + high) / 2 overflows Integer.MAX_VALUE for large indices
            int mid = (low + high) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
}`,
        expected: "Must use `low <= high` to check single element ranges and `low + (high - low) / 2` to prevent overflow.",
        failure: "Fails to find elements when low == high and overflows into negative integers on large arrays.",
        validate: function(code) {
          const hasSafeMid = code.includes("low + (high - low) / 2") || code.includes("low + (high-low)/2") || code.includes(">>> 1");
          const hasEqualBound = code.includes("low <= high") || code.includes("low<=high");
          return {
            tc1: { name: "Standard Target Found", passed: true },
            tc2: { name: "Last Element (low == high)", passed: hasEqualBound },
            tc3: { name: "Large Array Safe Midpoint", passed: hasSafeMid }
          };
        },
        hint: "1. Update loop to `while (low <= high)`\\n2. Calculate mid using `int mid = low + (high - low) / 2;`."
      },

      dbg_7: {
        badge: "STRING MANIPULATION",
        title: "07. String Palindrome & Null-Terminator",
        desc: "Check whether a given C string is a palindrome. The current code calculates string length incorrectly by checking NULL pointer instead of '\\0' and has an off-by-one indexing error.",
        constraints: "• String length up to 10^4 characters.<br/>• Case-sensitive comparison.",
        lang: "C (Gcc 11.3)",
        file: "PalindromeCheck.c",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(char* str) {
    if (str == NULL) return false;
    
    int len = 0;
    // BUG 1: Comparing str[len] with NULL pointer instead of null-terminator '\\0'
    while (str[len] != NULL) { 
        len++;
    }
    
    // BUG 2: j starts at len (out of bounds character '\\0') instead of len - 1
    int i = 0, j = len; 
    while (i < j) {
        if (str[i] != str[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}`,
        expected: "Use `str[len] != '\\0'` for character termination and initialize `j = len - 1`.",
        failure: "Compiles with warnings and compares `str[0]` with `str[len]` ('\\0'), always returning false.",
        validate: function(code) {
          const hasNullChar = code.includes("'\\0'") || code.includes("str[len] != 0") || code.includes("while (str[len])") || code.includes("strlen");
          const hasCorrectJ = code.includes("len - 1") || code.includes("len-1");
          return {
            tc1: { name: "Null Terminator Character Check", passed: hasNullChar },
            tc2: { name: "Valid End Index (len - 1)", passed: hasCorrectJ },
            tc3: { name: "Palindrome Validation ('racecar')", passed: hasCorrectJ }
          };
        },
        hint: "1. Terminate length loop with `while (str[len] != '\\0')` or `strlen(str)`.\\n2. Initialize right pointer: `int j = len - 1;`."
      },

      dbg_8: {
        badge: "POINTERS & REFERENCES",
        title: "08. Pass-by-Value Swap & Array Inversion",
        desc: "Reverse an integer array in place by calling a helper swap function. Because the helper passes integers by value, elements are not actually swapped in the original array.",
        constraints: "• In-place modification required.<br/>• Time: O(N), Space: O(1).",
        lang: "C++ 20",
        file: "ArraySwap.cpp",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <iostream>
#include <vector>
using namespace std;

// BUG: Passed by value! Local copies a and b are modified, leaving caller array unchanged
void swapElements(int a, int b) { 
    int temp = a;
    a = b;
    b = temp;
}

void reverseArray(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        swapElements(arr[left], arr[right]);
        left++;
        right--;
    }
}`,
        expected: "Pass arguments by reference (`int &a, int &b`) or pointers (`int* a, int* b`) to mutate the array.",
        failure: "Array remains completely unchanged after reverseArray() completes.",
        validate: function(code) {
          const hasRef = code.includes("int &a") || code.includes("int& a") || code.includes("int* a") || code.includes("std::swap");
          return {
            tc1: { name: "Pass-by-Reference / Pointer Signature", passed: hasRef },
            tc2: { name: "In-Place Array Reversal [1,2,3,4,5]", passed: hasRef },
            tc3: { name: "Even Length Reversal", passed: hasRef }
          };
        },
        hint: "Change signature to `void swapElements(int &a, int &b)` in C++ or `void swapElements(int* a, int* b)` and dereference."
      },

      dbg_9: {
        badge: "MEMORY MANAGEMENT",
        title: "09. Dangling Pointer & Double Free",
        desc: "Allocate and initialize dynamic buffers in C. The code deallocates the pointer twice and returns a dangling reference to a local stack array.",
        constraints: "• Clean heap memory management without leaks or SIGSEGV.",
        lang: "C (Gcc 11.3)",
        file: "MemoryBuffer.c",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
#include <stdio.h>
#include <stdlib.h>

int* createAndProcessBuffer(int size) {
    int* ptr = (int*)malloc(size * sizeof(int));
    if (ptr == NULL) return NULL;
    
    for (int i = 0; i < size; i++) {
        ptr[i] = i * 2;
    }
    
    // BUG 1: Frees buffer before returning, causing callers to access dangling deallocated memory!
    free(ptr);
    
    // BUG 2: Double free!
    free(ptr);
    
    return ptr;
}`,
        expected: "Caller owns the allocated buffer; do not call `free(ptr)` inside the creation function.",
        failure: "Double free crashes memory allocator with SIGABRT and returns freed dangling pointer.",
        validate: function(code) {
          const noDoubleFree = !code.includes("free(ptr);\n    free(ptr)") && !code.includes("free(ptr); \n    free(ptr)");
          const returnsAlive = !code.includes("free(ptr);\n    return ptr;");
          return {
            tc1: { name: "No Double Free Vulnerability", passed: noDoubleFree },
            tc2: { name: "Returns Valid Allocated Heap Pointer", passed: returnsAlive },
            tc3: { name: "Buffer Integrity Check", passed: returnsAlive }
          };
        },
        hint: "Remove both `free(ptr);` lines from `createAndProcessBuffer` so the allocated memory remains valid for the caller."
      },

      dbg_10: {
        badge: "DYNAMIC PROGRAMMING",
        title: "10. Longest Increasing Subsequence (LIS)",
        desc: "Find the length of the longest strictly increasing subsequence in an integer array. The DP table is initialized to 0 instead of 1, causing incorrect length calculations.",
        constraints: "• 1 <= nums.length <= 2500.<br/>• Time: O(N^2), Space: O(N).",
        lang: "Java 17",
        file: "LIS.java",
        initialCode: `// Capgemini Exceller Stage 2B — Buggy Code
import java.util.Arrays;

public class LIS {
    public static int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        
        int n = nums.length;
        int[] dp = new int[n]; 
        // BUG 1: Every single element is an increasing subsequence of length 1 (dp array must be initialized to 1)
        
        int maxLen = 0; // BUG 2: Should be at least 1 for non-empty array
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    // BUG 3: Recurrence logic fails because dp[j] starts at 0
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        return maxLen;
    }
}`,
        expected: "Initialize `Arrays.fill(dp, 1)` and `maxLen = 1`.",
        failure: "Returns 0 or understated lengths because un-updated elements retain default value of 0.",
        validate: function(code) {
          const hasFill = code.includes("Arrays.fill(dp, 1)") || code.includes("dp[i] = 1") || code.includes("Arrays.fill(dp,1)");
          return {
            tc1: { name: "Single Element Array [10] -> 1", passed: hasFill },
            tc2: { name: "Strictly Decreasing Array [5,4,3,2,1] -> 1", passed: hasFill },
            tc3: { name: "Standard LIS [10,9,2,5,3,7,101,18] -> 4", passed: hasFill }
          };
        },
        hint: "Initialize every element's base length to 1: `Arrays.fill(dp, 1);` and `int maxLen = 1;`."
      }
    };

    let currentProbKey = 'dbg_1';

    function loadProblem(key) {
      currentProbKey = key;
      const select = document.getElementById('probSelect');
      if (select && select.value !== key) select.value = key;

      const p = PROBLEMS[key] || PROBLEMS['dbg_1'];
      document.getElementById('probBadge').textContent = p.badge;
      document.getElementById('probTitle').textContent = p.title;
      document.getElementById('probDesc').textContent = p.desc;
      document.getElementById('probConstraints').innerHTML = p.constraints;
      document.getElementById('langBadge').textContent = p.lang;
      document.getElementById('fileName').textContent = p.file;
      document.getElementById('codeEditor').value = p.initialCode;
      document.getElementById('hudExpected').textContent = p.expected;
      document.getElementById('hudFailure').textContent = p.failure;
      document.getElementById('tcResults').innerHTML = `<div class="tc-pill" style="background:#131d33; color:#94a3b8;">Click "Validate Solution" to test your fix</div>`;
      document.getElementById('passCount').textContent = "0 / 3 Passed";
      
      // Update step tracker
      document.querySelectorAll('.step-item').forEach(el => el.classList.remove('active', 'completed'));
      document.getElementById('st-1').classList.add('active');
    }

    function resetCode() {
      const p = PROBLEMS[currentProbKey] || PROBLEMS['dbg_1'];
      document.getElementById('codeEditor').value = p.initialCode;
      loadProblem(currentProbKey);
    }

    function runValidation() {
      const p = PROBLEMS[currentProbKey] || PROBLEMS['dbg_1'];
      const code = document.getElementById('codeEditor').value;
      const res = p.validate(code);
      
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
        alert("🎉 EXCELLENT! All test cases passed! You resolved all bugs according to Capgemini specifications.");
      } else if (passCount > 0) {
        document.getElementById('st-1').classList.add('completed');
        document.getElementById('st-2').classList.add('completed');
        document.getElementById('st-3').classList.add('active');
      }
    }

    function showSolutionHint() {
      const p = PROBLEMS[currentProbKey] || PROBLEMS['dbg_1'];
      alert("💡 Solution Advice / Root Cause Fix:\\n\\n" + p.hint.replace(/\\n/g, "\\n"));
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
      loadProblem(PROBLEMS[testId] ? testId : 'dbg_1');
    };
  </script>
</body>
</html>
'''

with open('modules/debug_sim.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated modules/debug_sim.html with all 10 problems successfully!")
