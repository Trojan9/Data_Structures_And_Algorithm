# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, node1, node2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        if not node1 and not node2:
            return None
        t1=node1.val if node1 else 0
        t2=node2.val if node2 else 0
           
        root=TreeNode(t1+t2)
            
        root.left=self.mergeTrees(node1.left if node1 else None,node2.left if node2 else None)
        root.right=self.mergeTrees(node1.right if node1 else None,node2.right if node2 else None)
        return root
            
#O(n+m) complexicity
        # The solution above is PRE-ORDER: it builds the node FIRST (top -> down), then fills in its children.


# ==================== Post-order version (work AFTER the recursive calls, bottom -> up) ====================
# Same template as diameter-of-binary-tree: handle the None level, recurse left and right first,
# then do this node's work on the way back UP. Building a node here doesn't depend on the order,
# so both versions are correct; this one just follows the usual "recurse first, then combine" format.

class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:              # fell off both trees: the None level
            return None                          # nothing to build here

        # 1. go down first (left, then right)
        left = self.mergeTrees(root1.left if root1 else None,
                               root2.left if root2 else None)
        right = self.mergeTrees(root1.right if root1 else None,
                                root2.right if root2 else None)

        # 2. coming back UP: children are already merged, now build this node
        t1 = root1.val if root1 else 0
        t2 = root2.val if root2 else 0
        return TreeNode(t1 + t2, left, right)    # attach the merged children

# Complexity: Time O(n + m) (visits every node of both trees), Space O(n + m) for the new tree
# (plus recursion depth O(height)).
#
#   step                 | diameter                    | merge trees
#   ---------------------+-----------------------------+--------------------------------------
#   bottom (None)        | return 0                    | return None
#   recurse              | left = dfs(..), right = ..  | left = merge(..), right = merge(..)
#   work AFTER recursion | return 1 + max(left, right) | return TreeNode(t1 + t2, left, right)
#
# ---------------------------------------------------------------------------------------------
# Dry run
# ---------------------------------------------------------------------------------------------
#   tree1:   1          tree2:   2         merged:   3
#           /                     \                 / \
#          3                       4               3   4
#
#   merge(1, 2)
#   ├── merge(3, None)                     left side
#   │   ├── merge(None, None) -> None      <- bottom
#   │   ├── merge(None, None) -> None      <- bottom
#   │   └── build 3+0 = 3, left=None, right=None -> returns node 3
#   ├── merge(None, 4)                     right side
#   │   ├── merge(None, None) -> None
#   │   ├── merge(None, None) -> None
#   │   └── build 0+4 = 4 -> returns node 4
#   └── build 1+2 = 3, left=node 3, right=node 4 -> returns the root   <- built LAST
#
# Pre-order (first solution): the root is built FIRST, its children are filled in after.
# Post-order (this one):      the leaves are built FIRST, the root is built LAST.


# ==================== Shorter version: reuse the leftover subtree ====================
# When only ONE tree has a node at a spot, there's nothing to add, so just hand back that whole
# subtree instead of copying it node by node.

class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1:                     # only tree2 has something here (or both empty -> None)
            return root2                  # reuse tree2's subtree as is
        if not root2:                     # only tree1 has something here
            return root1                  # reuse tree1's subtree as is

        left = self.mergeTrees(root1.left, root2.left)      # both exist: merge children first
        right = self.mergeTrees(root1.right, root2.right)
        return TreeNode(root1.val + root2.val, left, right) # then build this node (post-order)

# Complexity: Time O(min(n, m)): stops as soon as one side runs out (only overlapping nodes are visited).
#
# Same dry run:
#   merge(1, 2)
#   ├── merge(3, None)  -> root2 is None, return tree1's node 3 as is (no copying)
#   ├── merge(None, 4)  -> root1 is None, return tree2's node 4 as is
#   └── build 1+2 = 3, left=node 3, right=node 4
#
# Trade-off: the result SHARES nodes with the input trees. Changing tree1's node 3 later would also
# change the merged tree. The copying versions above are O(n + m) but give a fully separate tree.


