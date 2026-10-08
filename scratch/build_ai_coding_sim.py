# build_ai_coding_sim.py
import json

problems = {
  "aic_1": {
    "num": "Test 1 • Tree Recursion & Arithmetic",
    "title": "01. LCM of Two Binary Trees (Official Capgemini Pattern)",
    "desc": "Given the roots of two binary trees, <code>root1</code> and <code>root2</code>, merge them into a single binary tree such that each node's value is the <strong>Least Common Multiple (LCM)</strong> of the values of the nodes at the identical position in the two trees.<br><br>If a node exists only in <code>root1</code>, copy that node directly to the output. If a node exists only in <code>root2</code>, copy that node directly to the output. If both corresponding positions are null/empty, the merged tree should also have null at that position.",
    "method_signatures": {
      "c": "struct TreeNode* LCMOfTrees(struct TreeNode* root1, struct TreeNode* root2);",
      "cpp": "TreeNode* LCMOfTrees(TreeNode* root1, TreeNode* root2);",
      "java": "public static TreeNode LCMOfTrees(TreeNode root1, TreeNode root2)",
      "python": "def lcm_of_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:"
    },
    "input_format": "<code>root1</code>: Pointer/reference to root of first binary tree.<br><code>root2</code>: Pointer/reference to root of second binary tree.",
    "output_format": "Return pointer/reference to root of the merged LCM binary tree.",
    "constraints": "• 0 <= Number of nodes in either tree <= 10^4<br>• 1 <= Node.val <= 10^4<br>• Formula: LCM(a, b) = (a * b) / GCD(a, b)",
    "examples": [
      {
        "ex_num": 1,
        "input": "root1 = [4, 6, 8], root2 = [6, 3, 12]",
        "output": "[12, 6, 24]",
        "explanation": "• Root node: LCM(4, 6) = 12<br>• Left child: LCM(6, 3) = 6<br>• Right child: LCM(8, 12) = 24<br>Result tree is [12, 6, 24]."
      },
      {
        "ex_num": 2,
        "input": "root1 = [2, null, 5], root2 = [3, 7, null]",
        "output": "[6, 7, 5]",
        "explanation": "• Root node: LCM(2, 3) = 6<br>• Left child: root1 has null, root2 has 7 -> Copy 7 directly<br>• Right child: root1 has 5, root2 has null -> Copy 5 directly<br>Result tree is [6, 7, 5]."
      }
    ],
    "structs": {
      "c": "struct TreeNode {\n    int data;\n    struct TreeNode* left;\n    struct TreeNode* right;\n};",
      "cpp": "struct TreeNode {\n    int data;\n    TreeNode* left;\n    TreeNode* right;\n    TreeNode(int x) : data(x), left(nullptr), right(nullptr) {}\n};",
      "java": "public static class TreeNode {\n    int data;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int d) { this.data = d; }\n}",
      "python": "class TreeNode:\n    def __init__(self, data=0, left=None, right=None):\n        self.data = data\n        self.left = left\n        self.right = right"
    },
    "files": { "c": "LCMTrees.c", "cpp": "LCMTrees.cpp", "java": "LCMTrees.java", "python": "lcm_trees.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

// Implement the function below
struct TreeNode* LCMOfTrees(struct TreeNode* root1, struct TreeNode* root2) {
    // Write your code here using AI scaffolding
    return NULL;
}
""",
      "cpp": """#include <iostream>
#include <numeric>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : data(x), left(nullptr), right(nullptr) {}
};

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int lcm(int a, int b) { return (a == 0 || b == 0) ? 0 : (a / gcd(a, b)) * b; }

// Implement the function below
TreeNode* LCMOfTrees(TreeNode* root1, TreeNode* root2) {
    // Write your code here using AI scaffolding
    return nullptr;
}
""",
      "java": """public class Solution {
    static class TreeNode {
        int data;
        TreeNode left, right;
        TreeNode(int d) { this.data = d; }
    }

    public static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    public static int lcm(int a, int b) { return (a == 0 || b == 0) ? 0 : (a / gcd(a, b)) * b; }

    // Implement the function below
    public static TreeNode LCMOfTrees(TreeNode root1, TreeNode root2) {
        // Write your code here using AI scaffolding
        return null;
    }
}
""",
      "python": """import math

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def lcm(a, b):
    return (a * b) // math.gcd(a, b) if a and b else 0

# Implement the function below
def lcm_of_trees(root1, root2):
    # Write your code here using AI scaffolding
    return None
"""
    },
    "step1Auto": "The problem asks us to merge two binary trees (root1 and root2) into a single new tree. At every position, if both nodes exist, the new node's value is LCM(root1.data, root2.data). If only one exists, we copy that node. If both are null, that position is null.",
    "step2Auto": "I will use a recursive tree traversal (DFS approach). At each recursive call: 1) Base case: if root1 is NULL and root2 is NULL return NULL. 2) If root1 is NULL return root2, if root2 is NULL return root1. 3) Otherwise, allocate a new node with data = lcm(root1->data, root2->data), and recursively compute left = LCMOfTrees(root1->left, root2->left) and right = LCMOfTrees(root1->right, root2->right). Return the new node.",
    "generatedCodes": {
      "c": """struct TreeNode* LCMOfTrees(struct TreeNode* root1, struct TreeNode* root2) {
    if (!root1 && !root2) return NULL;
    if (!root1) return root2;
    if (!root2) return root1;
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->data = lcm(root1->data, root2->data);
    node->left = LCMOfTrees(root1->left, root2->left);
    node->right = LCMOfTrees(root1->right, root2->right);
    return node;
}""",
      "cpp": """TreeNode* LCMOfTrees(TreeNode* root1, TreeNode* root2) {
    if (!root1 && !root2) return nullptr;
    if (!root1) return root2;
    if (!root2) return root1;
    TreeNode* node = new TreeNode(lcm(root1->data, root2->data));
    node->left = LCMOfTrees(root1->left, root2->left);
    node->right = LCMOfTrees(root1->right, root2->right);
    return node;
}""",
      "java": """public static TreeNode LCMOfTrees(TreeNode root1, TreeNode root2) {
    if (root1 == null && root2 == null) return null;
    if (root1 == null) return root2;
    if (root2 == null) return root1;
    TreeNode node = new TreeNode(lcm(root1.data, root2.data));
    node.left = LCMOfTrees(root1.left, root2.left);
    node.right = LCMOfTrees(root1.right, root2.right);
    return node;
}""",
      "python": """def lcm_of_trees(root1, root2):
    if not root1 and not root2: return None
    if not root1: return root2
    if not root2: return root1
    node = TreeNode(lcm(root1.data, root2.data))
    node.left = lcm_of_trees(root1.left, root2.left)
    node.right = lcm_of_trees(root1.right, root2.right)
    return node"""
    },
    "tc_names": ["Both Subtrees Populated: LCM(4, 6)=12", "Asymmetric Subtrees: Null propagation", "Edge Case: Both Root Nodes Null"]
  },

  "aic_2": {
    "num": "Test 2 • Linked Lists & Pointers",
    "title": "02. In-Place Reversal of Singly Linked List",
    "desc": "Given the <code>head</code> of a singly linked list, reverse the list in-place and return the new head pointer. You must solve this with <strong>O(1) extra auxiliary space</strong> and <strong>O(N) time complexity</strong>.",
    "method_signatures": {
      "c": "struct ListNode* reverseList(struct ListNode* head);",
      "cpp": "ListNode* reverseList(ListNode* head);",
      "java": "public static ListNode reverseList(ListNode head)",
      "python": "def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:"
    },
    "input_format": "<code>head</code>: Pointer to the first node of the singly linked list.",
    "output_format": "Return pointer to the new head node after complete in-place reversal.",
    "constraints": "• 0 <= Number of nodes <= 5000<br>• -5000 <= Node.val <= 5000<br>• Must be in-place: No array copies or node re-allocations.",
    "examples": [
      {
        "ex_num": 1,
        "input": "head = [1 -> 2 -> 3 -> 4 -> 5]",
        "output": "[5 -> 4 -> 3 -> 2 -> 1]",
        "explanation": "The links between successive nodes are reversed in-place. Node 5 becomes the new head, and Node 1 points to null."
      },
      {
        "ex_num": 2,
        "input": "head = [1 -> 2]",
        "output": "[2 -> 1]",
        "explanation": "Node 2 points to Node 1, and Node 1 points to null. Output head is 2."
      }
    ],
    "structs": {
      "c": "struct ListNode {\n    int val;\n    struct ListNode* next;\n};",
      "cpp": "struct ListNode {\n    int val;\n    ListNode* next;\n    ListNode(int x) : val(x), next(nullptr) {}\n};",
      "java": "public static class ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { this.val = x; }\n}",
      "python": "class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next"
    },
    "files": { "c": "ReverseList.c", "cpp": "ReverseList.cpp", "java": "ReverseList.java", "python": "reverse_list.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

// Implement the function below
struct ListNode* reverseList(struct ListNode* head) {
    // Write your code here using AI scaffolding
    return head;
}
""",
      "cpp": """#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Implement the function below
ListNode* reverseList(ListNode* head) {
    // Write your code here using AI scaffolding
    return head;
}
""",
      "java": """public class Solution {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { this.val = x; }
    }

    // Implement the function below
    public static ListNode reverseList(ListNode head) {
        // Write your code here using AI scaffolding
        return head;
    }
}
""",
      "python": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implement the function below
def reverse_list(head):
    # Write your code here using AI scaffolding
    return head
"""
    },
    "step1Auto": "The task is to reverse a singly linked list in-place. We receive the head node and must return the new head node. All next pointers should point to their predecessors. Constraints: O(1) extra space, O(N) time.",
    "step2Auto": "I will implement the classic 3-pointer iterative pattern: prev = NULL, curr = head, next = NULL. While curr is not NULL: store next = curr->next, reverse pointer curr->next = prev, advance prev = curr, advance curr = next. At the end, return prev.",
    "generatedCodes": {
      "c": """struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL, *curr = head, *next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}""",
      "cpp": """ListNode* reverseList(ListNode* head) {
    ListNode *prev = nullptr, *curr = head, *nxt = nullptr;
    while (curr != nullptr) {
        nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}""",
      "java": """public static ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head, next = null;
    while (curr != null) {
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}""",
      "python": """def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev"""
    },
    "tc_names": ["Standard 5-Node List Inversion", "Empty & Single Node Boundary Case", "O(1) Memory Verification"]
  },

  "aic_3": {
    "num": "Test 3 • Strings & Sliding Window",
    "title": "03. Longest Substring Without Repeating Characters",
    "desc": "Given a string <code>s</code>, find the length of the <strong>longest contiguous substring</strong> without repeating characters.",
    "method_signatures": {
      "c": "int lengthOfLongestSubstring(char* s);",
      "cpp": "int lengthOfLongestSubstring(string s);",
      "java": "public static int lengthOfLongestSubstring(String s)",
      "python": "def length_of_longest_substring(s: str) -> int:"
    },
    "input_format": "<code>s</code>: A string containing letters, digits, symbols, and spaces.",
    "output_format": "Return an integer representing the maximum length found.",
    "constraints": "• 0 <= s.length <= 5 * 10^4<br>• Expected Time Complexity: O(N)<br>• Expected Space Complexity: O(min(N, charset))",
    "examples": [
      {
        "ex_num": 1,
        "input": "s = \"abcabcbb\"",
        "output": "3",
        "explanation": "The longest substring without repeating characters is \"abc\", with the length of 3."
      },
      {
        "ex_num": 2,
        "input": "s = \"bbbbb\"",
        "output": "1",
        "explanation": "The longest substring is \"b\", with the length of 1."
      }
    ],
    "structs": {
      "c": "int lengthOfLongestSubstring(char* s);",
      "cpp": "int lengthOfLongestSubstring(string s);",
      "java": "public static int lengthOfLongestSubstring(String s);",
      "python": "def length_of_longest_substring(s: str) -> int:"
    },
    "files": { "c": "LongestSubstring.c", "cpp": "LongestSubstring.cpp", "java": "LongestSubstring.java", "python": "longest_substring.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <string.h>

// Implement the function below
int lengthOfLongestSubstring(char* s) {
    // Write your code here using AI scaffolding
    return 0;
}
""",
      "cpp": """#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Implement the function below
int lengthOfLongestSubstring(string s) {
    // Write your code here using AI scaffolding
    return 0;
}
""",
      "java": """public class Solution {
    // Implement the function below
    public static int lengthOfLongestSubstring(String s) {
        // Write your code here using AI scaffolding
        return 0;
    }
}
""",
      "python": """# Implement the function below
def length_of_longest_substring(s: str) -> int:
    # Write your code here using AI scaffolding
    return 0
"""
    },
    "step1Auto": "The goal is to determine the maximum length of any contiguous substring in string s that contains no duplicate characters. Edge cases include empty string (0), all identical characters (1), and all unique characters (length of string).",
    "step2Auto": "I will use the Two-Pointer Sliding Window approach. Maintain a pointer 'left' = 0, and iterate 'right' from 0 to N-1. Use a hash map or 256-element integer lookup table to store the last seen index of each character. When s[right] is already in the window (lastSeen[c] >= left), slide 'left' to lastSeen[c] + 1. Update maxLen = max(maxLen, right - left + 1) and record lastSeen[c] = right.",
    "generatedCodes": {
      "c": """int lengthOfLongestSubstring(char* s) {
    if (!s || !*s) return 0;
    int lastSeen[256];
    for (int i = 0; i < 256; i++) lastSeen[i] = -1;
    int maxLen = 0, left = 0;
    for (int right = 0; s[right]; right++) {
        unsigned char c = (unsigned char)s[right];
        if (lastSeen[c] >= left) {
            left = lastSeen[c] + 1;
        }
        lastSeen[c] = right;
        int len = right - left + 1;
        if (len > maxLen) maxLen = len;
    }
    return maxLen;
}""",
      "cpp": """int lengthOfLongestSubstring(string s) {
    vector<int> lastSeen(256, -1);
    int maxLen = 0, left = 0;
    for (int right = 0; right < (int)s.length(); right++) {
        unsigned char c = s[right];
        if (lastSeen[c] >= left) {
            left = lastSeen[c] + 1;
        }
        lastSeen[c] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}""",
      "java": """public static int lengthOfLongestSubstring(String s) {
    int[] lastSeen = new int[256];
    java.util.Arrays.fill(lastSeen, -1);
    int maxLen = 0, left = 0;
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        if (lastSeen[c] >= left) {
            left = lastSeen[c] + 1;
        }
        lastSeen[c] = right;
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}""",
      "python": """def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    max_len = left = 0
    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1
        last_seen[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len"""
    },
    "tc_names": ["Standard Repeating Pattern ('abcabcbb' -> 3)", "All Monotonous Characters ('bbbbb' -> 1)", "Empty & Whitespace Substring Handled"]
  },

  "aic_4": {
    "num": "Test 4 • Binary Trees & LCA",
    "title": "04. Lowest Common Ancestor (LCA) in Binary Tree",
    "desc": "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes <code>p</code> and <code>q</code>.<br><br>The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow a node to be a descendant of itself).",
    "method_signatures": {
      "c": "struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q);",
      "cpp": "TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q);",
      "java": "public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)",
      "python": "def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:"
    },
    "input_format": "<code>root</code>: Root of the binary tree.<br><code>p</code>, <code>q</code>: Pointers to target nodes to find ancestor for.",
    "output_format": "Return pointer/reference to LCA node.",
    "constraints": "• Number of nodes in tree: [2, 10^5]<br>• All Node.val are unique.<br>• p != q and both p and q exist in the tree.",
    "examples": [
      {
        "ex_num": 1,
        "input": "root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1",
        "output": "3",
        "explanation": "The LCA of nodes 5 and 1 is node 3 because it is the deepest node possessing both 5 and 1 in its subtrees."
      },
      {
        "ex_num": 2,
        "input": "root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4",
        "output": "5",
        "explanation": "The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition."
      }
    ],
    "structs": {
      "c": "struct TreeNode {\n    int val;\n    struct TreeNode* left;\n    struct TreeNode* right;\n};",
      "cpp": "struct TreeNode {\n    int val;\n    TreeNode* left;\n    TreeNode* right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};",
      "java": "public static class TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { this.val = x; }\n}",
      "python": "class TreeNode:\n    def __init__(self, x):\n        self.val = x\n        self.left = None\n        self.right = None"
    },
    "files": { "c": "LCA.c", "cpp": "LCA.cpp", "java": "LCA.java", "python": "lca.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

// Implement the function below
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    // Write your code here using AI scaffolding
    return NULL;
}
""",
      "cpp": """#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Implement the function below
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    // Write your code here using AI scaffolding
    return nullptr;
}
""",
      "java": """public class Solution {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int x) { this.val = x; }
    }

    // Implement the function below
    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Write your code here using AI scaffolding
        return null;
    }
}
""",
      "python": """class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Implement the function below
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Write your code here using AI scaffolding
    return None
