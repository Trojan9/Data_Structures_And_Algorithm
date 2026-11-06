# Amazon SDE-I 50, #43: Clone Graph (Medium)  [Graphs]
#
# Definition for a graph node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

# Brief: Deep copy a connected undirected graph.
#
# In plain words: make a full copy of a network of connected nodes. Walk it copying nodes, keeping
# a map from each original node to its copy. The map stops you looping forever on cycles (if a
# node's already copied, reuse that copy) and makes shared connections point to the same copy.
#
# Why it works: recording the clone *before* recursing into neighbours breaks cycles; reusing
# existing clones preserves the exact structure.
#
# Algorithm
# 1. None → None. 2. Already cloned → return it. 3. Clone, record, then clone each neighbour.

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy          # record BEFORE recursing (breaks cycles)
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None

# Complexity: Time O(V + E), Space O(V).
