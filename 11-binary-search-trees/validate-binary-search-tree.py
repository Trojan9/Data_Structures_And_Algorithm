
The Fundamental Rule of a BST

For a binary tree to be a valid Binary Search Tree, it must act like a perfectly sorted filing system:
• Everything to the left of a number must be strictly smaller than that number.
• Everything to the right of a number must be strictly larger than that number.
This rule doesn't just apply to immediate children; it applies to every descendant down the line.

Why a "Simple Check" Fails

It is tempting to just look at a parent node, check if its left child is smaller, and check if its right child is bigger. 
However, a local check isn't enough.
Take a look at this flawed tree:
text
     10
    /  \
   5    15
       /  \
      3    20   <-- Look closely at the number 3!
Use code with caution.
• If you only check 10, its children are 5 and 15. (Looks valid!)
• If you only check 15, its children are 3 and 20. (Looks valid!)
But notice the 3. It is in the right-hand subtree of 10. 
Because it sits on the right side of 10, the entire system breaks unless that number is greater than 10. 
If you were searching this tree for the number 3, your search algorithm would look at 10, say "3 is smaller than 10, let's look left!", 
and it would completely miss the 3 hidden on the right side.







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #so the idea is to use inequality equations so for it to be valid we must have
        #left< val < right....so we are using 2 pointers of lower and higher....when we move left, we update the right pointer to present node val,and leave the left pointer val....when we move right we update the left pointer to present node value and leave the right pointer val
        def dfs(p,left,right):
            #i.e it did not see any defaulting node not adhering to these rule
            if not p:
                return True
            #then we check if any node doesn't adhere left< val < right
            if not (left< p.val < right):
                return False
            #return the and operator for both node.left and node.right
            #when we move left, we update the right pointer to present node val,and leave the left pointer val....when we move right we update the left pointer to present node value and leave the right pointer val
            return (dfs(p.left,left,p.val)and dfs(p.right,p.val,right))
        #start from -infinity to infinity....since we don't know whats at the root
        return dfs(root,float('-inf'),float('inf'))




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque()
        # Each item: (node, min_val, max_val)
        queue.append((root, float('-inf'), float('inf')))
        
        while queue:
            node,minval,maxval = queue.popleft()

            if not (minval< node.val< maxval):
                return False

            if node.left:
                queue.append((node.left,minval,node.val))
            if node.right:
                queue.append((node.right,node.val,maxval))
            
        return True

            
First iteration:
Node: 5

Allowed range: (-∞, ∞)

✅ 5 is valid

Then:
Left child 4 → range (-∞, 5)

Right child 6 → range (5, ∞)

✅ So far, all good.

Now visit 6:
Left child 3 → range (5, 6)

❌ 3 is not greater than 5, so the tree is invalid.


Each node’s value must be:

python
Copy
Edit
min_val < node.val < max_val
Left child: max becomes node.val

Right child: min becomes node.val





Dry Run 1: A Valid BST (True)

Let's track the execution flow using the example root = [2, 1, 3].
     2
    / \
   1   3
1. Initial Call: valid(Node(2), -∞, ∞)
	• Is -∞ < 2 < ∞? Yes.
	• Recursively split into left and right subtrees.
2. Left Child Call: valid(Node(1), -∞, 2)
	• The maximum value is now updated to the parent's value (2).
	• Is -∞ < 1 < 2? Yes.
	• Check child nodes: valid(None, -∞, 1) and valid(None, 1, 2). Both reach the base case (if not node) and return True.
	• Returns True back to the root.
3. Right Child Call: valid(Node(3), 2, ∞)
	• The minimum value is now updated to the parent's value (2).
	• Is 2 < 3 < ∞? Yes.
	• Check child nodes: valid(None, 2, 3) and valid(None, 3, ∞). Both return True.
	• Returns True back to the root.
4. Final Conclusion: Both paths return True, so the overall function evaluates to True.

Dry Run 2: An Invalid BST (False)

Let's see how the boundary constraints catch a hidden violation using root = [5, 1, 4, null, null, 3, 6].
     5
    / \
   1   4
      / \
     3   6
Note: Looking locally at node 4, its children 3 (left) and 6 (right) seem valid. However, node 3 is sitting in the right subtree of 5, which means it must be greater than 5. This is a global violation.
1. Initial Call: valid(Node(5), -∞, ∞)
	• Is -∞ < 5 < ∞? Yes.
2. Left Child Call: valid(Node(1), -∞, 5)
	• Is -∞ < 1 < 5? Yes. (Its children return True). Returns True.
3. Right Child Call: valid(Node(4), 5, ∞)
	• Is 5 < 4 < ∞? No! 4 is not greater than the lower bound of 5.
	• The function immediately triggers return False.


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #37: Validate Binary Search Tree (Medium)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

# Brief: True if a valid BST.
#
# In plain words: a BST means for every node, *everything* in its left subtree is smaller and
# everything in its right is bigger, not just the direct children. Checking only children misses
# cases: a node deep in a left subtree must still beat an ancestor far above. So carry an allowed
# `(low, high)` range down: going left caps the high at the node's value, going right raises the
# low. A node outside its range makes the tree invalid.
#
# Why it works: the range accumulates every ancestor constraint, so a value illegal relative to a
# distant ancestor is caught.
#
# Algorithm
# 1. Recurse with bounds (−inf, +inf). 2. Require `low < val < high`. 3. Left gets `(low, val)`,
#    right `(val, high)`.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (valid(node.left, left, node.val)
                    and valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))

# Complexity: Time O(n), Space O(h).
