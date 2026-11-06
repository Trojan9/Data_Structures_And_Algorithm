# Amazon SDE-I 50, #13: Trapping Rain Water (Hard)  [Two Pointers]
#
from typing import List

# Brief: Water trapped between bars. `[0,1,0,2,1,0,1,3,2,1,2,1]` → `6`.
#
# In plain words: a row of walls; after rain, water pools in the dips. Water on top of any
# position = (the shorter of the tallest wall to its left and the tallest to its right) − that
# position's height. Example `[3,0,2]`: the `0` has a 3 on its left and a 2 on its right, so water
# = min(3,2) − 0 = 2. Total 2.
#
# Why it works: using two pointers, when `leftMax < rightMax` the left bar's water is definitely
# capped by `leftMax` (anything on the right is at least `rightMax`, which is bigger), so you can
# commit it without knowing the exact right wall. That's why you always advance the shorter side.
#
# Algorithm
# 1. `l`, `r` at ends; track `leftMax`, `rightMax`. 2. `leftMax < rightMax` → move `l`, update
#    `leftMax`, add `leftMax − height[l]`. 3. Else mirror on the right.

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# Complexity: Time O(n), Space O(1).
# Gotcha: a left-only anchor fails when the tallest wall is on the left; you need the max from
# both ends.
