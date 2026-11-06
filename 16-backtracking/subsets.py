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

# Complexity: Time O(n·2ⁿ), Space O(n) excluding output.
