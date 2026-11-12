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
