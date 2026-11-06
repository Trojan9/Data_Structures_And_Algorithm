# Amazon SDE-I 50, #41: Binary Tree Right Side View (Medium)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
import collections

# Brief: Values visible from the right (last node of each level).
#
# In plain words: standing on the right, you see the rightmost node of each level. Do a level-by-
# level walk and keep the last node of each level.
#
# Why it works: level order processes each level left to right, so the final node of a level is
# the one visible from the right.
#
# Algorithm
# 1. BFS by level. 2. Append the last node's value of each level.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rightSide = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node        # last non-null on this level survives
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

# Complexity: Time O(n), Space O(n).
