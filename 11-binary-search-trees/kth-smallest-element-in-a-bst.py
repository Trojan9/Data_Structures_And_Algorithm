# Amazon SDE-I 50, #39: Kth Smallest Element in a BST (Medium)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

# Brief: kth smallest value (1-indexed).
#
# In plain words: visiting a BST "in-order" (left, node, right) yields values smallest to largest.
# So do that and stop at the kth one. A stack lets you stop early instead of visiting everything.
#
# Why it works: in-order traversal of a BST is sorted order by the BST property, so the kth node
# visited is the kth smallest.
#
# Algorithm
# 1. Go left, stacking. 2. Pop (next smallest), `k -= 1`; `k == 0` → return. 3. Go right.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

# Complexity: Time O(h + k), Space O(h).
