# Backtracking strategies (branch and bound, kill and bound) explained: https://www.youtube.com/watch?v=DKCbsiDBN6c
#
# looking at this solution to the question
# we start with an empty list of list as res [[]]
# then loop through the array  arr given in question
# every element from arr is interated with the elements in res to form a new array  
# e.g [[]] elemet=3   = [[],[]+[3]] = [[],[3]]
# [[],[3]] elemrnt=4  = [[],[3],[]+4,[3]+[4] ] = [[],[3],[4],[3,4]]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub=[[]]
        for element in nums:
            #javascript way
            # sub=[...sub,[...k, element]for k in sub]
            sub=sub + [ k + [element] for k in sub]
        return sub

# Dry run: nums = [1, 2, 3]
#
#   start            sub = [[]]
#
#   element = 1      new = [ k + [1] for k in [[]] ]
#                        = [ [1] ]
#                    sub = [[]] + [[1]]
#                        = [[], [1]]
#
#   element = 2      new = [ []+[2], [1]+[2] ]
#                        = [ [2], [1,2] ]
#                    sub = [[], [1], [2], [1,2]]
#
#   element = 3      new = [ []+[3], [1]+[3], [2]+[3], [1,2]+[3] ]
#                        = [ [3], [1,3], [2,3], [1,2,3] ]
#                    sub = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
#
#   return sub  ->  8 subsets (2^3)
#
# Key point: every new element DOUBLES the list. Each old subset stays as it is ("don't take
# the element") and also gets a copy with the element added ("take it"). 1 -> 2 -> 4 -> 8.
# k + [element] makes a NEW list, so the old subsets are never changed.


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #47: Subsets (Medium)  [Backtracking]
#
from typing import List

# Brief: All subsets (the power set) of distinct integers.
#
# In plain words: list every possible subset of `[1,2,3]` (there are 2³ = 8, including the empty
# one). Go element by element; for each, branch on include vs exclude. Every complete set of
# yes/no choices is one subset.
#
# Why it works: the recursion makes both choices at every index, so the leaves are exactly all 2ⁿ
# subsets, each once. You store a *copy* because the working list keeps mutating as you backtrack.
#
# Algorithm
# 1. DFS(i). 2. `i == len` → record a copy. 3. Include nums[i] (recurse, pop), then exclude
#    (recurse).

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())   # copy: the list keeps changing
                return
            subset.append(nums[i])          # include
            dfs(i + 1)
            subset.pop()                    # exclude
            dfs(i + 1)
        dfs(0)
        return res

# Dry run: nums = [1, 2, 3]
#
# At each index i we make two choices: take nums[i] (append, go deeper), then skip it (pop, go
# deeper). The recursion tree (left branch = take, right branch = skip):
#
#                                  dfs(0)  subset=[]
#                        take 1 /                    \ skip 1
#                  dfs(1) [1]                          dfs(1) []
#            take 2 /         \ skip 2           take 2 /       \ skip 2
#         dfs(2) [1,2]       dfs(2) [1]          dfs(2) [2]       dfs(2) []
#         /        \         /       \          /       \        /      \
#     [1,2,3]    [1,2]    [1,3]     [1]      [2,3]     [2]      [3]      []     <- i == 3: record
#
# Step by step (indent = recursion depth):
#
#   dfs(0)  subset=[]         append 1 -> [1]
#     dfs(1)  subset=[1]        append 2 -> [1,2]
#       dfs(2)  subset=[1,2]      append 3 -> [1,2,3]
#         dfs(3)                    i == 3, record [1,2,3]      res = [[1,2,3]]
#       dfs(2)                    pop 3 -> [1,2]
#         dfs(3)                    record [1,2]                res = [[1,2,3],[1,2]]
#     dfs(1)                    pop 2 -> [1]
#       dfs(2)  subset=[1]        append 3 -> [1,3]
#         dfs(3)                    record [1,3]
#       dfs(2)                    pop 3 -> [1]
#         dfs(3)                    record [1]
#   dfs(0)                    pop 1 -> []
#     dfs(1)  subset=[]         append 2 -> [2]
#       dfs(2)  subset=[2]        append 3 -> [2,3]
#         dfs(3)                    record [2,3]
#       dfs(2)                    pop 3 -> [2]
#         dfs(3)                    record [2]
#     dfs(1)                    pop 2 -> []
#       dfs(2)  subset=[]         append 3 -> [3]
#         dfs(3)                    record [3]
#       dfs(2)                    pop 3 -> []
#         dfs(3)                    record []
#
#   res = [[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []]   -> 8 subsets
#
# Why subset.copy(): there is only ONE subset list, shared by every call. If we appended the list
# itself, every entry in res would point to that same list, which ends up [] after all the pops,
# so res would be [[], [], [], [], [], [], [], []].
#
# Compare with the first solution: same 8 subsets, different order.
#   iterative: [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]   (grows the list element by element)
#   DFS:       [1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []   (always tries "take" before "skip")

