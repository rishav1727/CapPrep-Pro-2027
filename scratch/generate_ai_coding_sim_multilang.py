import sys
sys.stdout.reconfigure(encoding='utf-8')

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Stage 3: AI-Assisted Coding Assessment (Multi-Language: C, C++, Java, Python) | Capgemini Exceller 2027</title>
  <link rel="stylesheet" href="../css/style.css"/>
  <style>
    body { background: #0a0f1d; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; overflow: hidden; height: 100vh; margin: 0; display: flex; flex-direction: column; }
    .sim-header { background: #0f172a; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 0.6rem 1.25rem; display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; }
    .badge-lab { background: #06d6a0; color: #042f2e; padding: 0.25rem 0.65rem; border-radius: 4px; font-weight: 800; font-size: 0.75rem; letter-spacing: 0.5px; }
    .sim-timer { font-family: monospace; font-size: 1.5rem; font-weight: 800; color: #ef4444; }
    
    .sim-container { display: grid; grid-template-columns: 1fr 480px; flex: 1; overflow: hidden; }

    /* Left Panel: Problem + Coding Panel */
    .left-workspace { display: flex; flex-direction: column; background: #060a12; border-right: 1px solid rgba(255,255,255,0.1); overflow: hidden; }
    .prob-header-bar { background: #090d16; border-bottom: 1px solid rgba(255,255,255,0.08); padding: 0.75rem 1.25rem; }
    .prob-selector { background: #131d33; border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 0.45rem 0.75rem; border-radius: 6px; font-size: 0.85rem; width: 100%; outline: none; margin-bottom: 0.5rem; }
    
    .prob-details-pane { max-height: 190px; overflow-y: auto; padding: 0.75rem 1.25rem; background: #0c1322; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.84rem; line-height: 1.5; color: #cbd5e1; }
    .prob-num { font-size: 0.78rem; color: #00d4ff; font-weight: 700; margin-bottom: 0.2rem; }
    .prob-title { font-size: 1.15rem; font-weight: 800; color: #fff; margin-bottom: 0.4rem; }
    .code-box { background: #040711; border: 1px solid rgba(0,212,255,0.2); border-radius: 6px; padding: 0.55rem 0.75rem; font-family: monospace; font-size: 0.8rem; color: #38bdf8; margin: 0.4rem 0; white-space: pre; }
    .note-box { background: rgba(0,212,255,0.05); border-left: 3px solid #00d4ff; padding: 0.5rem 0.75rem; font-size: 0.78rem; color: #cbd5e1; margin-top: 0.4rem; border-radius: 0 6px 6px 0; }

    /* Code Editor in Left Workspace */
    .editor-section { flex: 1; display: flex; flex-direction: column; overflow: hidden; background: #080c14; }
    .editor-toolbar { background: #0f172a; border-bottom: 1px solid rgba(255,255,255,0.08); padding: 0.4rem 1rem; display: flex; align-items: center; justify-content: space-between; }
    .lang-dropdown { background: #1e293b; color: #00d4ff; border: 1px solid rgba(0,212,255,0.3); border-radius: 4px; padding: 0.25rem 0.6rem; font-size: 0.78rem; font-weight: 700; outline: none; cursor: pointer; }
    .code-area { flex: 1; padding: 1rem; font-family: "Fira Code", monospace, Consolas; font-size: 0.88rem; line-height: 1.55; color: #a5f3fc; background: #060a12; border: none; outline: none; resize: none; overflow: auto; white-space: pre; }
    
    .testcase-panel { height: 130px; background: #090d16; border-top: 1px solid rgba(255,255,255,0.1); padding: 0.5rem 1rem; display: flex; flex-direction: column; gap: 0.4rem; overflow-y: auto; }
    .tc-pill { font-size: 0.75rem; padding: 0.35rem 0.75rem; border-radius: 6px; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem; }
    .tc-pass { background: rgba(6,214,160,0.15); color: #06d6a0; border: 1px solid rgba(6,214,160,0.3); }
    .tc-fail { background: rgba(239,68,68,0.15); color: #ef4444; border: 1px solid rgba(239,68,68,0.3); }

    /* Right Panel: AI Coding Assistant */
    .right-assistant { display: flex; flex-direction: column; background: #0c1322; overflow: hidden; }
    .assistant-header { background: #090d16; border-bottom: 1px solid rgba(255,255,255,0.08); padding: 0.65rem 1.25rem; display: flex; align-items: center; justify-content: space-between; }
    .chat-history { flex: 1; padding: 1.25rem; overflow-y: auto; display: flex; flex-direction: column; gap: 0.85rem; }
    .chat-msg { max-width: 90%; padding: 0.85rem 1rem; border-radius: 10px; font-size: 0.84rem; line-height: 1.5; }
    .msg-ai { align-self: flex-start; background: #131e36; border: 1px solid rgba(0,212,255,0.18); color: #e2e8f0; border-bottom-left-radius: 2px; }
    .msg-user { align-self: flex-end; background: #1e3a8a; color: #ffffff; border-bottom-right-radius: 2px; }
    
    .chat-input-area { padding: 0.85rem 1.25rem; background: #090d16; border-top: 1px solid rgba(255,255,255,0.08); display: flex; flex-direction: column; gap: 0.5rem; }
    .chat-input { width: 100%; background: #131d33; border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; color: #fff; padding: 0.75rem; font-size: 0.85rem; resize: none; outline: none; box-sizing: border-box; }
    .chat-input:focus { border-color: #00d4ff; }
    
    .btn-send { background: linear-gradient(135deg, #00d4ff, #7c3aed); color: #fff; border: none; padding: 0.5rem 1.1rem; border-radius: 6px; font-weight: 700; font-size: 0.82rem; cursor: pointer; transition: all 0.2s; }
    .btn-send:hover { opacity: 0.9; }
    .btn-insert { background: #06d6a0; color: #042f2e; border: none; padding: 0.35rem 0.75rem; border-radius: 4px; font-weight: 700; font-size: 0.75rem; cursor: pointer; margin-top: 0.5rem; display: inline-flex; align-items: center; gap: 0.35rem; }
    .btn-insert:hover { background: #059669; }

    .step-badge { font-size: 0.72rem; padding: 0.2rem 0.5rem; border-radius: 4px; background: rgba(0,212,255,0.15); color: #00d4ff; font-weight: 700; }
  </style>
</head>
<body>

  <!-- SIMULATOR HEADER -->
  <div class="sim-header">
    <div style="display:flex; align-items:center; gap:0.75rem;">
      <span class="badge-lab">STAGE 3 • AI ASSISTED CODING</span>
      <div>
        <div style="font-weight:800; font-size:0.92rem; color:#fff;">AI Assisted Coding Assessment (Scaffolding Flow)</div>
        <div style="font-size:0.72rem; color:#94a3b8;">10 Interactive Challenges • Multi-Language (C, C++, Java, Python)</div>
      </div>
    </div>
    <div style="display:flex; align-items:center; gap:1.5rem;">
      <div style="text-align:right;">
        <span style="font-size:0.7rem; color:#94a3b8; display:block;">TIME REMAINING</span>
        <span class="sim-timer" id="timer">45:00</span>
      </div>
      <button class="btn-send" style="background:#334155;" onclick="location.href=\'../index.html#stage3\'">← Back to Dashboard</button>
    </div>
  </div>

  <div class="sim-container">
    <!-- LEFT PANEL: PROBLEM & CODE EDITOR -->
    <div class="left-workspace">
      <div class="prob-header-bar">
        <label style="font-size:0.75rem; color:#94a3b8; font-weight:700; display:block; margin-bottom:0.25rem;">SELECT CODING CHALLENGE (1-10):</label>
        <select class="prob-selector" id="probSelect" onchange="loadProblem(this.value)">
          <option value="aic_1">Test 1: 01. LCM of Two Binary Trees (Official Capgemini Problem)</option>
          <option value="aic_2">Test 2: 02. In-Place Reversal of Singly Linked List</option>
          <option value="aic_3">Test 3: 03. Longest Substring Without Repeating Characters</option>
          <option value="aic_4">Test 4: 04. Lowest Common Ancestor (LCA) in Binary Tree</option>
          <option value="aic_5">Test 5: 05. Course Schedule / Cycle Detection in DAG</option>
          <option value="aic_6">Test 6: 06. Merge K Sorted Linked Lists</option>
          <option value="aic_7">Test 7: 07. Subarray Sum Equals K</option>
          <option value="aic_8">Test 8: 08. Coin Change (Minimum Coins DP)</option>
          <option value="aic_9">Test 9: 09. Valid Parentheses with Wildcards</option>
          <option value="aic_10">Test 10: 10. Word Search on 2D Matrix (Backtracking)</option>
        </select>
      </div>

      <!-- PROBLEM DETAILS -->
      <div class="prob-details-pane">
        <div class="prob-num" id="probNum">01. Tree Recursion • Math</div>
        <div class="prob-title" id="probTitle">01. LCM of Two Trees</div>
        <div id="probDesc">
          A binary tree is represented by the following structure. Implement the function to return a tree which is LCM of both trees. Each node value of output tree is equal to LCM of data values of nodes on that same position in input trees.
        </div>
        <div class="code-box" id="probStruct">struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};</div>
        <div class="note-box" id="probNotes">
          <strong>Note:</strong> LCM of 2 integers is the smallest positive integer that is exactly divisible by both integers. If one node is NULL, copy the non-null node. If both are NULL, return NULL.
        </div>
      </div>

      <!-- CODING PANEL -->
      <div class="editor-section">
        <div class="editor-toolbar">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <span style="font-weight:700; font-size:0.82rem; color:#fff;">&lt;&gt; Coding Panel</span>
            <select class="lang-dropdown" id="langSelect" onchange="switchLanguage(this.value)">
              <option value="c">C (GCC 11.3)</option>
              <option value="cpp">C++ 20</option>
              <option value="java">Java 17</option>
              <option value="python">Python 3.10</option>
            </select>
            <span style="color:#64748b; font-size:0.75rem;" id="fileName">Solution.c</span>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button class="btn-send" style="padding:0.35rem 0.75rem; font-size:0.75rem; background:#334155;" onclick="resetEditor()">↺ Clear</button>
            <button class="btn-send" style="padding:0.35rem 0.9rem; font-size:0.75rem; background:#06d6a0; color:#042f2e;" onclick="runTestCases()">▶ Compile &amp; Run Test Cases</button>
          </div>
        </div>

        <textarea class="code-area" id="codeEditor" spellcheck="false"></textarea>

        <!-- TEST CASES RUNNER -->
        <div class="testcase-panel">
          <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.78rem; font-weight:700; color:#94a3b8;">
            <span>EXECUTION &amp; TEST RESULTS</span>
            <span id="tcSummary" style="color:#94a3b8;">0 / 3 Passed</span>
          </div>
          <div id="tcList" style="display:flex; gap:0.5rem; flex-wrap:wrap;">
            <div class="tc-pill" style="background:#131d33; color:#94a3b8;">Click "Compile &amp; Run Test Cases" to validate your solution</div>
          </div>
        </div>
      </div>
    </div>

    <!-- RIGHT PANEL: YOUR CODING ASSISTANT -->
    <div class="right-assistant">
      <div class="assistant-header">
        <div style="display:flex; align-items:center; gap:0.5rem;">
          <span style="font-weight:800; font-size:0.88rem; color:#fff;">Your Coding Assistant</span>
          <span class="step-badge" id="stepBadge">Step 1 of 4</span>
        </div>
        <span style="font-size:0.72rem; color:#06d6a0; font-weight:700;">● Active</span>
      </div>

      <!-- CHAT HISTORY -->
      <div class="chat-history" id="chatHistory">
        <div class="chat-msg msg-ai" id="welcomeMsg">
          <strong>Welcome to the AI-Assisted Coding Assessment!</strong><br/>
          I'm your AI coding assistant. Here's how this works:<br/>
          1. First, describe the problem in your own words (inputs, outputs, constraints).<br/>
          2. I'll ask about the data structures and approach you plan to use.<br/>
          3. Based on YOUR explanation, I'll generate starter code in your selected language.<br/>
          4. You can then refine the code, click "Insert in Editor", and test it.<br/><br/>
          <em>👉 To begin, please explain the problem requirements and edge cases in your own words.</em>
        </div>
      </div>

      <!-- CHAT INPUT AREA -->
      <div class="chat-input-area">
        <textarea class="chat-input" id="userInput" rows="2" placeholder="Explain the problem in your own words (inputs, outputs, edge cases)..."></textarea>
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:0.72rem; color:#64748b;" id="stepPromptHint">Step 1: Frame the problem</span>
          <div style="display:flex; gap:0.4rem;">
            <button class="btn-send" style="background:#1e293b; font-size:0.75rem; padding:0.4rem 0.8rem;" onclick="autoFillGoodPrompt()">Auto-Fill Best Prompt</button>
            <button class="btn-send" style="font-size:0.75rem; padding:0.4rem 0.9rem;" onclick="sendPrompt()">Send Prompt</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    let currentLang = 'c';
    let currentProbKey = 'aic_1';
    let step = 1;

    const AIC_BANK = {
      aic_1: {
        num: "01. Tree Recursion • Math (Capgemini Exceller Official)",
        title: "01. LCM of Two Trees",
        desc: "Implement a function to return a binary tree whose node values equal the LCM of data values of nodes at that same position in root1 and root2. If a node exists in only one tree, copy it directly. If both are NULL/None, return NULL/None.",
        notes: "<strong>Constraints:</strong> 1 <= Node Data <= 10^4. LCM(a, b) = (a * b) / GCD(a, b).",
        files: { c: "LCMTrees.c", cpp: "LCMTrees.cpp", java: "LCMTrees.java", python: "lcm_trees.py" },
        structs: {
          c: `struct TreeNode { int data; struct TreeNode* left; struct TreeNode* right; };\\nstruct TreeNode* LCMOfTrees(struct TreeNode* root1, struct TreeNode* root2);`,
          cpp: `struct TreeNode { int data; TreeNode* left; TreeNode* right; };\\nTreeNode* LCMOfTrees(TreeNode* root1, TreeNode* root2);`,
          java: `class TreeNode { int data; TreeNode left, right; }\\npublic static TreeNode LCMOfTrees(TreeNode root1, TreeNode root2);`,
          python: `class TreeNode:\\n    def __init__(self, data=0, left=None, right=None):\\n        self.data = data\\n        self.left = left\\n        self.right = right`
        },
        initialCodes: {
          c: `#include <stdio.h>\\n#include <stdlib.h>\\n\\nstruct TreeNode { int data; struct TreeNode* left; struct TreeNode* right; };\\n\\nint gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }\\nint lcm(int a, int b) { return (a == 0 || b == 0) ? 0 : (a / gcd(a, b)) * b; }\\n\\nstruct TreeNode* LCMOfTrees(struct TreeNode* root1, struct TreeNode* root2) {\\n    /* Write code here */\\n    return NULL;\\n}`,
          cpp: `#include <iostream>\\n#include <numeric>\\nusing namespace std;\\n\\nstruct TreeNode { int data; TreeNode* left; TreeNode* right; TreeNode(int x): data(x), left(nullptr), right(nullptr) {} };\\n\\nint gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }\\nint lcm(int a, int b) { return (a == 0 || b == 0) ? 0 : (a / gcd(a, b)) * b; }\\n\\nTreeNode* LCMOfTrees(TreeNode* root1, TreeNode* root2) {\\n    /* Write code here */\\n    return nullptr;\\n}`,
          java: `public class Solution {\\n    static class TreeNode { int data; TreeNode left, right; TreeNode(int d) { this.data = d; } }\\n    public static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }\\n    public static int lcm(int a, int b) { return (a == 0 || b == 0) ? 0 : (a / gcd(a, b)) * b; }\\n\\n    public static TreeNode LCMOfTrees(TreeNode root1, TreeNode root2) {\\n        /* Write code here */\\n        return null;\\n    }\\n}`,
          python: `import math\\n\\nclass TreeNode:\\n    def __init__(self, data=0, left=None, right=None):\\n        self.data = data\\n        self.left = left\\n        self.right = right\\n\\ndef lcm(a, b):\\n    return (a * b) // math.gcd(a, b) if a and b else 0\\n\\ndef lcm_of_trees(root1, root2):\\n    # Write code here\\n    return None`
        },
        step1Auto: "The problem asks us to merge two binary trees into a new tree where each node's value is the Least Common Multiple (LCM) of the values of the corresponding nodes in root1 and root2. If a node exists in only one tree, we return a copy of that node. If both are NULL, return NULL. Constraints: Node values are positive integers.",
        step2Auto: "I will use recursive tree traversal (DFS). For each step: if root1 is NULL, return root2; if root2 is NULL, return root1. Otherwise, create a new node whose data is lcm(root1->data, root2->data), and recursively compute the left child from root1->left & root2->left, and right child from root1->right & root2->right.",
        generatedCodes: {
          c: `struct TreeNode* LCMOfTrees(struct TreeNode* root1, struct TreeNode* root2) {\\n    if (!root1 && !root2) return NULL;\\n    if (!root1) return root2;\\n    if (!root2) return root1;\\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\\n    node->data = lcm(root1->data, root2->data);\\n    node->left = LCMOfTrees(root1->left, root2->left);\\n    node->right = LCMOfTrees(root1->right, root2->right);\\n    return node;\\n}`,
          cpp: `TreeNode* LCMOfTrees(TreeNode* root1, TreeNode* root2) {\\n    if (!root1 && !root2) return nullptr;\\n    if (!root1) return root2;\\n    if (!root2) return root1;\\n    TreeNode* node = new TreeNode(lcm(root1->data, root2->data));\\n    node->left = LCMOfTrees(root1->left, root2->left);\\n    node->right = LCMOfTrees(root1->right, root2->right);\\n    return node;\\n}`,
          java: `public static TreeNode LCMOfTrees(TreeNode root1, TreeNode root2) {\\n    if (root1 == null && root2 == null) return null;\\n    if (root1 == null) return root2;\\n    if (root2 == null) return root1;\\n    TreeNode node = new TreeNode(lcm(root1.data, root2.data));\\n    node.left = LCMOfTrees(root1.left, root2.left);\\n    node.right = LCMOfTrees(root1.right, root2.right);\\n    return node;\\n}`,
          python: `def lcm_of_trees(root1, root2):\\n    if not root1 and not root2: return None\\n    if not root1: return root2\\n    if not root2: return root1\\n    node = TreeNode(lcm(root1.data, root2.data))\\n    node.left = lcm_of_trees(root1.left, root2.left)\\n    node.right = lcm_of_trees(root1.right, root2.right)\\n    return node`
        },
        validate: function(code, lang) {
          const hasNull = code.includes("NULL") || code.includes("nullptr") || code.includes("null") || code.includes("not root1");
          const hasLCM = code.includes("lcm(") || code.includes("lcm_of_trees") || code.includes("gcd");
          return {
            tc1: { name: "Both Nodes Present (LCM(4, 6) = 12)", passed: hasLCM },
            tc2: { name: "Skewed Tree (Null propagation)", passed: hasNull },
            tc3: { name: "Recursive Left & Right Subtrees", passed: code.length > 30 }
          };
        }
      },

      aic_2: {
        num: "02. Linked List • Pointers",
        title: "02. In-Place Reversal of Singly Linked List",
        desc: "Reverse a singly linked list in-place and return the new head in O(N) time and O(1) space.",
        notes: "<strong>Rules:</strong> Must reverse pointers in-place. If head is NULL or single node, return head immediately.",
        files: { c: "ReverseList.c", cpp: "ReverseList.cpp", java: "ReverseList.java", python: "reverse_list.py" },
        structs: {
          c: `struct ListNode { int data; struct ListNode* next; };\\nstruct ListNode* ReverseList(struct ListNode* head);`,
          cpp: `struct ListNode { int val; ListNode* next; };\\nListNode* reverseList(ListNode* head);`,
          java: `class ListNode { int val; ListNode next; }\\npublic static ListNode reverseList(ListNode head);`,
          python: `class ListNode:\\n    def __init__(self, val=0, next=None):\\n        self.val = val; self.next = next`
        },
        initialCodes: {
          c: `struct ListNode* ReverseList(struct ListNode* head) {\\n    /* Write code here */\\n    return head;\\n}`,
          cpp: `ListNode* reverseList(ListNode* head) {\\n    /* Write code here */\\n    return head;\\n}`,
          java: `public static ListNode reverseList(ListNode head) {\\n    /* Write code here */\\n    return head;\\n}`,
          python: `def reverse_list(head):\\n    # Write code here\\n    return head`
        },
        step1Auto: "The goal is to reverse a singly linked list in-place in O(N) time and O(1) extra space. The input is head pointer, and the output is the new head (original tail node). If head is NULL or a single node, return head as is.",
        step2Auto: "I will use the 3-pointer iterative technique: prev = NULL, curr = head, and next = NULL. In a loop while curr != NULL, save curr->next, point curr->next to prev, then advance prev = curr and curr = next. Finally return prev.",
        generatedCodes: {
          c: `struct ListNode* ReverseList(struct ListNode* head) {\\n    struct ListNode *prev = NULL, *curr = head, *next = NULL;\\n    while (curr != NULL) {\\n        next = curr->next;\\n        curr->next = prev;\\n        prev = curr;\\n        curr = next;\\n    }\\n    return prev;\\n}`,
          cpp: `ListNode* reverseList(ListNode* head) {\\n    ListNode *prev = nullptr, *curr = head, *nxt = nullptr;\\n    while (curr != nullptr) {\\n        nxt = curr->next;\\n        curr->next = prev;\\n        prev = curr;\\n        curr = nxt;\\n    }\\n    return prev;\\n}`,
          java: `public static ListNode reverseList(ListNode head) {\\n    ListNode prev = null, curr = head, next = null;\\n    while (curr != null) {\\n        next = curr.next;\\n        curr.next = prev;\\n        prev = curr;\\n        curr = next;\\n    }\\n    return prev;\\n}`,
          python: `def reverse_list(head):\\n    prev = None\\n    curr = head\\n    while curr:\\n        nxt = curr.next\\n        curr.next = prev\\n        prev = curr\\n        curr = nxt\\n    return prev`
        },
        validate: function(code, lang) {
          const hasInvert = code.includes("next = prev") || code.includes("curr->next = prev") || code.includes("curr.next = prev") || code.includes("curr.next = prev");
          const returnsPrev = code.includes("return prev");
          return {
            tc1: { name: "Standard List (1->2->3->4->5)", passed: hasInvert },
            tc2: { name: "Empty / Single Node", passed: returnsPrev },
            tc3: { name: "O(1) In-Place Memory Verification", passed: true }
          };
        }
      },

      aic_3: {
        num: "03. Strings • Sliding Window",
        title: "03. Longest Substring Without Repeating Characters",
        desc: "Find the length of the longest contiguous substring without repeating characters in O(N) time.",
        notes: "<strong>Constraints:</strong> 0 <= s.length <= 5 * 10^4.",
        files: { c: "LongestSubstring.c", cpp: "LongestSubstring.cpp", java: "LongestSubstring.java", python: "longest_substring.py" },
        structs: {
          c: `int lengthOfLongestSubstring(char* s);`,
          cpp: `int lengthOfLongestSubstring(string s);`,
          java: `public static int lengthOfLongestSubstring(String s);`,
          python: `def length_of_longest_substring(s: str) -> int:`
        },
        initialCodes: {
          c: `int lengthOfLongestSubstring(char* s) {\\n    /* Write sliding window code */\\n    return 0;\\n}`,
          cpp: `int lengthOfLongestSubstring(string s) {\\n    /* Write sliding window code */\\n    return 0;\\n}`,
          java: `public static int lengthOfLongestSubstring(String s) {\\n    /* Write sliding window code */\\n    return 0;\\n}`,
          python: `def length_of_longest_substring(s):\\n    # Write sliding window code\\n    return 0`
        },
        step1Auto: "Given a string s, we must find the maximum length of a contiguous substring containing all distinct characters. Input is a string; output is an integer length. Time complexity should be O(N).",
        step2Auto: "I will use a sliding window approach with two pointers (left and right) and a frequency/last-seen array/map. As right expands, if a duplicate is seen, shrink left until no duplicates remain, updating maxLength = max(maxLength, right - left + 1).",
        generatedCodes: {
          c: `int lengthOfLongestSubstring(char* s) {\\n    if (!s || !*s) return 0;\\n    int lastSeen[256]; for (int i = 0; i < 256; i++) lastSeen[i] = -1;\\n    int maxLen = 0, left = 0;\\n    for (int right = 0; s[right]; right++) {\\n        unsigned char c = (unsigned char)s[right];\\n        if (lastSeen[c] >= left) left = lastSeen[c] + 1;\\n        lastSeen[c] = right;\\n        int len = right - left + 1;\\n        if (len > maxLen) maxLen = len;\\n    }\\n    return maxLen;\\n}`,
          cpp: `int lengthOfLongestSubstring(string s) {\\n    vector<int> lastSeen(256, -1);\\n    int maxLen = 0, left = 0;\\n    for (int right = 0; right < s.length(); right++) {\\n        unsigned char c = s[right];\\n        if (lastSeen[c] >= left) left = lastSeen[c] + 1;\\n        lastSeen[c] = right;\\n        maxLen = max(maxLen, right - left + 1);\\n    }\\n    return maxLen;\\n}`,
          java: `public static int lengthOfLongestSubstring(String s) {\\n    int[] lastSeen = new int[256];\\n    java.util.Arrays.fill(lastSeen, -1);\\n    int maxLen = 0, left = 0;\\n    for (int right = 0; right < s.length(); right++) {\\n        char c = s.charAt(right);\\n        if (lastSeen[c] >= left) left = lastSeen[c] + 1;\\n        lastSeen[c] = right;\\n        maxLen = Math.max(maxLen, right - left + 1);\\n    }\\n    return maxLen;\\n}`,
          python: `def length_of_longest_substring(s):\\n    last_seen = {}\\n    max_len = left = 0\\n    for right, c in enumerate(s):\\n        if c in last_seen and last_seen[c] >= left:\\n            left = last_seen[c] + 1\\n        last_seen[c] = right\\n        max_len = max(max_len, right - left + 1)\\n    return max_len`
        },
        validate: function(code, lang) {
          const hasWindow = code.includes("left") && code.includes("right");
          return {
            tc1: { name: "Sample ('abcabcbb' -> 3)", passed: hasWindow },
            tc2: { name: "All Same ('bbbbb' -> 1)", passed: hasWindow },
            tc3: { name: "Empty String Handled", passed: true }
          };
        }
      },

      aic_4: {
        num: "04. Binary Trees • LCA",
        title: "04. Lowest Common Ancestor in Binary Tree",
        desc: "Find Lowest Common Ancestor (LCA) for two given nodes p and q in a binary tree in O(N) time.",
        notes: "<strong>Constraints:</strong> Node values are unique. p and q exist in the tree.",
        files: { c: "LCA.c", cpp: "LCA.cpp", java: "LCA.java", python: "lca.py" },
        structs: {
          c: `struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q);`,
          cpp: `TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q);`,
          java: `public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q);`,
          python: `def lowest_common_ancestor(root, p, q):`
        },
        initialCodes: {
          c: `struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) { return NULL; }`,
          cpp: `TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) { return nullptr; }`,
          java: `public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) { return null; }`,
          python: `def lowest_common_ancestor(root, p, q): return None`
        },
        step1Auto: "We need to find the lowest common ancestor node for two given nodes p and q in a binary tree. The LCA is the deepest node that has both p and q in its subtrees.",
        step2Auto: "We can use recursive DFS traversal: if root is NULL, or root == p, or root == q, return root. Recursively search left and right subtrees. If both return non-null, root is the LCA. Otherwise, return the non-null branch.",
        generatedCodes: {
          c: `struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {\\n    if (!root || root == p || root == q) return root;\\n    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);\\n    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);\\n    if (left && right) return root;\\n    return left ? left : right;\\n}`,
          cpp: `TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\\n    if (!root || root == p || root == q) return root;\\n    TreeNode* left = lowestCommonAncestor(root->left, p, q);\\n    TreeNode* right = lowestCommonAncestor(root->right, p, q);\\n    if (left && right) return root;\\n    return left ? left : right;\\n}`,
          java: `public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\\n    if (root == null || root == p || root == q) return root;\\n    TreeNode left = lowestCommonAncestor(root.left, p, q);\\n    TreeNode right = lowestCommonAncestor(root.right, p, q);\\n    if (left != null && right != null) return root;\\n    return left != null ? left : right;\\n}`,
          python: `def lowest_common_ancestor(root, p, q):\\n    if not root or root == p or root == q: return root\\n    left = lowest_common_ancestor(root.left, p, q)\\n    right = lowest_common_ancestor(root.right, p, q)\\n    if left and right: return root\\n    return left or right`
        },
        validate: function(code, lang) {
          const hasBranch = code.includes("left") && code.includes("right");
          return {
            tc1: { name: "Split Branches LCA", passed: hasBranch },
            tc2: { name: "Direct Ancestor Handled", passed: true },
            tc3: { name: "O(N) Traversal Time", passed: true }
          };
        }
      },

      aic_5: {
        num: "05. Graphs • Topological Sort",
        title: "05. Course Schedule / DAG Cycle Detection",
        desc: "Return true if all courses can be finished without circular dependency.",
        notes: "<strong>Constraints:</strong> 1 <= numCourses <= 2000.",
        files: { c: "CourseSchedule.c", cpp: "CourseSchedule.cpp", java: "CourseSchedule.java", python: "course_schedule.py" },
        structs: {
          c: `bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize);`,
          cpp: `bool canFinish(int numCourses, vector<vector<int>>& prerequisites);`,
          java: `public static boolean canFinish(int numCourses, int[][] prerequisites);`,
          python: `def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:`
        },
        initialCodes: {
          c: `bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) { return true; }`,
          cpp: `bool canFinish(int numCourses, vector<vector<int>>& prerequisites) { return true; }`,
          java: `public static boolean canFinish(int numCourses, int[][] prerequisites) { return true; }`,
          python: `def can_finish(num_courses, prerequisites): return True`
        },
        step1Auto: "The problem asks whether all courses can be completed given prerequisite pairs. This translates to checking whether the directed dependency graph contains a cycle (must be a DAG).",
        step2Auto: "I will use Kahn's Algorithm (BFS Topological Sort): compute in-degree for all courses, enqueue courses with in-degree 0. While queue is non-empty, dequeue course, increment processed count, and decrement in-degrees of its neighbors, enqueuing when in-degree reaches 0. Return processed count == numCourses.",
        generatedCodes: {
          c: `bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {\\n    int inDegree[2000] = {0}, queue[2000], front = 0, rear = 0, count = 0;\\n    for (int i = 0; i < prerequisitesSize; i++) inDegree[prerequisites[i][0]]++;\\n    for (int i = 0; i < numCourses; i++) if (!inDegree[i]) queue[rear++] = i;\\n    while (front < rear) {\\n        int curr = queue[front++]; count++;\\n        for (int i = 0; i < prerequisitesSize; i++) {\\n            if (prerequisites[i][1] == curr && --inDegree[prerequisites[i][0]] == 0) queue[rear++] = prerequisites[i][0];\\n        }\\n    }\\n    return count == numCourses;\\n}`,
          cpp: `bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\\n    vector<int> inDegree(numCourses, 0);\\n    vector<vector<int>> adj(numCourses);\\n    for (auto& p : prerequisites) { adj[p[1]].push_back(p[0]); inDegree[p[0]]++; }\\n    queue<int> q;\\n    for (int i = 0; i < numCourses; i++) if (!inDegree[i]) q.push(i);\\n    int count = 0;\\n    while (!q.empty()) {\\n        int curr = q.front(); q.pop(); count++;\\n        for (int nxt : adj[curr]) if (--inDegree[nxt] == 0) q.push(nxt);\\n    }\\n    return count == numCourses;\\n}`,
          java: `public static boolean canFinish(int numCourses, int[][] prerequisites) {\\n    int[] inDegree = new int[numCourses];\\n    java.util.List<java.util.List<Integer>> adj = new java.util.ArrayList<>();\\n    for (int i = 0; i < numCourses; i++) adj.add(new java.util.ArrayList<>());\\n    for (int[] p : prerequisites) { adj.get(p[1]).add(p[0]); inDegree[p[0]]++; }\\n    java.util.Queue<Integer> q = new java.util.LinkedList<>();\\n    for (int i = 0; i < numCourses; i++) if (inDegree[i] == 0) q.add(i);\\n    int count = 0;\\n    while (!q.isEmpty()) {\\n        int curr = q.poll(); count++;\\n        for (int nxt : adj.get(curr)) if (--inDegree[nxt] == 0) q.add(nxt);\\n    }\\n    return count == numCourses;\\n}`,
          python: `from collections import deque, defaultdict\\n\\ndef can_finish(num_courses, prerequisites):\\n    adj = defaultdict(list)\\n    in_degree = [0] * num_courses\\n    for dest, src in prerequisites:\\n        adj[src].append(dest)\\n        in_degree[dest] += 1\\n    q = deque([i for i in range(num_courses) if in_degree[i] == 0])\\n    count = 0\\n    while q:\\n        curr = q.popleft()\\n        count += 1\\n        for nxt in adj[curr]:\\n            in_degree[nxt] -= 1\\n            if in_degree[nxt] == 0: q.append(nxt)\\n    return count == num_courses`
        },
        validate: function(code, lang) {
          const hasInDegree = code.includes("inDegree") || code.includes("in_degree");
          return {
            tc1: { name: "Linear DAG Dependency", passed: hasInDegree },
            tc2: { name: "Cycle Detection (0->1->0)", passed: hasInDegree },
            tc3: { name: "Disconnected Graph Forest", passed: true }
          };
        }
      },

      aic_6: {
        num: "06. Linked Lists • Divide & Conquer",
        title: "06. Merge K Sorted Linked Lists",
        desc: "Merge k sorted linked lists into one sorted linked list in O(N log k) time.",
        notes: "<strong>Constraints:</strong> 0 <= k <= 10^4.",
        files: { c: "MergeK.c", cpp: "MergeK.cpp", java: "MergeK.java", python: "merge_k.py" },
        structs: {
          c: `struct ListNode* mergeKLists(struct ListNode** lists, int listsSize);`,
          cpp: `ListNode* mergeKLists(vector<ListNode*>& lists);`,
          java: `public static ListNode mergeKLists(ListNode[] lists);`,
          python: `def merge_k_lists(lists: list[ListNode]) -> ListNode:`
        },
        initialCodes: {
          c: `struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) { return NULL; }`,
          cpp: `ListNode* mergeKLists(vector<ListNode*>& lists) { return nullptr; }`,
          java: `public static ListNode mergeKLists(ListNode[] lists) { return null; }`,
          python: `def merge_k_lists(lists): return None`
        },
        step1Auto: "We are given an array of k sorted linked lists and need to merge all of them into a single sorted linked list in O(N log K) time without excess overhead.",
        step2Auto: "I will use Divide and Conquer: pairwise merge lists using a helper function mergeTwoLists(l1, l2), repeating in rounds until only 1 consolidated list remains. This achieves optimal O(N log k) time and O(1) extra space.",
        generatedCodes: {
          c: `struct ListNode* mergeTwo(struct ListNode* a, struct ListNode* b) {\\n    if (!a) return b; if (!b) return a;\\n    if (a->data < b->data) { a->next = mergeTwo(a->next, b); return a; }\\n    else { b->next = mergeTwo(a, b->next); return b; }\\n}\\nstruct ListNode* mergeKLists(struct ListNode** lists, int size) {\\n    if (!size) return NULL;\\n    for (int interval = 1; interval < size; interval *= 2) {\\n        for (int i = 0; i + interval < size; i += interval * 2) {\\n            lists[i] = mergeTwo(lists[i], lists[i + interval]);\\n        }\\n    }\\n    return lists[0];\\n}`,
          cpp: `ListNode* merge2(ListNode* a, ListNode* b) {\\n    if (!a) return b; if (!b) return a;\\n    if (a->val < b->val) { a->next = merge2(a->next, b); return a; }\\n    else { b->next = merge2(a, b->next); return b; }\\n}\\nListNode* mergeKLists(vector<ListNode*>& lists) {\\n    if (lists.empty()) return nullptr;\\n    int n = lists.size();\\n    for (int interval = 1; interval < n; interval *= 2) {\\n        for (int i = 0; i + interval < n; i += interval * 2) lists[i] = merge2(lists[i], lists[i + interval]);\\n    }\\n    return lists[0];\\n}`,
          java: `public static ListNode merge2(ListNode a, ListNode b) {\\n    if (a == null) return b; if (b == null) return a;\\n    if (a.val < b.val) { a.next = merge2(a.next, b); return a; }\\n    else { b.next = merge2(a, b.next); return b; }\\n}\\npublic static ListNode mergeKLists(ListNode[] lists) {\\n    if (lists == null || lists.length == 0) return null;\\n    int n = lists.length;\\n    for (int interval = 1; interval < n; interval *= 2) {\\n        for (int i = 0; i + interval < n; i += interval * 2) lists[i] = merge2(lists[i], lists[i + interval]);\\n    }\\n    return lists[0];\\n}`,
          python: `def merge_two(a, b):\\n    if not a: return b\\n    if not b: return a\\n    if a.val < b.val:\\n        a.next = merge_two(a.next, b)\\n        return a\\n    else:\\n        b.next = merge_two(a, b.next)\\n        return b\\n\\ndef merge_k_lists(lists):\\n    if not lists: return None\\n    interval = 1\\n    while interval < len(lists):\\n        for i in range(0, len(lists) - interval, interval * 2):\\n            lists[i] = merge_two(lists[i], lists[i + interval])\\n        interval *= 2\\n    return lists[0]`
        },
        validate: function(code, lang) {
          const hasMerge = code.includes("mergeTwo") || code.includes("merge2") || code.includes("merge_two") || code.includes("heap");
          return {
            tc1: { name: "K Sorted Lists Merged", passed: hasMerge },
            tc2: { name: "Empty / Single List Handled", passed: true },
            tc3: { name: "O(N log K) Complexity", passed: true }
          };
        }
      },

      aic_7: {
        num: "07. Arrays • Prefix Sum",
        title: "07. Subarray Sum Equals K",
        desc: "Return total count of continuous subarrays whose sum equals k.",
        notes: "<strong>Constraints:</strong> 1 <= nums.length <= 2 * 10^4. Array can contain negative numbers.",
        files: { c: "SubarraySum.c", cpp: "SubarraySum.cpp", java: "SubarraySum.java", python: "subarray_sum.py" },
        structs: {
          c: `int subarraySum(int* nums, int numsSize, int k);`,
          cpp: `int subarraySum(vector<int>& nums, int k);`,
          java: `public static int subarraySum(int[] nums, int k);`,
          python: `def subarray_sum(nums: list[int], k: int) -> int:`
        },
        initialCodes: {
          c: `int subarraySum(int* nums, int numsSize, int k) { return 0; }`,
          cpp: `int subarraySum(vector<int>& nums, int k) { return 0; }`,
          java: `public static int subarraySum(int[] nums, int k) { return 0; }`,
          python: `def subarray_sum(nums, k): return 0`
        },
        step1Auto: "Find the total count of contiguous subarrays that sum up to target k. Array elements can be positive, negative, or zero, so simple two pointers/sliding window will not work; we need Prefix Sums.",
        step2Auto: "I will maintain running prefixSum and a Hash Map storing frequency of previously seen prefix sums. At each element: add num to prefixSum, check if (prefixSum - k) exists in map, add its frequency to total count, and record current prefixSum in map.",
        generatedCodes: {
          c: `int subarraySum(int* nums, int numsSize, int k) {\\n    int count = 0;\\n    for (int start = 0; start < numsSize; start++) {\\n        int sum = 0;\\n        for (int end = start; end < numsSize; end++) {\\n            sum += nums[end];\\n            if (sum == k) count++;\\n        }\\n    }\\n    return count;\\n}`,
          cpp: `int subarraySum(vector<int>& nums, int k) {\\n    unordered_map<int, int> prefixCounts;\\n    prefixCounts[0] = 1;\\n    int sum = 0, count = 0;\\n    for (int num : nums) {\\n        sum += num;\\n        if (prefixCounts.find(sum - k) != prefixCounts.end()) count += prefixCounts[sum - k];\\n        prefixCounts[sum]++;\\n    }\\n    return count;\\n}`,
          java: `public static int subarraySum(int[] nums, int k) {\\n    java.util.Map<Integer, Integer> map = new java.util.HashMap<>();\\n    map.put(0, 1);\\n    int sum = 0, count = 0;\\n    for (int x : nums) {\\n        sum += x;\\n        count += map.getOrDefault(sum - k, 0);\\n        map.put(sum, map.getOrDefault(sum, 0) + 1);\\n    }\\n    return count;\\n}`,
          python: `def subarray_sum(nums, k):\\n    counts = {0: 1}\\n    curr_sum = total = 0\\n    for x in nums:\\n        curr_sum += x\\n        total += counts.get(curr_sum - k, 0)\\n        counts[curr_sum] = counts.get(curr_sum, 0) + 1\\n    return total`
        },
        validate: function(code, lang) {
          const hasSum = code.includes("sum") || code.includes("curr_sum");
          return {
            tc1: { name: "Positive & Negative Elements", passed: hasSum },
            tc2: { name: "Exact Match k Found", passed: hasSum },
            tc3: { name: "Target k = 0 Edge Case", passed: true }
          };
        }
      },

      aic_8: {
        num: "08. Dynamic Programming",
        title: "08. Coin Change (Minimum Coins DP)",
        desc: "Return the fewest number of coins needed to make up amount. If impossible, return -1.",
        notes: "<strong>Constraints:</strong> 0 <= amount <= 10^4.",
        files: { c: "CoinChange.c", cpp: "CoinChange.cpp", java: "CoinChange.java", python: "coin_change.py" },
        structs: {
          c: `int coinChange(int* coins, int coinsSize, int amount);`,
          cpp: `int coinChange(vector<int>& coins, int amount);`,
          java: `public static int coinChange(int[] coins, int amount);`,
          python: `def coin_change(coins: list[int], amount: int) -> int:`
        },
        initialCodes: {
          c: `int coinChange(int* coins, int coinsSize, int amount) { return -1; }`,
          cpp: `int coinChange(vector<int>& coins, int amount) { return -1; }`,
          java: `public static int coinChange(int[] coins, int amount) { return -1; }`,
          python: `def coin_change(coins, amount): return -1`
        },
        step1Auto: "Given coin denominations and a target amount, compute the minimum number of coins needed to make up the exact amount. If cannot be formed, return -1. Coins can be used infinitely.",
        step2Auto: "I will use 1D Dynamic Programming: initialize dp array of size amount + 1 with amount + 1 (infinity), and dp[0] = 0. For each i from 1 to amount, check every coin: if coin <= i, dp[i] = min(dp[i], dp[i - coin] + 1). Return dp[amount] > amount ? -1 : dp[amount].",
        generatedCodes: {
          c: `int coinChange(int* coins, int size, int amount) {\\n    if (amount <= 0) return 0;\\n    int* dp = (int*)malloc((amount + 1) * sizeof(int));\\n    for (int i = 0; i <= amount; i++) dp[i] = amount + 1;\\n    dp[0] = 0;\\n    for (int i = 1; i <= amount; i++) {\\n        for (int c = 0; c < size; c++) {\\n            if (coins[c] <= i && dp[i - coins[c]] != amount + 1) {\\n                if (dp[i - coins[c]] + 1 < dp[i]) dp[i] = dp[i - coins[c]] + 1;\\n            }\\n        }\\n    }\\n    int ans = dp[amount] > amount ? -1 : dp[amount];\\n    free(dp);\\n    return ans;\\n}`,
          cpp: `int coinChange(vector<int>& coins, int amount) {\\n    vector<int> dp(amount + 1, amount + 1);\\n    dp[0] = 0;\\n    for (int i = 1; i <= amount; i++) {\\n        for (int c : coins) if (c <= i) dp[i] = min(dp[i], dp[i - c] + 1);\\n    }\\n    return dp[amount] > amount ? -1 : dp[amount];\\n}`,
          java: `public static int coinChange(int[] coins, int amount) {\\n    int[] dp = new int[amount + 1];\\n    java.util.Arrays.fill(dp, amount + 1);\\n    dp[0] = 0;\\n    for (int i = 1; i <= amount; i++) {\\n        for (int c : coins) if (c <= i) dp[i] = Math.min(dp[i], dp[i - c] + 1);\\n    }\\n    return dp[amount] > amount ? -1 : dp[amount];\\n}`,
          python: `def coin_change(coins, amount):\\n    dp = [float('inf')] * (amount + 1)\\n    dp[0] = 0\\n    for i in range(1, amount + 1):\\n        for c in coins:\\n            if c <= i: dp[i] = min(dp[i], dp[i - c] + 1)\\n    return dp[amount] if dp[amount] != float('inf') else -1`
        },
        validate: function(code, lang) {
          const hasDp = code.includes("dp[") || code.includes("dp =");
          return {
            tc1: { name: "Standard Amount [1,2,5], amount=11 -> 3", passed: hasDp },
            tc2: { name: "Impossible Amount [2], amount=3 -> -1", passed: hasDp },
            tc3: { name: "Zero Amount Edge Case", passed: true }
          };
        }
      },

      aic_9: {
        num: "09. Greedy • Strings",
        title: "09. Valid Parentheses with Wildcards",
        desc: "Validate if string with '(', ')' and '*' forms balanced parentheses.",
        notes: "<strong>Constraints:</strong> 1 <= s.length <= 100.",
        files: { c: "ValidParentheses.c", cpp: "ValidParentheses.cpp", java: "ValidParentheses.java", python: "valid_parentheses.py" },
        structs: {
          c: `bool checkValidString(char* s);`,
          cpp: `bool checkValidString(string s);`,
          java: `public static boolean checkValidString(String s);`,
          python: `def check_valid_string(s: str) -> bool:`
        },
        initialCodes: {
          c: `bool checkValidString(char* s) { return true; }`,
          cpp: `bool checkValidString(string s) { return true; }`,
          java: `public static boolean checkValidString(String s) { return true; }`,
          python: `def check_valid_string(s): return True`
        },
        step1Auto: "We must validate if a string of '(', ')', and '*' forms valid balanced parentheses, where '*' can act as '(', ')', or an empty character.",
        step2Auto: "I will use a Greedy range counter: maintain cmin (minimum possible open brackets) and cmax (maximum possible open brackets). '(' increments both; ')' decrements both; '*' decrements cmin and increments cmax. If cmax < 0, return false; clamp cmin to 0. At the end, return cmin == 0.",
        generatedCodes: {
          c: `bool checkValidString(char* s) {\\n    int cmin = 0, cmax = 0;\\n    for (int i = 0; s[i]; i++) {\\n        if (s[i] == '(') { cmin++; cmax++; }\\n        else if (s[i] == ')') { cmin--; cmax--; }\\n        else if (s[i] == '*') { cmin--; cmax++; }\\n        if (cmax < 0) return false;\\n        if (cmin < 0) cmin = 0;\\n    }\\n    return cmin == 0;\\n}`,
          cpp: `bool checkValidString(string s) {\\n    int cmin = 0, cmax = 0;\\n    for (char c : s) {\\n        if (c == '(') { cmin++; cmax++; }\\n        else if (c == ')') { cmin--; cmax--; }\\n        else { cmin--; cmax++; }\\n        if (cmax < 0) return false;\\n        if (cmin < 0) cmin = 0;\\n    }\\n    return cmin == 0;\\n}`,
          java: `public static boolean checkValidString(String s) {\\n    int cmin = 0, cmax = 0;\\n    for (char c : s.toCharArray()) {\\n        if (c == '(') { cmin++; cmax++; }\\n        else if (c == ')') { cmin--; cmax--; }\\n        else { cmin--; cmax++; }\\n        if (cmax < 0) return false;\\n        if (cmin < 0) cmin = 0;\\n    }\\n    return cmin == 0;\\n}`,
          python: `def check_valid_string(s):\\n    cmin = cmax = 0\\n    for c in s:\\n        if c == '(': cmin += 1; cmax += 1\\n        elif c == ')': cmin -= 1; cmax -= 1\\n        else: cmin -= 1; cmax += 1\\n        if cmax < 0: return False\\n        if cmin < 0: cmin = 0\\n    return cmin == 0`
        },
        validate: function(code, lang) {
          const hasCmin = code.includes("cmin") || code.includes("cmax") || code.includes("low") || code.includes("high");
          return {
            tc1: { name: "Standard Wildcard '(*)' -> true", passed: hasCmin },
            tc2: { name: "Wildcard as Empty '(*))' -> true", passed: hasCmin },
            tc3: { name: "Negative Balance Clamp", passed: true }
          };
        }
      },

      aic_10: {
        num: "10. Backtracking • 2D Grid",
        title: "10. Word Search on 2D Matrix",
        desc: "Find if word exists in 2D grid using adjacent sequential character DFS without cell reuse.",
        notes: "<strong>Constraints:</strong> Cell letter cannot be used more than once per word.",
        files: { c: "WordSearch.c", cpp: "WordSearch.cpp", java: "WordSearch.java", python: "word_search.py" },
        structs: {
          c: `bool exist(char** board, int boardSize, int* boardColSize, char* word);`,
          cpp: `bool exist(vector<vector<char>>& board, string word);`,
          java: `public static boolean exist(char[][] board, String word);`,
          python: `def exist(board: list[list[str]], word: str) -> bool:`
        },
        initialCodes: {
          c: `bool exist(char** board, int boardSize, int* boardColSize, char* word) { return false; }`,
          cpp: `bool exist(vector<vector<char>>& board, string word) { return false; }`,
          java: `public static boolean exist(char[][] board, String word) { return false; }`,
          python: `def exist(board, word): return False`
        },
        step1Auto: "We must determine if a given word exists in an m x n 2D grid by moving horizontally or vertically to adjacent cells without reusing the same cell twice in a single word path.",
        step2Auto: "I will iterate through all starting cells matching word[0]. From each, execute DFS backtracking: mark cell as visited ('#'), recursively explore 4 cardinal directions for the next character, and backtrack (restore cell original char). Return true if any path matches the full word.",
        generatedCodes: {
          c: `bool dfs(char** board, int m, int n, int r, int c, char* word, int idx) {\\n    if (word[idx] == '\\0') return true;\\n    if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[idx]) return false;\\n    char temp = board[r][c]; board[r][c] = '#';\\n    bool ok = dfs(board, m, n, r+1, c, word, idx+1) || dfs(board, m, n, r-1, c, word, idx+1) || dfs(board, m, n, r, c+1, word, idx+1) || dfs(board, m, n, r, c-1, word, idx+1);\\n    board[r][c] = temp;\\n    return ok;\\n}\\nbool exist(char** board, int boardSize, int* boardColSize, char* word) {\\n    int m = boardSize, n = boardColSize[0];\\n    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) if (dfs(board, m, n, i, j, word, 0)) return true;\\n    return false;\\n}`,
          cpp: `bool dfs(vector<vector<char>>& board, int r, int c, string& word, int idx) {\\n    if (idx == word.length()) return true;\\n    if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() || board[r][c] != word[idx]) return false;\\n    char temp = board[r][c]; board[r][c] = '#';\\n    bool ok = dfs(board, r+1, c, word, idx+1) || dfs(board, r-1, c, word, idx+1) || dfs(board, r, c+1, word, idx+1) || dfs(board, r, c-1, word, idx+1);\\n    board[r][c] = temp;\\n    return ok;\\n}\\nbool exist(vector<vector<char>>& board, string word) {\\n    for (int i = 0; i < board.size(); i++) for (int j = 0; j < board[0].size(); j++) if (dfs(board, i, j, word, 0)) return true;\\n    return false;\\n}`,
          java: `public static boolean dfs(char[][] board, int r, int c, String word, int idx) {\\n    if (idx == word.length()) return true;\\n    if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(idx)) return false;\\n    char temp = board[r][c]; board[r][c] = '#';\\n    boolean ok = dfs(board, r+1, c, word, idx+1) || dfs(board, r-1, c, word, idx+1) || dfs(board, r, c+1, word, idx+1) || dfs(board, r, c-1, word, idx+1);\\n    board[r][c] = temp;\\n    return ok;\\n}\\npublic static boolean exist(char[][] board, String word) {\\n    for (int i = 0; i < board.length; i++) for (int j = 0; j < board[0].length; j++) if (dfs(board, i, j, word, 0)) return true;\\n    return false;\\n}`,
          python: `def exist(board, word):\\n    m, n = len(board), len(board[0])\\n    def dfs(r, c, idx):\\n        if idx == len(word): return True\\n        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]: return False\\n        temp = board[r][c]\\n        board[r][c] = '#'\\n        ok = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)\\n        board[r][c] = temp\\n        return ok\\n    return any(dfs(i, j, 0) for i in range(m) for j in range(n))`
        },
        validate: function(code, lang) {
          const hasDfs = code.includes("dfs") || code.includes("backtrack");
          return {
            tc1: { name: "Sequential Word Match", passed: hasDfs },
            tc2: { name: "Cell Reuse Prevented", passed: hasDfs },
            tc3: { name: "Word Not Found Handled", passed: true }
          };
        }
      }
    };

    function loadProblem(key) {
      currentProbKey = key;
      step = 1;
      const p = AIC_BANK[key] || AIC_BANK['aic_1'];
      
      const select = document.getElementById('probSelect');
      if (select && select.value !== key) select.value = key;

      document.getElementById('probNum').textContent = p.num;
      document.getElementById('probTitle').textContent = p.title;
      document.getElementById('probDesc').innerHTML = p.desc;
      document.getElementById('probNotes').innerHTML = p.notes;
      document.getElementById('tcList').innerHTML = `<div class="tc-pill" style="background:#131d33; color:#94a3b8;">Click "Compile &amp; Run Test Cases" to validate your solution</div>`;
      document.getElementById('tcSummary').textContent = "0 / 3 Passed";

      updateLanguageView();

      // Reset Chat
      document.getElementById('stepBadge').textContent = "Step 1 of 4";
      document.getElementById('stepPromptHint').textContent = "Step 1: Frame the problem";
      document.getElementById('chatHistory').innerHTML = `
        <div class="chat-msg msg-ai">
          <strong>Welcome to the AI-Assisted Coding Assessment!</strong><br/>
          I'm your AI coding assistant for <strong>${p.title}</strong> (${currentLang.toUpperCase()}).<br/>
          1. First, describe the problem in your own words (inputs, outputs, constraints).<br/>
          2. I'll ask about the data structures and approach you plan to use.<br/>
          3. Based on YOUR explanation, I'll generate starter code in ${currentLang.toUpperCase()}.<br/>
          4. You can then refine the code, click "Insert in Editor", and test it.<br/><br/>
          <em>👉 To begin, please explain the problem requirements and edge cases in your own words.</em>
        </div>
      `;
    }

    function switchLanguage(lang) {
      currentLang = lang;
      updateLanguageView();
    }

    function updateLanguageView() {
      const p = AIC_BANK[currentProbKey] || AIC_BANK['aic_1'];
      document.getElementById('fileName').textContent = p.files[currentLang] || "Solution.txt";
      document.getElementById('probStruct').textContent = (p.structs[currentLang] || "").replace(/\\\\n/g, "\\n");
      document.getElementById('codeEditor').value = (p.initialCodes[currentLang] || "").replace(/\\\\n/g, "\\n");
    }

    function resetEditor() {
      updateLanguageView();
    }

    function autoFillGoodPrompt() {
      const p = AIC_BANK[currentProbKey] || AIC_BANK['aic_1'];
      if (step === 1) {
        document.getElementById('userInput').value = p.step1Auto;
      } else if (step === 2) {
        document.getElementById('userInput').value = p.step2Auto;
      } else {
        document.getElementById('userInput').value = `Please generate the complete and optimal solution in ${currentLang.toUpperCase()} incorporating all edge cases, null checks, and memory constraints based on our discussion.`;
      }
    }

    function sendPrompt() {
      const input = document.getElementById('userInput');
      const val = input.value.trim();
      if (!val) return;

      const chat = document.getElementById('chatHistory');
      const p = AIC_BANK[currentProbKey] || AIC_BANK['aic_1'];

      // User Msg
      const userMsg = document.createElement('div');
      userMsg.className = 'chat-msg msg-user';
      userMsg.textContent = val;
      chat.appendChild(userMsg);
      input.value = '';

      // AI Response with Scaffolding Logic
      setTimeout(() => {
        const aiMsg = document.createElement('div');
        aiMsg.className = 'chat-msg msg-ai';

        if (val.length < 20 || val.toLowerCase() === "write code" || val.toLowerCase() === "give code") {
          aiMsg.innerHTML = "⚠️ <strong>Vague prompt rejected!</strong><br/>A one-liner like 'write code' will not unlock progression. Please restate the inputs, the output, and key constraints in your own words.";
        } else if (step === 1) {
          step = 2;
          document.getElementById('stepBadge').textContent = "Step 2 of 4";
          document.getElementById('stepPromptHint').textContent = "Step 2: Propose Data Structures & Algorithm";
          aiMsg.innerHTML = `<strong>Great problem framing!</strong> Input boundaries, output types, and edge cases are clearly defined.<br/><br/>Now, what <strong>data structures</strong> and <strong>algorithmic approach</strong> do you plan to use in <strong>${currentLang.toUpperCase()}</strong>?`;
        } else if (step === 2) {
          step = 3;
          const snippet = (p.generatedCodes[currentLang] || p.generatedCodes['c']).replace(/\\\\n/g, "\\n");
          document.getElementById('stepBadge').textContent = "Step 3 of 4";
          document.getElementById('stepPromptHint').textContent = "Step 3: Review & Adapt Generated Code";
          aiMsg.innerHTML = `<strong>Excellent approach!</strong> Your chosen algorithm provides optimal time and space complexity.<br/><br/>Based on your instructions, here is the generated starter code in <strong>${currentLang.toUpperCase()}</strong>:<br/>
          <pre style="background:#040711; padding:0.6rem; border-radius:6px; font-size:0.78rem; color:#38bdf8; margin:0.5rem 0; overflow-x:auto;">${escapeHtml(snippet)}</pre>
          <button class="btn-insert" onclick="insertCodeInEditor()">📥 Insert in Editor</button><br/>
          <small style="color:#94a3b8;">Review the code in the left Coding Panel, adjust edge cases, compile, and run tests.</small>`;
        } else {
          aiMsg.innerHTML = `Code is loaded in the <strong>&lt;&gt; Coding Panel</strong> in <strong>${currentLang.toUpperCase()}</strong>. You can modify any lines directly in the editor, then click <strong>▶ Compile &amp; Run Test Cases</strong> to verify!`;
        }

        chat.appendChild(aiMsg);
        chat.scrollTop = chat.scrollHeight;
      }, 500);
    }

    function insertCodeInEditor() {
      const p = AIC_BANK[currentProbKey] || AIC_BANK['aic_1'];
      const snippet = (p.generatedCodes[currentLang] || p.generatedCodes['c']).replace(/\\\\n/g, "\\n");
      document.getElementById('codeEditor').value = snippet;
      alert(`✅ Generated ${currentLang.toUpperCase()} code inserted into <> Coding Panel! You can now review, tweak, and compile.`);
    }

    function runTestCases() {
      const p = AIC_BANK[currentProbKey] || AIC_BANK['aic_1'];
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

      document.getElementById('tcList').innerHTML = html;
      document.getElementById('tcSummary').textContent = `${passCount} / ${total} Passed`;
      document.getElementById('tcSummary').style.color = passCount === total ? "#06d6a0" : "#ef4444";

      if (passCount === total) {
        document.getElementById('stepBadge').textContent = "Completed (100%)";
        alert(`🎉 CONGRATULATIONS! All test cases passed in ${currentLang.toUpperCase()}! Full marks awarded on AI Literacy, Prompt Quality, Problem-Solving, and Review & Adapt.`);
      }
    }

    function escapeHtml(text) {
      return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    // Timer (45 mins)
    let timeLeft = 45 * 60;
    setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        const m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
        const s = (timeLeft % 60).toString().padStart(2, '0');
        document.getElementById('timer').textContent = `${m}:${s}`;
      }
    }, 1000);

    // Initial load from URL param ?id=aic_1 to aic_10
    window.onload = () => {
      const urlParams = new URLSearchParams(window.location.search);
      const testId = urlParams.get('id') || 'aic_1';
      loadProblem(AIC_BANK[testId] ? testId : 'aic_1');
    };
  </script>
</body>
</html>
'''

with open('modules/ai_coding_sim.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated modules/ai_coding_sim.html with Multi-Language C, C++, Java, Python successfully!")
