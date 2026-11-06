# Amazon SDE-I 50, #12: Container With Most Water (Medium)  [Two Pointers]
#
from typing import List

# Brief: Two lines trapping the most water. `[1,8,6,2,5,4,8,3,7]` → `49`.
#
# In plain words: pick two vertical lines that, with the floor, hold the most water. Water held =
# width between them × the shorter line (water spills over the shorter side). Start with the
# widest gap, a pointer at each end, and always move the pointer on the shorter line inward.
#
# Why it works: the shorter wall caps the water, so moving the taller one in keeps the same cap
# but loses width, never helpful. Moving the shorter one is the only move that might find a taller
# wall and more area.
#
# Algorithm
# 1. `l`, `r` at ends. 2. Compute area, update max. 3. Move the pointer at the shorter wall.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

# Complexity: Time O(n), Space O(1).