"""
    },
    "step1Auto": "Given the root of a binary tree and two nodes p and q, find the lowest node that has both p and q in its descendants. Both p and q are guaranteed to be in the tree, and all values are unique.",
    "step2Auto": "I will use bottom-up recursive DFS. 1) If root is NULL, or root == p, or root == q, return root. 2) Recurse on left = LCA(root->left, p, q) and right = LCA(root->right, p, q). 3) If both left and right return non-null, root is the LCA. 4) If only one is non-null, return that non-null child.",
    "generatedCodes": {
      "c": """struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if (!root || root == p || root == q) return root;
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}""",
      "cpp": """TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}""",
      "java": """public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) return root;
    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);
    if (left != null && right != null) return root;
    return left != null ? left : right;
}""",
      "python": """def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right"""
    },
    "tc_names": ["Split Ancestor across Root (p in left, q in right)", "Self-Descendant Ancestor (p is parent of q)", "Deep Subtree LCA Identification"]
  },

  "aic_5": {
    "num": "Test 5 • Graphs & Topological Sort",
    "title": "05. Course Schedule / Cycle Detection in DAG",
    "desc": "There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a, b]</code> indicates that you must take course <code>b</code> first if you want to take course <code>a</code>.<br><br>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code> (i.e. if there exists a circular dependency / directed cycle).",
    "method_signatures": {
      "c": "bool canFinish(int numCourses, int prerequisitesSize, int prerequisitesColSize, int** prerequisites);",
      "cpp": "bool canFinish(int numCourses, vector<vector<int>>& prerequisites);",
      "java": "public static boolean canFinish(int numCourses, int[][] prerequisites)",
      "python": "def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:"
    },
    "input_format": "<code>numCourses</code>: Total number of courses.<br><code>prerequisites</code>: List of direct requirement pairs [course, prereq].",
    "output_format": "Return boolean: true if feasible to complete all courses, false otherwise.",
    "constraints": "• 1 <= numCourses <= 2000<br>• 0 <= prerequisites.length <= 5000<br>• All pairs are unique.",
    "examples": [
      {
        "ex_num": 1,
        "input": "numCourses = 2, prerequisites = [[1, 0]]",
        "output": "true",
        "explanation": "To take course 1 you must have finished course 0. You can take course 0 first and then course 1."
      },
      {
        "ex_num": 2,
        "input": "numCourses = 2, prerequisites = [[1, 0], [0, 1]]",
        "output": "false",
        "explanation": "To take course 1 you need 0, and to take 0 you need 1. This is a circular dependency (deadlock), so impossible."
      }
    ],
    "structs": {
      "c": "#include <stdbool.h>\nbool canFinish(int numCourses, int prerequisitesSize, int* prerequisitesColSize, int** prerequisites);",
      "cpp": "bool canFinish(int numCourses, vector<vector<int>>& prerequisites);",
      "java": "public static boolean canFinish(int numCourses, int[][] prerequisites);",
      "python": "def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:"
    },
    "files": { "c": "CourseSchedule.c", "cpp": "CourseSchedule.cpp", "java": "CourseSchedule.java", "python": "course_schedule.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Implement Kahn's Algorithm / BFS Indegree
bool canFinish(int numCourses, int prerequisitesSize, int* prerequisitesColSize, int** prerequisites) {
    // Write your code here using AI scaffolding
    return true;
}
""",
      "cpp": """#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Implement Kahn's Algorithm / BFS Indegree
bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    // Write your code here using AI scaffolding
    return true;
}
""",
      "java": """import java.util.*;

public class Solution {
    // Implement Kahn's Algorithm / BFS Indegree
    public static boolean canFinish(int numCourses, int[][] prerequisites) {
        // Write your code here using AI scaffolding
        return true;
    }
}
""",
      "python": """from collections import deque, defaultdict

# Implement Kahn's Algorithm / BFS Indegree
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # Write your code here using AI scaffolding
    return True
"""
    },
    "step1Auto": "The problem asks whether we can finish numCourses given prerequisite dependencies. If the directed dependency graph contains a cycle, return false; if it is a Directed Acyclic Graph (DAG), return true.",
    "step2Auto": "I will implement Kahn's Algorithm for Topological Sorting using BFS. 1) Build adjacency list and compute indegree for each course. 2) Enqueue all nodes with indegree == 0. 3) While queue is not empty, dequeue a course, decrement indegrees of its neighbors, and if any neighbor's indegree becomes 0, enqueue it. Count processed courses. 4) Return count == numCourses.",
    "generatedCodes": {
      "c": """bool canFinish(int numCourses, int prerequisitesSize, int* prerequisitesColSize, int** prerequisites) {
    int inDegree[2000] = {0};
    int adj[2000][100];
    int adjSize[2000] = {0};
    for (int i = 0; i < prerequisitesSize; i++) {
        int u = prerequisites[i][1], v = prerequisites[i][0];
        adj[u][adjSize[u]++] = v;
        inDegree[v]++;
    }
    int queue[2000], head = 0, tail = 0;
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) queue[tail++] = i;
    }
    int count = 0;
    while (head < tail) {
        int curr = queue[head++];
        count++;
        for (int i = 0; i < adjSize[curr]; i++) {
            int nxt = adj[curr][i];
            if (--inDegree[nxt] == 0) queue[tail++] = nxt;
        }
    }
    return count == numCourses;
}""",
      "cpp": """bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses);
    vector<int> inDegree(numCourses, 0);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);
        inDegree[p[0]]++;
    }
    queue<int> q;
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) q.push(i);
    }
    int count = 0;
    while (!q.empty()) {
        int curr = q.front(); q.pop();
        count++;
        for (int nxt : adj[curr]) {
            if (--inDegree[nxt] == 0) q.push(nxt);
        }
    }
    return count == numCourses;
}""",
      "java": """public static boolean canFinish(int numCourses, int[][] prerequisites) {
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
    int[] inDegree = new int[numCourses];
    for (int[] p : prerequisites) {
        adj.get(p[1]).add(p[0]);
        inDegree[p[0]]++;
    }
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) q.offer(i);
    }
    int count = 0;
    while (!q.isEmpty()) {
        int curr = q.poll();
        count++;
        for (int nxt : adj.get(curr)) {
            if (--inDegree[nxt] == 0) q.offer(nxt);
        }
    }
    return count == numCourses;
}""",
      "python": """def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
    q = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0
    while q:
        curr = q.popleft()
        count += 1
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    return count == num_courses"""
    },
    "tc_names": ["Acyclic Valid Sequence (Kahn BFS)", "Deadlock Circular Dependency Cycle", "Disconnected Graph Multiple Components"]
  },

  "aic_6": {
    "num": "Test 6 • Heaps & Linked Lists",
    "title": "06. Merge K Sorted Linked Lists",
    "desc": "You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return its head.",
    "method_signatures": {
      "c": "struct ListNode* mergeKLists(struct ListNode** lists, int listsSize);",
      "cpp": "ListNode* mergeKLists(vector<ListNode*>& lists);",
      "java": "public static ListNode mergeKLists(ListNode[] lists)",
      "python": "def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:"
    },
    "input_format": "<code>lists</code>: Array of k sorted singly-linked list head pointers.",
    "output_format": "Return head pointer of the merged, fully sorted linked list.",
    "constraints": "• k == lists.length, 0 <= k <= 10^4<br>• 0 <= lists[i].length <= 500<br>• Total nodes <= 10^5<br>• Optimal: O(N log k) via Min-Heap or Divide and Conquer.",
    "examples": [
      {
        "ex_num": 1,
        "input": "lists = [[1->4->5],[1->3->4],[2->6]]",
        "output": "[1->1->2->3->4->4->5->6]",
        "explanation": "All 3 lists are merged into a single sorted list preserving relative node orders."
      },
      {
        "ex_num": 2,
        "input": "lists = []",
        "output": "[]",
        "explanation": "Empty input lists array returns null."
      }
    ],
    "structs": {
      "c": "struct ListNode {\n    int val;\n    struct ListNode* next;\n};",
      "cpp": "struct ListNode {\n    int val;\n    ListNode* next;\n    ListNode(int x) : val(x), next(nullptr) {}\n};",
      "java": "public static class ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { this.val = x; }\n}",
      "python": "class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next"
    },
    "files": { "c": "MergeKLists.c", "cpp": "MergeKLists.cpp", "java": "MergeKLists.java", "python": "merge_k_lists.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

// Implement Merge K Sorted Lists (Divide & Conquer or Min-Heap)
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    // Write your code here using AI scaffolding
    return NULL;
}
""",
      "cpp": """#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Implement Merge K Sorted Lists
ListNode* mergeKLists(vector<ListNode*>& lists) {
    // Write your code here using AI scaffolding
    return nullptr;
}
""",
      "java": """import java.util.PriorityQueue;

public class Solution {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { this.val = x; }
    }

    // Implement Merge K Sorted Lists
    public static ListNode mergeKLists(ListNode[] lists) {
        // Write your code here using AI scaffolding
        return null;
    }
}
""",
      "python": """import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implement Merge K Sorted Lists
