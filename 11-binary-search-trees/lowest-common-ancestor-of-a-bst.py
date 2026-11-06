# Amazon SDE-I 50, #38: Lowest Common Ancestor of a BST (Medium)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brief: Deepest node that is an ancestor of both p and q.
#
# In plain words: in a BST (smaller left, bigger right), start at the top: if both targets are
# smaller than the current node go left, both bigger go right. The first node where they split (or
# one equals the node) is the lowest common ancestor.
#
# Why it works: all values less than a node are in its left subtree, all greater in its right. The
# split point is the lowest node from which both targets are still reachable.
#
# Algorithm
# 1. From root. 2. Both bigger → right; both smaller → left; else return node.

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# Complexity: Time O(h), Space O(1).
