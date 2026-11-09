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