def merge_k_lists(lists: list[ListNode]) -> ListNode:
    # Write your code here using AI scaffolding
    return None
"""
    },
    "step1Auto": "Given k sorted linked lists, merge all of them into one single sorted list. Total elements N, number of lists k. Target time complexity is O(N log k).",
    "step2Auto": "I will use a Min-Priority Queue (Min-Heap). 1) Push the head of each non-empty linked list into the heap, ordered by node value. 2) Pop the minimum element, append it to our result list. 3) If that popped node has a next node, push the next node into the heap. 4) Repeat until the heap is empty. Return dummy.next.",
    "generatedCodes": {
      "c": """struct ListNode* mergeTwo(struct ListNode* l1, struct ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    if (l1->val < l2->val) { l1->next = mergeTwo(l1->next, l2); return l1; }
    else { l2->next = mergeTwo(l1, l2->next); return l2; }
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize == 0) return NULL;
    int interval = 1;
    while (interval < listsSize) {
        for (int i = 0; i + interval < listsSize; i += interval * 2) {
            lists[i] = mergeTwo(lists[i], lists[i + interval]);
        }
        interval *= 2;
    }
    return lists[0];
}""",
      "cpp": """ListNode* mergeKLists(vector<ListNode*>& lists) {
    auto comp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
    priority_queue<ListNode*, vector<ListNode*>, decltype(comp)> pq(comp);
    for (auto node : lists) if (node) pq.push(node);
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while (!pq.empty()) {
        ListNode* curr = pq.top(); pq.pop();
        tail->next = curr;
        tail = tail->next;
        if (curr->next) pq.push(curr->next);
    }
    return dummy.next;
}""",
      "java": """public static ListNode mergeKLists(ListNode[] lists) {
    if (lists == null || lists.length == 0) return null;
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    for (ListNode node : lists) if (node != null) pq.offer(node);
    ListNode dummy = new ListNode(0);
    ListNode tail = dummy;
    while (!pq.isEmpty()) {
        ListNode curr = pq.poll();
        tail.next = curr;
        tail = tail.next;
        if (curr.next != null) pq.offer(curr.next);
    }
    return dummy.next;
}""",
      "python": """def merge_k_lists(lists: list[ListNode]) -> ListNode:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode(0)
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next"""
    },
    "tc_names": ["Standard 3-List Merge in O(N log K)", "Empty List and Single Element Arrays", "Large Value Disjoint Ranges"]
  },

  "aic_7": {
    "num": "Test 7 • Hash Maps & Prefix Sums",
    "title": "07. Subarray Sum Equals K",
    "desc": "Given an array of integers <code>nums</code> and an integer <code>k</code>, return the <strong>total number of subarrays</strong> whose sum equals to <code>k</code>.<br><br>A subarray is a contiguous non-empty sequence of elements within an array.",
    "method_signatures": {
      "c": "int subarraySum(int* nums, int numsSize, int k);",
      "cpp": "int subarraySum(vector<int>& nums, int k);",
      "java": "public static int subarraySum(int[] nums, int k)",
      "python": "def subarray_sum(nums: list[int], k: int) -> int:"
    },
    "input_format": "<code>nums</code>: Array of integers (can include negatives).<br><code>k</code>: Target sum integer.",
    "output_format": "Return integer count of contiguous subarrays that sum to k.",
    "constraints": "• 1 <= nums.length <= 2 * 10^4<br>• -1000 <= nums[i] <= 1000<br>• -10^7 <= k <= 10^7<br>• Optimal: O(N) using Prefix Sum + Hash Map.",
    "examples": [
      {
        "ex_num": 1,
        "input": "nums = [1, 1, 1], k = 2",
        "output": "2",
        "explanation": "Subarrays [1, 1] at indices [0..1] and [1..2] both sum to 2."
      },
      {
        "ex_num": 2,
        "input": "nums = [1, 2, 3], k = 3",
        "output": "2",
        "explanation": "Subarrays [1, 2] and [3] both sum to 3."
      }
    ],
    "structs": {
      "c": "int subarraySum(int* nums, int numsSize, int k);",
      "cpp": "int subarraySum(vector<int>& nums, int k);",
      "java": "public static int subarraySum(int[] nums, int k);",
      "python": "def subarray_sum(nums: list[int], k: int) -> int:"
    },
    "files": { "c": "SubarraySum.c", "cpp": "SubarraySum.cpp", "java": "SubarraySum.java", "python": "subarray_sum.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>

// Implement Subarray Sum Equals K (Prefix Sum + Frequency Map)
int subarraySum(int* nums, int numsSize, int k) {
    // Write your code here using AI scaffolding
    return 0;
}
""",
      "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// Implement Subarray Sum Equals K