# Complexity: Time O(n·2ⁿ), Space O(n) excluding output.


# ==================== BFS version (queue) ====================
#
# Same include / exclude idea as the DFS version, but instead of recursion we keep a queue of
# partial decisions. Each queue item is (i, cur): "I've decided elements 0..i-1, and cur is what
# I took so far". Popping an item makes the decision for nums[i] both ways and pushes two new
# items. When i == len(nums) every element has been decided, so cur is a finished subset.
#
# Why no .copy() here: cur + [nums[i]] builds a NEW list, so each queue item owns its own list.
# Nothing is shared and nothing is popped/undone, which is why there's no backtracking step.

from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        q = deque([(0, [])])                 # (index, current subset)
        while q:
            i, cur = q.popleft()
            if i == len(nums):               # decided every element
                res.append(cur)
                continue
            q.append((i + 1, cur))               # exclude nums[i]
            q.append((i + 1, cur + [nums[i]]))   # include nums[i]
        return res

# Dry run: nums = [1, 2, 3]   (queue shown front -> back, as (i, cur))
#
#   pop (0, [])        i=0, decide 1:  push (1, []), (1, [1])
#                      q = (1,[]) (1,[1])
#   pop (1, [])        decide 2:       push (2, []), (2, [2])
#                      q = (1,[1]) (2,[]) (2,[2])
#   pop (1, [1])       decide 2:       push (2, [1]), (2, [1,2])
#                      q = (2,[]) (2,[2]) (2,[1]) (2,[1,2])
#   -- level i=2: all four 2-element decisions made, now decide 3 for each --
#   pop (2, [])        push (3, []), (3, [3])
#   pop (2, [2])       push (3, [2]), (3, [2,3])
#   pop (2, [1])       push (3, [1]), (3, [1,3])
#   pop (2, [1,2])     push (3, [1,2]), (3, [1,2,3])
#                      q = (3,[]) (3,[3]) (3,[2]) (3,[2,3]) (3,[1]) (3,[1,3]) (3,[1,2]) (3,[1,2,3])
#   -- level i=3: every element decided, each pop is a finished subset --
#   pop (3, [])        record []
#   pop (3, [3])       record [3]
#   pop (3, [2])       record [2]
#   pop (3, [2,3])     record [2,3]
#   pop (3, [1])       record [1]
#   pop (3, [1,3])     record [1,3]
#   pop (3, [1,2])     record [1,2]
#   pop (3, [1,2,3])   record [1,2,3]
#
#   res = [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]   -> 8 subsets
#
# It's the same decision tree as the DFS version, just explored level by level (all decisions
# about 1, then all about 2, then all about 3) instead of going deep down one branch first.
# Exclude is pushed before include, so at every level the "skip" child comes out first.
#
# Complexity: Time O(n·2ⁿ). Space O(n·2ⁿ): the last level holds all 2ⁿ partial subsets in the
# queue at once, whereas DFS only ever holds one path of length n. That's the trade-off:
# BFS is easier to trace, DFS uses far less memory.

