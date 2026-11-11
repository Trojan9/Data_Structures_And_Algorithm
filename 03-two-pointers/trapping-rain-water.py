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
        # Empty input holds no water. We also need this guard because the next lines read
        # height[0], which would crash on an empty list.
        if not height:
            return 0

        # One pointer at each end. They walk toward each other, and every bar in between gets
        # visited exactly once by one of them.
        l, r = 0, len(height) - 1

        # leftMax  = tallest bar seen so far from the LEFT  (from index 0 up to l).
        # rightMax = tallest bar seen so far from the RIGHT (from the end down to r).
        # They start as the two end bars. The end bars themselves never hold water (there's
        # nothing outside them to act as a wall), which is why the loop moves the pointer FIRST
        # and only then adds water: we never add water on top of index 0 or the last index.
        leftMax, rightMax = height[l], height[r]

        # Total water trapped so far.
        res = 0

        # Stop when the pointers meet. By then every bar strictly between the two ends has been
        # visited once. The bar where they meet is the tallest bar, which holds no water.
        while l < r:

            # The core idea. Water above any bar = min(tallest wall on its left,
            #                                          tallest wall on its right) - its height.
            # We don't know both walls for every bar, but we don't need to:
            #
            # If leftMax < rightMax, the LEFT side is the bottleneck for the next bar on the left.
            #   - Its tallest-left wall is exactly leftMax (we've seen everything to its left).
            #   - Its tallest-right wall is AT LEAST rightMax (there's a bar that tall somewhere on
            #     the right, maybe taller ones we haven't seen), and rightMax > leftMax.
            #   - So min(left wall, right wall) = leftMax. We can work out its water right now,
            #     without knowing the exact right wall.
            if leftMax < rightMax:
                # Step to the next bar on the left. (Move first: the bar we were on is already
                # done, or it's the end bar, which holds no water.)
                l += 1

                # Update the left wall BEFORE adding water. If this new bar is taller than
                # everything before it, it becomes the new wall and its own water is
                # leftMax - height[l] = 0. Updating first is what stops us adding a NEGATIVE
                # amount of water.
                leftMax = max(leftMax, height[l])

                # Water above this bar = wall height - bar height (0 if the bar IS the wall).
                res += leftMax - height[l]

            else:
                # Mirror image: leftMax >= rightMax, so the RIGHT side is the bottleneck.
                # The next bar on the right has rightMax as its exact right wall, and its left wall
                # is at least leftMax >= rightMax, so min(...) = rightMax.
                # (When leftMax == rightMax either side is fine; both walls are the same height.
                # We just happen to go right.)
                r -= 1

                # Same as the left side: update the wall first so the water is never negative.
                rightMax = max(rightMax, height[r])

                # Water above this bar.
                res += rightMax - height[r]

        return res

# Dry run 1 (small): height = [3, 0, 2]
#
#   l=0, r=2, leftMax=3, rightMax=2, res=0
#
#   leftMax 3 < rightMax 2?  No  -> right side is the bottleneck
#       r = 1, rightMax = max(2, 0) = 2, water = 2 - 0 = 2     res = 2
#   l=0, r=1: leftMax 3 < rightMax 2?  No
#       r = 0, rightMax = max(2, 3) = 3, water = 3 - 3 = 0     res = 2
#   l == r, stop.  return 2
#
#   The 0 sits between walls 3 and 2. Water can only rise to the SHORTER wall (2), or it spills
#   over that side. So 2 units, exactly what the right pointer committed.
#
# Dry run 2 (the classic example): height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  -> 6
#
#   Picture (# = bar, ~ = trapped water):
#
#   3 |                      #
#   2 |          #  ~  ~  ~  #  #  ~  #
#   1 |    #  ~  #  #  ~  #  #  #  #  #  #
#     +------------------------------------
#       0  1  2  3  4  5  6  7  8  9 10 11     <- index
#
#   start: l=0, r=11, leftMax=0, rightMax=1, res=0
#
#   step | compare        | move | bar height | leftMax | rightMax | water added | res
#   -----+----------------+------+------------+---------+----------+-------------+----
#     1  | 0 < 1   left   | l=1  |     1      |    1    |    1     |  1-1 = 0    |  0
#     2  | 1 < 1?  right  | r=10 |     2      |    1    |    2     |  2-2 = 0    |  0
#     3  | 1 < 2   left   | l=2  |     0      |    1    |    2     |  1-0 = 1    |  1
#     4  | 1 < 2   left   | l=3  |     2      |    2    |    2     |  2-2 = 0    |  1
#     5  | 2 < 2?  right  | r=9  |     1      |    2    |    2     |  2-1 = 1    |  2
#     6  | 2 < 2?  right  | r=8  |     2      |    2    |    2     |  2-2 = 0    |  2
#     7  | 2 < 2?  right  | r=7  |     3      |    2    |    3     |  3-3 = 0    |  2
#     8  | 2 < 3   left   | l=4  |     1      |    2    |    3     |  2-1 = 1    |  3
#     9  | 2 < 3   left   | l=5  |     0      |    2    |    3     |  2-0 = 2    |  5
#    10  | 2 < 3   left   | l=6  |     1      |    2    |    3     |  2-1 = 1    |  6
#    11  | 2 < 3   left   | l=7  |     3      |    3    |    3     |  3-3 = 0    |  6
#   l == r == 7 (the tallest bar), stop.  return 6
#
#   Look at steps 8-10: the bars at 4, 5, 6 get water up to leftMax = 2, even though the right
#   pointer never "saw" a wall right next to them. It didn't need to: rightMax = 3 already proved
#   there's a wall of at least 3 on the right, so the left wall (2) decides the water level.
#
#   Steps 4, 7, 11 add 0 because the new bar became the new max. That's the "update the max
#   first" line doing its job: without it, step 7 would add 2 - 3 = -1.

# Complexity: Time O(n), Space O(1).
# Gotcha: a left-only anchor fails when the tallest wall is on the left; you need the max from
# both ends.