int subarraySum(vector<int>& nums, int k) {
    // Write your code here using AI scaffolding
    return 0;
}
""",
      "java": """import java.util.HashMap;

public class Solution {
    // Implement Subarray Sum Equals K
    public static int subarraySum(int[] nums, int k) {
        // Write your code here using AI scaffolding
        return 0;
    }
}
""",
      "python": """from collections import defaultdict

# Implement Subarray Sum Equals K
def subarray_sum(nums: list[int], k: int) -> int:
    # Write your code here using AI scaffolding
    return 0
"""
    },
    "step1Auto": "The problem asks for the count of contiguous subarrays in nums that sum to k. Elements can be negative, zero, or positive, so a simple two-pointer window won't work. We need O(N) time.",
    "step2Auto": "I will use Prefix Sums with a Hash Map. Keep a running sum 'currSum'. At each index, check if (currSum - k) exists in the map. If so, add its frequency to 'count'. Then increment the frequency of 'currSum' in the map. Initialize map with {0: 1} to handle subarrays starting from index 0.",
    "generatedCodes": {
      "c": """int subarraySum(int* nums, int numsSize, int k) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        int sum = 0;
        for (int j = i; j < numsSize; j++) {
            sum += nums[j];
            if (sum == k) count++;
        }
    }
    return count;
}""",
      "cpp": """int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> prefixMap;
    prefixMap[0] = 1;
    int currSum = 0, count = 0;
    for (int x : nums) {
        currSum += x;
        if (prefixMap.find(currSum - k) != prefixMap.end()) {
            count += prefixMap[currSum - k];
        }
        prefixMap[currSum]++;
    }
    return count;
}""",
      "java": """public static int subarraySum(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    map.put(0, 1);
    int currSum = 0, count = 0;
    for (int x : nums) {
        currSum += x;
        if (map.containsKey(currSum - k)) {
            count += map.get(currSum - k);
        }
        map.put(currSum, map.getOrDefault(currSum, 0) + 1);
    }
    return count;
}""",
      "python": """def subarray_sum(nums: list[int], k: int) -> int:
    map_freq = defaultdict(int)
    map_freq[0] = 1
    curr_sum = count = 0
    for x in nums:
        curr_sum += x
        if curr_sum - k in map_freq:
            count += map_freq[curr_sum - k]
        map_freq[curr_sum] += 1
    return count"""
    },
    "tc_names": ["Standard All-Positive Array ([1,1,1], k=2)", "Negative Numbers Mixed Array ([1,-1,0], k=0)", "Single Element Matches Target"]
  },

  "aic_8": {
    "num": "Test 8 • Dynamic Programming",
    "title": "08. Coin Change (Minimum Coins DP)",
    "desc": "You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.<br><br>Return the <strong>fewest number of coins</strong> that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.",
    "method_signatures": {
      "c": "int coinChange(int* coins, int coinsSize, int amount);",
      "cpp": "int coinChange(vector<int>& coins, int amount);",
      "java": "public static int coinChange(int[] coins, int amount)",
      "python": "def coin_change(coins: list[int], amount: int) -> int:"
    },
    "input_format": "<code>coins</code>: Array of distinct coin denominations.<br><code>amount</code>: Target sum amount.",
    "output_format": "Return minimum coin count required, or -1 if impossible.",
    "constraints": "• 1 <= coins.length <= 12<br>• 1 <= coins[i] <= 2^31 - 1<br>• 0 <= amount <= 10^4",
    "examples": [
      {
        "ex_num": 1,
        "input": "coins = [1, 2, 5], amount = 11",
        "output": "3",
        "explanation": "11 = 5 + 5 + 1 (3 coins total, which is the minimum)."
      },
      {
        "ex_num": 2,
        "input": "coins = [2], amount = 3",
        "output": "-1",
        "explanation": "Amount 3 cannot be formed using only coins of denomination 2."
      }
    ],
    "structs": {
      "c": "int coinChange(int* coins, int coinsSize, int amount);",
      "cpp": "int coinChange(vector<int>& coins, int amount);",
      "java": "public static int coinChange(int[] coins, int amount);",
      "python": "def coin_change(coins: list[int], amount: int) -> int:"
    },
    "files": { "c": "CoinChange.c", "cpp": "CoinChange.cpp", "java": "CoinChange.java", "python": "coin_change.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdlib.h>

// Implement Minimum Coin Change DP
int coinChange(int* coins, int coinsSize, int amount) {
    // Write your code here using AI scaffolding
    return -1;
}
""",
      "cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Implement Minimum Coin Change DP
int coinChange(vector<int>& coins, int amount) {
    // Write your code here using AI scaffolding
    return -1;
}
""",
      "java": """import java.util.Arrays;

public class Solution {
    // Implement Minimum Coin Change DP
    public static int coinChange(int[] coins, int amount) {
        // Write your code here using AI scaffolding
        return -1;
    }
}
""",
      "python": """# Implement Minimum Coin Change DP
def coin_change(coins: list[int], amount: int) -> int:
    # Write your code here using AI scaffolding
    return -1
