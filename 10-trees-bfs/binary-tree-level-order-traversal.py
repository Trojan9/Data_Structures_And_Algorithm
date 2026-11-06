# Amazon SDE-I 50, #36: Binary Tree Level Order Traversal (Medium)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
import collections

# Brief: Node values level by level.
#
# In plain words: list values top level first, then the next, etc. A queue processes nodes in the
# order added, which for a tree is level by level. At each round the queue holds exactly one
# level, note how many, process that many, add their children for next round.
#
# Why it works: capturing `len(queue)` before processing isolates the current level before its
# children get mixed in.
#
# Algorithm
# 1. Queue root. 2. For each level, pop `len(q)` nodes, collect, enqueue children.

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        while q:
            level = []
            for _ in range(len(q)):          # exactly this level's nodes
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

# Complexity: Time O(n), Space O(n).
