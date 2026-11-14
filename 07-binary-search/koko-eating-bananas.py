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






import math  # Used to round up decimal numbers to whole numbers

class Solution:
    def minEatingSpeed(self, piles, h):

        # The slowest possible eating speed is 1 banana per hour.
        # We cannot use 0 because we would be dividing by zero.
        left = 1

        # The fastest speed we need to consider is the largest pile.
        # At this speed, Koko can finish any pile in one hour.
        right = max(piles)

        # Continue searching while there are possible speeds to check.
        # We use <= because we must also check when left == right.
        while left <= right:

            # Find the middle speed between left and right.
            # This is equivalent to (left + right) // 2.
            mid = left + (right - left) // 2

            # Reset hours to 0 each time we test a new speed.
            # We need to calculate the total hours for this speed.
            hours = 0

            # Go through every pile because Koko must finish all piles.
            for pile in piles:

                # pile = number of bananas in the current pile
                # mid = number of bananas Koko eats per hour
                #
                # pile / mid = hours needed to finish this pile.
                #
                # Example:
                # pile = 11, mid = 4
                # 11 / 4 = 2.75 hours
                #
                # But Koko cannot finish 11 bananas in 2 hours:
                # Hour 1: eats 4 bananas (7 remaining)
                # Hour 2: eats 4 bananas (3 remaining)
                # Hour 3: eats 3 bananas (0 remaining)
                #
                # So she needs 3 hours, not 2.75.
                #
                # math.ceil(2.75) = 3
                # ceil() rounds UP to the nearest whole number.
                #
                # We calculate this separately for each pile because
                # Koko cannot start another pile in the same hour.
                #
                # hours += means hours = hours + ...
                # This adds the hours for each pile to the total.
                hours += math.ceil(pile / mid)

            # If the total hours are less than or equal to h,
            # Koko can finish all bananas within the allowed time.
            if hours <= h:

                # This speed works, but we want the MINIMUM speed.
                # So we search the smaller speeds on the left.
                right = mid - 1

            else:
                # If hours > h, Koko is eating too slowly.
                # We need a faster speed.
                # So we search the larger speeds on the right.
                left = mid + 1

        # When the loop ends, left is the smallest valid speed.
        # right is just below the smallest valid speed.
        return left