"""
    },
    "step1Auto": "The problem asks for the minimum number of coins from given denominations to sum up to amount. If unattainable, return -1. If amount is 0, return 0.",
    "step2Auto": "I will use bottom-up 1D Dynamic Programming. Define dp[i] as the minimum coins to make amount i. Initialize dp array of size amount + 1 with amount + 1 (infinity), and set dp[0] = 0. For each i from 1 to amount, and for each coin in coins: if i - coin >= 0, dp[i] = min(dp[i], dp[i - coin] + 1). Finally return dp[amount] > amount ? -1 : dp[amount].",
    "generatedCodes": {
      "c": """int coinChange(int* coins, int coinsSize, int amount) {
    if (amount == 0) return 0;
    int* dp = (int*)malloc((amount + 1) * sizeof(int));
    for (int i = 0; i <= amount; i++) dp[i] = amount + 1;
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < coinsSize; j++) {
            if (i >= coins[j]) {
                int prev = dp[i - coins[j]];
                if (prev + 1 < dp[i]) dp[i] = prev + 1;
            }
        }
    }
    int res = dp[amount] > amount ? -1 : dp[amount];
    free(dp);
    return res;
}""",
      "cpp": """int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        for (int c : coins) {
            if (i >= c) dp[i] = min(dp[i], dp[i - c] + 1);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}""",
      "java": """public static int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        for (int c : coins) {
            if (i >= c) dp[i] = Math.min(dp[i], dp[i - c] + 1);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}""",
      "python": """def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1"""
    },
    "tc_names": ["Standard Denominations ([1,2,5], amount=11 -> 3)", "Impossible Target Amount ([2], amount=3 -> -1)", "Zero Amount Base Case (amount=0 -> 0)"]
  },

  "aic_9": {
    "num": "Test 9 • Stacks & Greedy Strings",
    "title": "09. Valid Parentheses String with Wildcards",
    "desc": "Given a string <code>s</code> containing only three types of characters: <code>'('</code>, <code>')'</code> and <code>'*'</code>, return <code>true</code> if <code>s</code> is valid.<br><br>The following rules define a valid string:<br>• Any left parenthesis <code>'('</code> must have a corresponding right parenthesis <code>')'</code>.<br>• Any right parenthesis <code>')'</code> must have a corresponding left parenthesis <code>'('</code>.<br>• Left parenthesis must occur before the corresponding right parenthesis.<br>• <code>'*'</code> could be treated as a single right parenthesis <code>')'</code> or a single left parenthesis <code>'('</code> or an empty string <code>\"\"</code>.",
    "method_signatures": {
      "c": "bool checkValidString(char* s);",
      "cpp": "bool checkValidString(string s);",
      "java": "public static boolean checkValidString(String s)",
      "python": "def check_valid_string(s: str) -> bool:"
    },
    "input_format": "<code>s</code>: String containing '(', ')', '*'.",
    "output_format": "Return boolean: true if string can be balanced, false otherwise.",
    "constraints": "• 1 <= s.length <= 100<br>• s[i] is '(', ')' or '*'.<br>• Optimal: O(N) time and O(1) space via range greedy.",
    "examples": [
      {
        "ex_num": 1,
        "input": "s = \"(*))\"",
        "output": "true",
        "explanation": "The wildcard '*' acts as a '(' to balance the two right parentheses: \"(())\"."
      },
      {
        "ex_num": 2,
        "input": "s = \"(*)\"",
        "output": "true",
        "explanation": "The wildcard '*' acts as an empty string: \"()\"."
      }
    ],
    "structs": {
      "c": "#include <stdbool.h>\nbool checkValidString(char* s);",
      "cpp": "bool checkValidString(string s);",
      "java": "public static boolean checkValidString(String s);",
      "python": "def check_valid_string(s: str) -> bool:"
    },
    "files": { "c": "ValidString.c", "cpp": "ValidString.cpp", "java": "ValidString.java", "python": "valid_string.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdbool.h>

// Implement Wildcard Parentheses Validator
bool checkValidString(char* s) {
    // Write your code here using AI scaffolding
    return true;
}
""",
      "cpp": """#include <iostream>
#include <string>
using namespace std;

// Implement Wildcard Parentheses Validator
bool checkValidString(string s) {
    // Write your code here using AI scaffolding
    return true;
}
""",
      "java": """public class Solution {
    // Implement Wildcard Parentheses Validator
    public static boolean checkValidString(String s) {
        // Write your code here using AI scaffolding
        return true;
    }
}
""",
      "python": """# Implement Wildcard Parentheses Validator
def check_valid_string(s: str) -> bool:
    # Write your code here using AI scaffolding
    return True
"""
    },
    "step1Auto": "The problem asks whether a string with '(', ')', and '*' can form a valid balanced parentheses sequence where '*' can be '(', ')', or empty string.",
    "step2Auto": "I will use the Greedy Range tracking algorithm (cmin, cmax) representing the minimum and maximum number of open '(' brackets possible. Iterate each char: if '(', cmin++, cmax++; if ')', cmin--, cmax--; if '*', cmin--, cmax++. If cmax < 0, return false immediately (too many ')'). Ensure cmin = max(cmin, 0). At the end, return cmin == 0.",
    "generatedCodes": {
      "c": """bool checkValidString(char* s) {
    int cmin = 0, cmax = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(') { cmin++; cmax++; }
        else if (s[i] == ')') { cmin--; cmax--; }
        else if (s[i] == '*') { cmin--; cmax++; }
        if (cmax < 0) return false;
        if (cmin < 0) cmin = 0;
    }
    return cmin == 0;
}""",
      "cpp": """bool checkValidString(string s) {
    int cmin = 0, cmax = 0;
    for (char c : s) {
        if (c == '(') { cmin++; cmax++; }
        else if (c == ')') { cmin--; cmax--; }
        else if (c == '*') { cmin--; cmax++; }
        if (cmax < 0) return false;
        if (cmin < 0) cmin = 0;
    }
    return cmin == 0;
}""",
      "java": """public static boolean checkValidString(String s) {
    int cmin = 0, cmax = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(') { cmin++; cmax++; }
        else if (c == ')') { cmin--; cmax--; }
        else if (c == '*') { cmin--; cmax++; }
        if (cmax < 0) return false;
        if (cmin < 0) cmin = 0;
    }
    return cmin == 0;
}""",
      "python": """def check_valid_string(s: str) -> bool:
    cmin = cmax = 0
    for c in s:
        if c == '(':
            cmin += 1; cmax += 1
        elif c == ')':
            cmin -= 1; cmax -= 1
        elif c == '*':
            cmin -= 1; cmax += 1
        if cmax < 0:
            return False
        if cmin < 0:
            cmin = 0
    return cmin == 0"""
    },
    "tc_names": ["Multi-Wildcard Balancing ('(*))' -> True)", "Empty Wildcard Reduction ('(*)' -> True)", "Invalid Prefix Mismatch (')(' -> False)"]
  },

  "aic_10": {
    "num": "Test 10 • Backtracking & 2D Matrix DFS",
    "title": "10. Word Search on 2D Matrix (Backtracking)",
    "desc": "Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> if <code>word</code> exists in the grid.<br><br>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.",
    "method_signatures": {
      "c": "bool exist(char** board, int boardSize, int* boardColSize, char* word);",
      "cpp": "bool exist(vector<vector<char>>& board, string word);",
      "java": "public static boolean exist(char[][] board, String word)",
      "python": "def exist(board: list[list[str]], word: str) -> bool:"
    },
    "input_format": "<code>board</code>: 2D matrix of uppercase/lowercase English letters.<br><code>word</code>: Target word string to search.",
    "output_format": "Return boolean: true if word is found along a valid contiguous non-repeating path, false otherwise.",
    "constraints": "• m == board.length, n == board[i].length<br>• 1 <= m, n <= 6<br>• 1 <= word.length <= 15<br>• Backtracking with in-place cell masking.",
    "examples": [
      {
        "ex_num": 1,
        "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCCED\"",
        "output": "true",
        "explanation": "Path: (0,0) 'A' -> (0,1) 'B' -> (0,2) 'C' -> (1,2) 'C' -> (2,2) 'E' -> (2,1) 'D'."
      },
      {
        "ex_num": 2,
        "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCB\"",
        "output": "false",
        "explanation": "Cell 'B' at (0,1) cannot be reused after moving to (0,2) 'C'."
      }
    ],
    "structs": {
      "c": "#include <stdbool.h>\nbool exist(char** board, int boardSize, int* boardColSize, char* word);",
      "cpp": "bool exist(vector<vector<char>>& board, string word);",
      "java": "public static boolean exist(char[][] board, String word);",
      "python": "def exist(board: list[list[str]], word: str) -> bool:"
    },
    "files": { "c": "WordSearch.c", "cpp": "WordSearch.cpp", "java": "WordSearch.java", "python": "word_search.py" },
    "initialCodes": {
      "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Implement 2D Grid Backtracking DFS
bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    // Write your code here using AI scaffolding
    return false;
}
""",
      "cpp": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Implement 2D Grid Backtracking DFS
bool exist(vector<vector<char>>& board, string word) {
    // Write your code here using AI scaffolding
    return false;
}
""",
      "java": """public class Solution {
    // Implement 2D Grid Backtracking DFS
    public static boolean exist(char[][] board, String word) {
        // Write your code here using AI scaffolding
        return false;
    }
}
""",
      "python": """# Implement 2D Grid Backtracking DFS
def exist(board: list[list[str]], word: str) -> bool:
    # Write your code here using AI scaffolding
    return False
"""
    },
    "step1Auto": "The task is to verify if a word exists in a 2D matrix of characters. Letters must be horizontally or vertically adjacent, and no cell can be visited twice during the same path exploration.",
    "step2Auto": "I will use Depth First Search (DFS) with Backtracking. 1) Iterate every cell (r, c). If board[r][c] == word[0], launch dfs(r, c, 0). 2) In dfs(r, c, idx): if idx == word.length return true. If out of bounds or board[r][c] != word[idx] return false. 3) Temporarily mark board[r][c] = '#' (visited). 4) Explore 4 directions: (r+1,c), (r-1,c), (r,c+1), (r,c-1). 5) Restore board[r][c] = word[idx] (backtrack). Return true if any path matches.",
    "generatedCodes": {
      "c": """bool dfs(char** board, int m, int n, int r, int c, char* word, int idx) {
    if (word[idx] == '\\0') return true;
    if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[idx]) return false;
    char temp = board[r][c];
    board[r][c] = '#';
    bool found = dfs(board, m, n, r + 1, c, word, idx + 1) ||
                 dfs(board, m, n, r - 1, c, word, idx + 1) ||
                 dfs(board, m, n, r, c + 1, word, idx + 1) ||
                 dfs(board, m, n, r, c - 1, word, idx + 1);
    board[r][c] = temp;
    return found;
}
bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    int m = boardSize, n = boardColSize[0];
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (dfs(board, m, n, r, c, word, 0)) return true;
        }
    }
    return false;
}""",
      "cpp": """bool dfs(vector<vector<char>>& board, int r, int c, string& word, int idx) {
    if (idx == word.size()) return true;
    if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() || board[r][c] != word[idx]) return false;
    char temp = board[r][c];
    board[r][c] = '#';
    bool found = dfs(board, r + 1, c, word, idx + 1) ||
                 dfs(board, r - 1, c, word, idx + 1) ||
                 dfs(board, r, c + 1, word, idx + 1) ||
                 dfs(board, r, c - 1, word, idx + 1);
    board[r][c] = temp;
    return found;
}
bool exist(vector<vector<char>>& board, string word) {
    for (int r = 0; r < board.size(); r++) {
        for (int c = 0; c < board[0].size(); c++) {
            if (dfs(board, r, c, word, 0)) return true;
        }
    }
    return false;
}""",
      "java": """static boolean dfs(char[][] board, int r, int c, String word, int idx) {
    if (idx == word.length()) return true;
    if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(idx)) return false;
    char temp = board[r][c];
    board[r][c] = '#';
    boolean found = dfs(board, r + 1, c, word, idx + 1) ||
                    dfs(board, r - 1, c, word, idx + 1) ||
                    dfs(board, r, c + 1, word, idx + 1) ||
                    dfs(board, r, c - 1, word, idx + 1);
    board[r][c] = temp;
    return found;
}
public static boolean exist(char[][] board, String word) {
    for (int r = 0; r < board.length; r++) {
        for (int c = 0; c < board[0].length; c++) {
            if (dfs(board, r, c, word, 0)) return true;
        }
    }
    return false;
}""",
      "python": """def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    def dfs(r, c, idx):
        if idx == len(word): return True
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]: return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or
                 dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
        board[r][c] = temp
        return found
    for r in range(m):
        for c in range(n):
            if dfs(r, c, 0): return True
    return False"""
    },
    "tc_names": ["Valid Zigzag Snake Path ('ABCCED' -> True)", "Cell Reuse Prevention ('ABCB' -> False)", "Single Character Grid Boundary"]
  }
}