# ==================== BFS version (queue of PAIRS, merge INTO tree1) ====================
# Idea: walk both trees level by level AT THE SAME TIME. Each queue entry is a PAIR of nodes
# that sit in the same position in both trees, e.g. (tree1's root, tree2's root), then
# (tree1's root.left, tree2's root.left), and so on.
#
# Instead of building a new tree, we write the answer straight INTO tree1:
#   - add tree2's value onto tree1's node
#   - if tree1 is missing a child that tree2 has, just plug tree2's whole subtree in
#
# For each pair we pop, look at the LEFT children and then the RIGHT children. There are only
# 3 cases per side:
#
#   tree1 child | tree2 child | what to do
#   ------------+-------------+-----------------------------------------------------------
#   yes         | yes         | both exist: put the pair in the queue, they get merged later
#   no          | yes / no    | n1.left = n2.left: plug in tree2's subtree (None if neither)
#   yes         | no          | nothing: tree1's child is already where it should be

from collections import deque

class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1:                           # tree1 empty: the answer is just tree2
            return root2
        if not root2:                           # tree2 empty: the answer is just tree1
            return root1

        q = deque([(root1, root2)])             # start with the two roots as a pair
        while q:
            n1, n2 = q.popleft()                # a pair at the same position (both always exist,
                                                # because we only ever queue pairs where both exist)
            n1.val += n2.val                    # merge: tree1's node now holds the sum

            # ----- LEFT children -----
            if n1.left and n2.left:             # case 1: both have a left child
                q.append((n1.left, n2.left))    #   -> merge that pair when it's popped
            elif not n1.left:                   # case 2: tree1 has no left child
                n1.left = n2.left               #   -> borrow tree2's left subtree (or None)
            # case 3: only tree1 has a left child -> keep it, nothing to do

            # ----- RIGHT children (same 3 cases) -----
            if n1.right and n2.right:           # case 1: both have a right child
                q.append((n1.right, n2.right))
            elif not n1.right:                  # case 2: tree1 has no right child
                n1.right = n2.right             #   -> borrow tree2's right subtree (or None)
            # case 3: only tree1 has a right child -> keep it

        return root1                            # tree1 has become the merged tree

# Complexity: Time O(min(n, m)): only positions where BOTH trees have a node are queued;
# borrowed subtrees are plugged in whole, never walked. Space O(width) for the queue.
#
# Note: this CHANGES tree1 (in place) and shares nodes with tree2 (borrowed subtrees). The first
# two solutions in this file build a brand new tree and leave both inputs untouched.
#
# ---------------------------------------------------------------------------------------------
# Dry run (LeetCode example 1)
# ---------------------------------------------------------------------------------------------
#   tree1:      1            tree2:      2            expected:      3
#              / \                      / \                         / \
#             3   2                    1   3                       4   5
#            /                          \   \                     / \   \
#           5                            4   7                   5   4   7
#
#   start:  q = [ (1,2) ]
#
#   step 1: pop (1,2)
#           value: 1 + 2 = 3              tree1 root is now 3
#           left:  tree1 has 3, tree2 has 1   -> case 1, queue (3,1)
#           right: tree1 has 2, tree2 has 3   -> case 1, queue (2,3)
#           q = [ (3,1), (2,3) ]
#
#                   3                     (tree1 so far)
#                  / \
#                 3   2
#                /
#               5
#
#   step 2: pop (3,1)
#           value: 3 + 1 = 4
#           left:  tree1 has 5, tree2 has None -> case 3, keep 5
#           right: tree1 has None, tree2 has 4 -> case 2, plug in 4: n1.right = 4
#           q = [ (2,3) ]
#
#                   3
#                  / \
#                 4   2
#                / \
#               5   4      <- 4 borrowed from tree2
#
#   step 3: pop (2,3)
#           value: 2 + 3 = 5
#           left:  tree1 has None, tree2 has None -> case 2, n1.left = None (no change)
#           right: tree1 has None, tree2 has 7    -> case 2, plug in 7: n1.right = 7
#           q = [ ]  -> loop ends
#
#                   3
#                  / \
#                 4   5
#                / \   \
#               5   4   7  <- 7 borrowed from tree2
#
#   return root1 = [3, 4, 5, 5, 4, null, 7]   matches expected
#
# Notice: 5 (tree1 only) was never queued, and 4 and 7 (tree2 only) were never queued either.
# Only the 3 positions where BOTH trees had a node went through the queue. That's why it's
# O(min(n, m)).
#
# Why "elif not n1.left" also covers "neither has a child": n2.left is None too, so
# n1.left = None changes nothing. One line handles both case 2 situations.
