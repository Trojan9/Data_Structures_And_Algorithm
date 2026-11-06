# Amazon SDE-I 50, #48: Permutations (Medium)  [Backtracking]
#
from typing import List

# Brief: All orderings of distinct integers.
#
# In plain words: list every ordering of `[1,2,3]` (there are 3! = 6). Build an ordering position
# by position: for each spot, try each number not yet used, recurse on the rest, then put it back.
#
# Why it works: iterating over the remaining elements at each level tries every choice for that
# position; passing "remaining minus the chosen one" prevents reuse. Backtracking resets for the
# next choice.
#
# Algorithm
# 1. No remaining → record a copy. 2. For each remaining element, choose, recurse on the rest, un-
#    choose.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, remaining):
            if not remaining:
                res.append(current[:])
                return
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i + 1:])
                current.pop()
        backtrack([], nums)
        return res

# Complexity: Time O(n·n!), Space O(n) excluding output.