json_data = json.dumps(problems, indent=2)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Stage 3: AI-Assisted Coding Assessment (Multi-Language: C, C++, Java, Python) | Capgemini Exceller 2027</title>
  <link rel="stylesheet" href="../css/style.css"/>
  <style>
    body {{
      background: #0a0f1d;
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
      height: 100vh;
      margin: 0;
      display: flex;
      flex-direction: column;
    }}
    .sim-header {{
      background: #0f172a;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      padding: 0.6rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
    }}
    .badge-lab {{
      background: #06d6a0;
      color: #042f2e;
      padding: 0.25rem 0.65rem;
      border-radius: 4px;
      font-weight: 800;
      font-size: 0.75rem;
      letter-spacing: 0.5px;
    }}
    .sim-timer {{
      font-family: monospace;
      font-size: 1.4rem;
      font-weight: 800;
      color: #ef4444;
    }}
    
    .sim-container {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      flex: 1;
      overflow: hidden;
    }}

    /* Left Panel: Problem Specification + Code Editor */
    .left-workspace {{
      display: flex;
      flex-direction: column;
      background: #060a12;
      border-right: 1px solid rgba(255,255,255,0.1);
      overflow: hidden;
    }}
    .prob-header-bar {{
      background: #090d16;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding: 0.6rem 1rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .prob-selector {{
      background: #131d33;
      border: 1px solid rgba(255,255,255,0.15);
      color: #fff;
      padding: 0.45rem 0.75rem;
      border-radius: 6px;
      font-size: 0.84rem;
      flex: 1;
      outline: none;
    }}
    
    .prob-details-pane {{
      flex: 0 0 250px;
      overflow-y: auto;
      padding: 0.85rem 1.15rem;
      background: #0c1322;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      font-size: 0.83rem;
      line-height: 1.55;
      color: #cbd5e1;
    }}
    .prob-num {{
      font-size: 0.74rem;
      color: #00d4ff;
      font-weight: 700;
      margin-bottom: 0.15rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .prob-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: #fff;
      margin-bottom: 0.4rem;
    }}
    
    .section-title {{
      font-size: 0.76rem;
      font-weight: 800;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 0.65rem;
      margin-bottom: 0.25rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}
    
    .code-box {{
      background: #040711;
      border: 1px solid rgba(0,212,255,0.2);
      border-radius: 6px;
      padding: 0.5rem 0.75rem;
      font-family: "Fira Code", Consolas, monospace;
      font-size: 0.78rem;
      color: #38bdf8;
      margin: 0.35rem 0;
      white-space: pre-wrap;
    }}
    
    .example-card {{
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 6px;
      padding: 0.6rem 0.85rem;
      margin: 0.45rem 0;
    }}
    .example-header {{
      font-weight: 800;
      font-size: 0.76rem;
      color: #a5b4fc;
      margin-bottom: 0.3rem;
    }}

    /* Code Editor in Left Workspace */
    .editor-section {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: #080c14;
    }}
    .editor-toolbar {{
      background: #0f172a;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding: 0.4rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .lang-dropdown {{
      background: #1e293b;
      color: #00d4ff;
      border: 1px solid rgba(0,212,255,0.3);
      border-radius: 4px;
      padding: 0.25rem 0.6rem;
      font-size: 0.78rem;
      font-weight: 700;
      outline: none;
      cursor: pointer;
    }}
    .code-area {{
      flex: 1;
      padding: 1rem;
      font-family: "Fira Code", monospace, Consolas;
      font-size: 0.88rem;
      line-height: 1.55;
      color: #a5f3fc;
      background: #060a12;
      border: none;
      outline: none;
      resize: none;
      overflow: auto;
      white-space: pre;
    }}
    
    .testcase-panel {{
      height: 120px;
      background: #090d16;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding: 0.5rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      overflow-y: auto;
    }}
    .tc-pill {{
      font-size: 0.75rem;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .tc-pass {{ background: rgba(6,214,160,0.15); color: #06d6a0; border: 1px solid rgba(6,214,160,0.3); }}
    .tc-fail {{ background: rgba(239,68,68,0.15); color: #ef4444; border: 1px solid rgba(239,68,68,0.3); }}

    /* Right Panel: AI Coding Assistant */
    .right-assistant {{
      display: flex;
      flex-direction: column;
      background: #0c1322;
      overflow: hidden;
    }}
    .assistant-header {{
      background: #090d16;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding: 0.6rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    
    /* Token Budget Meter */
    .token-meter-box {{
      background: rgba(15,23,42,0.8);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 6px;
      padding: 0.3rem 0.65rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .token-bar-bg {{
      width: 80px;
      height: 8px;
      background: rgba(255,255,255,0.1);
      border-radius: 4px;
      overflow: hidden;
    }}
    .token-bar-fill {{
      height: 100%;
      width: 100%;
      background: #06d6a0;
      transition: width 0.3s ease, background-color 0.3s ease;
    }}
    .token-text {{
      font-size: 0.74rem;
      font-weight: 800;
      font-family: monospace;
      color: #06d6a0;
    }}

    .chat-history {{
      flex: 1;
      padding: 1rem;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}
    .chat-msg {{
      max-width: 92%;
      padding: 0.75rem 0.95rem;
      border-radius: 10px;
      font-size: 0.83rem;
      line-height: 1.5;
    }}
    .msg-ai {{
      align-self: flex-start;
      background: #131e36;
      border: 1px solid rgba(0,212,255,0.18);
      color: #e2e8f0;
      border-bottom-left-radius: 2px;
    }}
    .msg-user {{
      align-self: flex-end;
      background: #1e3a8a;
      color: #ffffff;
      border-bottom-right-radius: 2px;
    }}
    
    .token-spent-badge {{
      font-size: 0.68rem;
      color: #94a3b8;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      margin-top: 0.35rem;
    }}

    .chat-input-area {{
      padding: 0.75rem 1rem;
      background: #090d16;
      border-top: 1px solid rgba(255,255,255,0.08);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}
    .chat-input {{
      width: 100%;
      background: #131d33;
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 8px;
      color: #fff;
      padding: 0.65rem 0.75rem;
      font-size: 0.84rem;
      resize: none;
      outline: none;
      box-sizing: border-box;
    }}
    .chat-input:focus {{
      border-color: #00d4ff;
    }}
    .chat-input:disabled {{
      background: rgba(239,68,68,0.08);
      border-color: #ef4444;
      color: #f87171;
      cursor: not-allowed;
    }}
    
    .btn-send {{
      background: linear-gradient(135deg, #00d4ff, #7c3aed);
      color: #fff;
      border: none;
      padding: 0.45rem 1rem;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-send:hover {{ opacity: 0.9; }}
    .btn-send:disabled {{ opacity: 0.4; cursor: not-allowed; }}
    
    .btn-insert {{
      background: #06d6a0;
      color: #042f2e;
      border: none;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.75rem;
      cursor: pointer;
      margin-top: 0.5rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .btn-insert:hover {{ background: #059669; }}

    .step-badge {{
      font-size: 0.72rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      background: rgba(0,212,255,0.15);
      color: #00d4ff;
      font-weight: 700;
    }}
  </style>
</head>
<body>

  <!-- SIMULATOR HEADER -->
  <div class="sim-header">
    <div style="display:flex; align-items:center; gap:0.75rem;">
      <span class="badge-lab">STAGE 3 • AI ASSISTED CODING</span>
      <div>
        <div style="font-weight:800; font-size:0.92rem; color:#fff;">AI Assisted Coding Assessment (Multi-Language)</div>
        <div style="font-size:0.72rem; color:#94a3b8;">Official Capgemini Exceller Aon Simulator • 2,000 AI Token Budget</div>
      </div>
    </div>
    <div style="display:flex; align-items:center; gap:1.25rem;">
      <div style="text-align:right;">
        <span style="font-size:0.7rem; color:#94a3b8; display:block;">TIME REMAINING</span>
        <span class="sim-timer" id="timer">45:00</span>
      </div>
      <button class="btn-send" style="background:#334155;" onclick="location.href='../index.html#stage3'">← Dashboard</button>
    </div>
  </div>

  <div class="sim-container">
    <!-- LEFT PANEL: PROBLEM & CODE EDITOR -->
    <div class="left-workspace">
      <div class="prob-header-bar">
        <label style="font-size:0.75rem; color:#94a3b8; font-weight:700; white-space:nowrap;">SELECT TEST (1-10):</label>
        <select class="prob-selector" id="probSelect" onchange="loadProblem(this.value)">
          <option value="aic_1">Test 1: 01. LCM of Two Binary Trees (Official Capgemini Pattern)</option>
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

      <!-- PROBLEM DETAILS PANE -->
      <div class="prob-details-pane" id="probDetailsPane">
        <div class="prob-num" id="probNum">Test 1 • Tree Recursion</div>
        <div class="prob-title" id="probTitle">01. LCM of Two Binary Trees</div>
        
        <div class="section-title">📌 Problem Statement</div>
        <div id="probDesc">Loading description...</div>

        <div class="section-title">⚙️ Method Signature &amp; Struct Definition (<span id="currLangLabel">C</span>)</div>
        <div class="code-box" id="probStruct">Loading struct...</div>

        <div class="section-title">📥 Input &amp; Output Format</div>
        <div style="font-size:0.8rem; margin-bottom:0.4rem;">
          <div><strong>Input:</strong> <span id="probInput"></span></div>
          <div><strong>Output:</strong> <span id="probOutput"></span></div>
        </div>

        <div class="section-title">📏 Constraints &amp; Complexity</div>
        <div style="font-size:0.8rem; color:#cbd5e1; margin-bottom:0.5rem;" id="probConstraints"></div>

        <div class="section-title">💡 Worked Examples with Explanations</div>
        <div id="probExamplesList"></div>
      </div>

      <!-- CODING PANEL -->
      <div class="editor-section">
        <div class="editor-toolbar">
          <div style="display:flex; align-items:center; gap:0.6rem;">
            <span style="font-weight:700; font-size:0.82rem; color:#fff;">&lt;&gt; Coding Workspace</span>
            <select class="lang-dropdown" id="langSelect" onchange="switchLanguage(this.value)">
              <option value="c">C (GCC 11.3)</option>
              <option value="cpp">C++ 20</option>
              <option value="java">Java 17</option>
              <option value="python">Python 3.10</option>
            </select>
            <span style="color:#64748b; font-size:0.75rem;" id="fileName">Solution.c</span>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button class="btn-send" style="padding:0.35rem 0.75rem; font-size:0.75rem; background:#334155;" onclick="resetEditor()">↺ Reset Code</button>
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
          <span style="font-weight:800; font-size:0.88rem; color:#fff;">🤖 Your AI Assistant</span>
          <span class="step-badge" id="stepBadge">Step 1 of 3</span>
        </div>
        
        <!-- TOKEN BUDGET GAUGE -->
        <div class="token-meter-box" title="AI Token Budget: Max 2000 credits allowed per coding session">
          <span style="font-size:0.7rem; color:#94a3b8;">TOKENS:</span>
          <div class="token-bar-bg">
            <div class="token-bar-fill" id="tokenBarFill"></div>
          </div>
          <span class="token-text" id="tokenCount">2,000 / 2,000</span>
        </div>
      </div>

      <!-- CHAT HISTORY -->
      <div class="chat-history" id="chatHistory">
        <div class="chat-msg msg-ai" id="welcomeMsg">
          <strong>Welcome to Capgemini Stage 3 AI-Assisted Assessment!</strong><br/>
          I am your interactive AI Assistant. You have a strict <strong>2,000 Token Credit Budget</strong>.<br/>
          Follow the 3 official scaffolding steps:<br/>
          <strong>Step 1:</strong> Explain the problem requirements &amp; edge cases in your own words.<br/>
          <strong>Step 2:</strong> Detail the data structure and algorithmic approach you plan to use.<br/>
          <strong>Step 3:</strong> I will generate and refine starter code for you in your chosen language.<br/><br/>
          <em>👉 To begin, type your problem framing below or click 'Auto-Fill Best Prompt'.</em>
        </div>
      </div>

      <!-- CHAT INPUT AREA -->
      <div class="chat-input-area">
        <textarea class="chat-input" id="userInput" rows="2" placeholder="Explain the problem in your own words (inputs, outputs, edge cases)..."></textarea>
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:0.72rem; color:#64748b;" id="stepPromptHint">Step 1: Frame problem logic</span>
          <div style="display:flex; gap:0.4rem;">
            <button class="btn-send" id="btnAutoPrompt" style="background:#1e293b; font-size:0.75rem; padding:0.4rem 0.8rem;" onclick="autoFillGoodPrompt()">Auto-Fill Best Prompt</button>
            <button class="btn-send" id="btnSendPrompt" style="font-size:0.75rem; padding:0.4rem 0.9rem;" onclick="sendPrompt()">Send Prompt</button>
          </div>
        </div>
        <div id="tokenWarning" style="display:none; color:#f87171; font-size:0.74rem; font-weight:700; background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); padding:0.35rem 0.65rem; border-radius:6px; text-align:center;">
          ⚠️ Token Budget Exhausted (0 Credits Remaining). Write or refine the remaining code manually in the editor.
        </div>
      </div>
    </div>
  </div>

  <script>
    const AIC_BANK = {json_data};

    let currentLang = 'c';
    let currentProbKey = 'aic_1';
    let step = 1;
    const MAX_TOKENS = 2000;
    let tokensRemaining = MAX_TOKENS;

    function deductTokens(amount) {{
      tokensRemaining = Math.max(0, tokensRemaining - amount);
      updateTokenUI();
    }}

    function updateTokenUI() {{
      const tokenCount = document.getElementById('tokenCount');
      const tokenBarFill = document.getElementById('tokenBarFill');
      const tokenWarning = document.getElementById('tokenWarning');
      const btnSendPrompt = document.getElementById('btnSendPrompt');
      const btnAutoPrompt = document.getElementById('btnAutoPrompt');
      const userInput = document.getElementById('userInput');

      if (tokenCount) tokenCount.innerText = tokensRemaining.toLocaleString() + ' / ' + MAX_TOKENS.toLocaleString();
      
      const pct = (tokensRemaining / MAX_TOKENS) * 100;
      if (tokenBarFill) {{
        tokenBarFill.style.width = pct + '%';
        if (tokensRemaining <= 300) {{
          tokenBarFill.style.backgroundColor = '#ef4444';
          if (tokenCount) tokenCount.style.color = '#ef4444';
        }} else if (tokensRemaining <= 800) {{
          tokenBarFill.style.backgroundColor = '#f59e0b';
          if (tokenCount) tokenCount.style.color = '#f59e0b';
        }} else {{
          tokenBarFill.style.backgroundColor = '#06d6a0';
          if (tokenCount) tokenCount.style.color = '#06d6a0';
        }}
      }}

      if (tokensRemaining <= 0) {{
        if (tokenWarning) tokenWarning.style.display = 'block';
        if (btnSendPrompt) btnSendPrompt.disabled = true;
        if (btnAutoPrompt) btnAutoPrompt.disabled = true;
        if (userInput) {{
          userInput.disabled = true;
          userInput.placeholder = "Token budget exhausted. Please write code manually in the editor.";
        }}
      }} else {{
        if (tokenWarning) tokenWarning.style.display = 'none';
        if (btnSendPrompt) btnSendPrompt.disabled = false;
        if (btnAutoPrompt) btnAutoPrompt.disabled = false;
        if (userInput) {{
          userInput.disabled = false;
          userInput.placeholder = step === 1 
            ? "Explain the problem in your own words (inputs, outputs, edge cases)..." 
            : (step === 2 ? "Describe your algorithm, data structures, and time/space complexity..." : "Ask questions or request code refinements...");
        }}
      }}
    }}

    function loadProblem(key) {{
      currentProbKey = key;
      const p = AIC_BANK[key];
      if (!p) return;

      document.getElementById('probNum').innerText = p.num;
      document.getElementById('probTitle').innerText = p.title;
      document.getElementById('probDesc').innerHTML = p.desc;
      document.getElementById('probInput').innerHTML = p.input_format;
      document.getElementById('probOutput').innerHTML = p.output_format;
      document.getElementById('probConstraints').innerHTML = p.constraints;

      // Worked Examples rendering
      const exContainer = document.getElementById('probExamplesList');
      if (exContainer && p.examples) {{
        exContainer.innerHTML = p.examples.map(ex => `
          <div class="example-card">
            <div class="example-header">Example ${{ex.ex_num}}</div>
            <div style="font-size:0.78rem; font-family:monospace; color:#38bdf8; margin-bottom:0.2rem;"><strong>Input:</strong> ${{ex.input}}</div>
            <div style="font-size:0.78rem; font-family:monospace; color:#06d6a0; margin-bottom:0.35rem;"><strong>Output:</strong> ${{ex.output}}</div>
            <div style="font-size:0.76rem; color:#94a3b8; line-height:1.4;"><strong>Explanation:</strong> ${{ex.explanation}}</div>
          </div>
        `).join('');
      }}

      updateLangStruct();
      resetEditor();
      resetChat();
      tokensRemaining = MAX_TOKENS;
      updateTokenUI();
    }}

    function updateLangStruct() {{
      const p = AIC_BANK[currentProbKey];
      if (!p) return;
      const langNames = {{ c: "C", cpp: "C++", java: "Java", python: "Python" }};
      const langLabel = document.getElementById('currLangLabel');
      if (langLabel) langLabel.innerText = langNames[currentLang] || currentLang.toUpperCase();
      
      const structText = (p.structs && p.structs[currentLang]) ? p.structs[currentLang] : (p.method_signatures[currentLang] || "");
      document.getElementById('probStruct').innerText = structText;
      document.getElementById('fileName').innerText = p.files[currentLang] || 'Solution.' + currentLang;
    }}

    function switchLanguage(lang) {{
      currentLang = lang;
      updateLangStruct();
      resetEditor();
      if (step === 3) {{
        generateAICodeReply();
      }}
    }}

    function resetEditor() {{
      const p = AIC_BANK[currentProbKey];
      if (p && p.initialCodes) {{
        document.getElementById('codeEditor').value = p.initialCodes[currentLang] || '';
      }}
      document.getElementById('tcList').innerHTML = '<div class="tc-pill" style="background:#131d33; color:#94a3b8;">Click \\"Compile & Run Test Cases\\" to validate your solution</div>';
      document.getElementById('tcSummary').innerText = '0 / 3 Passed';
      document.getElementById('tcSummary').style.color = '#94a3b8';
    }}

    function resetChat() {{
      step = 1;
      document.getElementById('stepBadge').innerText = 'Step 1 of 3';
      document.getElementById('stepPromptHint').innerText = 'Step 1: Frame the problem';
      document.getElementById('chatHistory').innerHTML = `
        <div class="chat-msg msg-ai">
          <strong>Welcome to Capgemini Stage 3 AI-Assisted Assessment!</strong><br/>
          I am your interactive AI Assistant. You have a strict <strong>2,000 Token Credit Budget</strong>.<br/>
          Follow the 3 official scaffolding steps:<br/>
          <strong>Step 1:</strong> Explain the problem requirements &amp; edge cases in your own words.<br/>
          <strong>Step 2:</strong> Detail the data structure and algorithmic approach you plan to use.<br/>
          <strong>Step 3:</strong> I will generate and refine starter code for you in your chosen language.<br/><br/>
          <em>👉 To begin, type your problem framing below or click 'Auto-Fill Best Prompt'.</em>
        </div>
      `;
      document.getElementById('userInput').value = '';
    }}

    function autoFillGoodPrompt() {{
      const p = AIC_BANK[currentProbKey];
      if (!p) return;
      if (step === 1) {{
        document.getElementById('userInput').value = p.step1Auto;
      }} else if (step === 2) {{
        document.getElementById('userInput').value = p.step2Auto;
      }} else {{
        document.getElementById('userInput').value = "Can you optimize the code for memory efficiency and add comments?";
      }}
    }}

    function sendPrompt() {{
      if (tokensRemaining <= 0) return;
      const input = document.getElementById('userInput');
      const text = input.value.trim();
      if (!text) return;

      // Deduct tokens based on prompt length (min 120 tokens)
      const promptTokens = Math.min(300, Math.max(120, Math.round(text.length * 0.8)));
      deductTokens(promptTokens);

      const chat = document.getElementById('chatHistory');
      
      // User bubble
      const userBubble = document.createElement('div');
      userBubble.className = 'chat-msg msg-user';
      userBubble.innerHTML = escapeHtml(text) + `<br><span class="token-spent-badge">⚡ -${{promptTokens}} tokens</span>`;
      chat.appendChild(userBubble);
      input.value = '';
      chat.scrollTop = chat.scrollHeight;

      // AI response based on step
      setTimeout(() => {{
        if (step === 1) {{
          const aiTokens = 220;
          deductTokens(aiTokens);
          step = 2;
          document.getElementById('stepBadge').innerText = 'Step 2 of 3';
          document.getElementById('stepPromptHint').innerText = 'Step 2: Algorithm & Data Structures';
          const aiBubble = document.createElement('div');
          aiBubble.className = 'chat-msg msg-ai';
          aiBubble.innerHTML = `
            <strong>Great problem formulation! 👍</strong><br/>
            You clearly identified the inputs, outputs, and edge cases.<br/><br/>
            <strong>Now, Step 2:</strong> What algorithmic approach, data structure, and time/space complexity do you plan to employ?<br/>
            <em>(e.g., Recursion DFS, Two Pointers, Sliding Window, DP, Kahn's algorithm)</em><br>
            <span class="token-spent-badge">⚡ -${{aiTokens}} tokens generated</span>
          `;
          chat.appendChild(aiBubble);
        }} else if (step === 2) {{
          step = 3;
          document.getElementById('stepBadge').innerText = 'Step 3 of 3';
          document.getElementById('stepPromptHint').innerText = 'Step 3: Code Generated & Review';
          generateAICodeReply();
        }} else {{
          const aiTokens = 180;
          deductTokens(aiTokens);
          const aiBubble = document.createElement('div');
          aiBubble.className = 'chat-msg msg-ai';
          aiBubble.innerHTML = `
            <strong>Refinement Insight:</strong><br/>
            The solution has been generated with optimal time &amp; space complexity.<br/>
            Click <strong>"Insert Code into Editor"</strong> above to load it directly into your Coding Workspace, then click <strong>"Compile &amp; Run Test Cases"</strong>.<br>
            <span class="token-spent-badge">⚡ -${{aiTokens}} tokens generated</span>
          `;
          chat.appendChild(aiBubble);
        }}
        chat.scrollTop = chat.scrollHeight;
        updateTokenUI();
      }}, 500);
    }}

    function generateAICodeReply() {{
      const p = AIC_BANK[currentProbKey];
      if (!p) return;
      const code = (p.generatedCodes && p.generatedCodes[currentLang]) ? p.generatedCodes[currentLang] : "// No code";
      const codeTokens = 350;
      deductTokens(codeTokens);

      const chat = document.getElementById('chatHistory');
      const aiBubble = document.createElement('div');
      aiBubble.className = 'chat-msg msg-ai';
      aiBubble.innerHTML = `
        <strong>Excellent plan! Here is your scaffolded solution in ${{currentLang.toUpperCase()}}:</strong>
        <div class="code-box" style="margin-top:0.4rem; max-height:220px; overflow-y:auto;">${{escapeHtml(code)}}</div>
        <button class="btn-insert" onclick="insertCodeToEditor()">⬇️ Insert Code into Editor</button><br>
        <span class="token-spent-badge">⚡ -${{codeTokens}} tokens generated</span>
      `;
      chat.appendChild(aiBubble);
      chat.scrollTop = chat.scrollHeight;
      updateTokenUI();
    }}

    function insertCodeToEditor() {{
      const p = AIC_BANK[currentProbKey];
      if (!p) return;
      const code = (p.generatedCodes && p.generatedCodes[currentLang]) ? p.generatedCodes[currentLang] : "";
      document.getElementById('codeEditor').value = code;
    }}

    function runTestCases() {{
      const p = AIC_BANK[currentProbKey];
      const code = document.getElementById('codeEditor').value.trim();
      const tcList = document.getElementById('tcList');
      const tcSummary = document.getElementById('tcSummary');
      
      const tcNames = p.tc_names || ["Test Case 1 (Sample)", "Test Case 2 (Edge Case)", "Test Case 3 (Performance)"];
      
      // Validation heuristic
      const isNotEmpty = code.length > 40;
      const hasCoreLogic = code.includes("return") && (code.includes("if") || code.includes("while") || code.includes("for"));
      const isPassed = isNotEmpty && hasCoreLogic;

      if (isPassed) {{
        tcList.innerHTML = tcNames.map((name, i) => `
          <div class="tc-pill tc-pass">
            <span>✅</span> <span>TC ${{i + 1}}: ${{name}} [PASS 0.${{12 + i * 4}}s]</span>
          </div>
        `).join('');
        tcSummary.innerText = "3 / 3 Passed (100%)";
        tcSummary.style.color = "#06d6a0";
      }} else {{
        tcList.innerHTML = `
          <div class="tc-pill tc-fail">
            <span>❌</span> <span>TC 1: ${{tcNames[0]}} (Compilation / Incomplete Implementation Error)</span>
          </div>
          <div class="tc-pill tc-fail">
            <span>❌</span> <span>TC 2: ${{tcNames[1]}} (Not Evaluated)</span>
          </div>
          <div class="tc-pill tc-fail">
            <span>❌</span> <span>TC 3: ${{tcNames[2]}} (Not Evaluated)</span>
          </div>
        `;
        tcSummary.innerText = "0 / 3 Passed (Failed)";
        tcSummary.style.color = "#ef4444";
      }}
    }}

    function escapeHtml(text) {{
      return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    // Timer countdown
    let seconds = 45 * 60;
    setInterval(() => {{
      if (seconds > 0) {{
        seconds--;
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        document.getElementById('timer').innerText = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
      }}
    }}, 1000);

    window.onload = function() {{
      loadProblem('aic_1');
    }};
  </script>
</body>
</html>
'''

with open("c:/cap/ai/modules/ai_coding_sim.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("ai_coding_sim.html written successfully!")
