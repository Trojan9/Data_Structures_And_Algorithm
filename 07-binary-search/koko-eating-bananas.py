# Amazon SDE-I 50, #26: Koko Eating Bananas (Medium)  [Binary Search]
#
from typing import List
import math

# Brief: Min integer speed to finish all piles within `h` hours. `[3,6,7,11], 8` → `4`.
#
# In plain words: find the slowest eating speed that still clears all piles within h hours. A
# faster speed never needs more hours, so "does speed X finish in time?" flips from no to yes once
# as speed rises. That lets you binary search the *speed* (between 1 and the biggest pile) instead
# of searching array values.
#
# Why it works: the yes/no of feasibility is monotonic (sorted), which is exactly what binary
# search needs, here applied to the answer space. Max speed ever needed is the biggest pile (one
# pile per hour).
#
# Algorithm
# 1. `l=1`, `r=max(piles)`, `res=r`. 2. For a mid speed, hours = sum of `ceil(p/mid)`. 3. Fits →
#    record, go slower; else go faster.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1                   # fast enough, try slower
            else:
                l = k + 1                   # too slow, speed up
        return res

# Complexity: Time O(n log(max pile)), Space O(1).
