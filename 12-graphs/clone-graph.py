# Amazon SDE-I 50, #43: Clone Graph (Medium)  [Graphs]
#
# Definition for a graph node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

# Two solutions below: DFS (recursive) first, then BFS (queue), which is easier to trace by hand.
#
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


# ==================== BFS version (easier to follow) ====================
#
# Same idea, oldToNew maps each original node to its copy, but instead of recursion we walk the
# graph level by level with a queue.
#
# Walkthrough on 1 -- 2, 1 -- 4, 2 -- 3, 3 -- 4 (a square):
#   start: copy 1, queue = [1]
#   pop 1: neighbours 2, 4 are new -> copy them, queue them. Link copy1 -> copy2, copy4
#   pop 2: neighbour 1 already copied (just link it), 3 is new -> copy, queue. copy2 -> copy1, copy3
#   pop 4: 1 and 3 already copied, just link. copy4 -> copy1, copy3
#   pop 3: 2 and 4 already copied, just link. copy3 -> copy2, copy4
#   queue empty -> every copy has all its edges. Return copy of 1.
#
# Why it works:
# - A node is copied (and queued) the first time we see it, so it is never queued twice.
#   That is what stops cycles from looping forever.
# - Every node is popped exactly once, and when popped we link its copy to the copies of ALL its
#   neighbours, so every edge ends up in the clone.
# - Copy a neighbour before linking to it: oldToNew[nei] must exist when we append it.
#
# Algorithm
# 1. Empty input -> None.
# 2. Copy the start node, put it in oldToNew and in the queue.
# 3. While the queue isn't empty: pop cur. For each neighbour: if not copied yet, copy it and
#    queue it. Then append the neighbour's copy to cur's copy's neighbours.
# 4. Return oldToNew[node].

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:            # first time seeing it: copy + queue
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])   # link the copies

        return oldToNew[node]

# Complexity: Time O(V + E) (each node popped once, each edge looked at from both ends),
# Space O(V) (the map and the queue).
