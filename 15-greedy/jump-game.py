# LeetCode 55: Jump Game (Medium)  [Greedy]
#
from typing import List

# Problem: you start at index 0. nums[i] is the MAXIMUM jump length from index i (you can jump
# any distance from 1 up to nums[i]). Can you reach the last index?
#
#   [2,3,1,1,4] -> True    (0 -> 1 -> 4)
#   [3,2,1,0,4] -> False   (every path gets stuck on the 0 at index 3)
#
# =============================================================================================
# KEY IDEA: WORK BACKWARDS. KEEP A "GOAL" = THE LEFTMOST INDEX THAT WE KNOW CAN REACH THE END.
# AT THE START THE GOAL IS THE LAST INDEX (YOU'RE ALREADY THERE).
# WALK FROM RIGHT TO LEFT. IF FROM INDEX i YOU CAN JUMP AS FAR AS THE GOAL (i + nums[i] >= goal),
# THEN i CAN ALSO REACH THE END (JUMP TO THE GOAL, THEN FOLLOW ITS WAY) -> i IS THE NEW GOAL.
# AT THE END: IF THE GOAL HAS MOVED ALL THE WAY TO INDEX 0, THE START CAN REACH THE END.
# =============================================================================================
#
# Picture for [2,3,1,1,4]:
#
#   index:   0   1   2   3   4
#   nums:    2   3   1   1   4
#                            G      <- goal starts at the last index
#                        G          <- 3 can reach 4, goal moves to 3
#                    G              <- 2 can reach 3, goal moves to 2
#                G                  <- 1 can reach 2, goal moves to 1
#            G                      <- 0 can reach 1, goal moves to 0  -> True
#
# Why ">=" and not "==": nums[i] is the MAX jump, so if i + nums[i] goes PAST the goal you can
# just jump shorter and land exactly on it. Reaching or passing the goal is enough.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1                     # the last index can trivially "reach the end"
        for i in range(len(nums) - 2, -1, -1):   # second-to-last index down to 0 (right to left)
            if i + nums[i] >= goal:              # from i you can land on (or past) the goal
                goal = i                         # so i itself can reach the end: new goal
            # else: i can't reach the goal -> leave the goal where it is.
            #       Some index further left might still be able to jump OVER i to the goal.
        return goal == 0                         # did the goal get all the way back to the start?

# Complexity: Time O(n) (one pass), Space O(1).


# =============================================================================================
# Dry run 1: nums = [2,3,1,1,4]   -> expected True
# =============================================================================================
#   start: goal = 4 (last index)
#
#    i | nums[i] | i + nums[i] (furthest jump) | >= goal? | goal after
#   ---+---------+-----------------------------+----------+-----------
#    3 |    1    |   3 + 1 = 4                 | 4 >= 4 ✓ |    3
#    2 |    1    |   2 + 1 = 3                 | 3 >= 3 ✓ |    2
#    1 |    3    |   1 + 3 = 4                 | 4 >= 2 ✓ |    1      (overshoots the goal: fine)
#    0 |    2    |   0 + 2 = 2                 | 2 >= 1 ✓ |    0
#
#   goal == 0 -> return True
#
#   Reading the goals back: 0 can reach 1, 1 can reach 2 (or straight to 4), 2 can reach 3,
#   3 can reach 4. So a path exists from 0 to the end.
#
# =============================================================================================
# Dry run 2: nums = [3,2,1,0,4]   -> expected False
# =============================================================================================
#   start: goal = 4
#
#    i | nums[i] | i + nums[i] | >= goal? | goal after
#   ---+---------+-------------+----------+-----------
#    3 |    0    |  3 + 0 = 3  | 3 >= 4 ✗ |    4
#    2 |    1    |  2 + 1 = 3  | 3 >= 4 ✗ |    4
#    1 |    2    |  1 + 2 = 3  | 3 >= 4 ✗ |    4
#    0 |    3    |  0 + 3 = 3  | 3 >= 4 ✗ |    4
#
#   goal is still 4, not 0 -> return False
#
#   Why: every index's furthest jump lands on index 3, and nums[3] = 0, so you're stuck there.
#
#   index:   0   1   2   3   4
#   nums:    3   2   1   0   4
#            \___\___\___^          everyone tops out at index 3 (the 0 trap), nobody reaches 4
#
# =============================================================================================
# Dry run 3 (goal skips over a dead index): nums = [2,0,2,0,1]   -> expected True
# =============================================================================================
#   start: goal = 4
#
#    i | nums[i] | i + nums[i] | >= goal? | goal after
#   ---+---------+-------------+----------+-----------
#    3 |    0    |  3 + 0 = 3  | 3 >= 4 ✗ |    4      index 3 is a dead end, goal stays at 4
#    2 |    2    |  2 + 2 = 4  | 4 >= 4 ✓ |    2      2 jumps OVER the dead index 3 to 4
#    1 |    0    |  1 + 0 = 1  | 1 >= 2 ✗ |    2      index 1 is a dead end too
#    0 |    2    |  0 + 2 = 2  | 2 >= 2 ✓ |    0      0 jumps over 1, lands on 2
#
#   goal == 0 -> return True      path: 0 -> 2 -> 4
#
#   This is why a failed index doesn't end the search: the goal just stays put, and an index
#   further left can still jump over the dead one.
#
# =============================================================================================
# Why it's safe to only keep ONE goal (the greedy part)
# =============================================================================================
# The goal is always the LEFTMOST index known to reach the end. For any i to the left of it,
# the goal is the closest "good" index, so it's the easiest one to reach. If i can't reach even
# that one, it can't reach any good index further right either. So checking just
# `i + nums[i] >= goal` gives the right answer, and we never need a list of all good indexes.


# ---------------------------------------------------------------------------------------------
# Same idea going FORWARD: track the furthest index you can reach so far
# ---------------------------------------------------------------------------------------------
# Walk left to right. `reach` = furthest index reachable from anything seen so far. If you ever
# stand on an index beyond `reach`, you could never have got there -> False.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0                                # furthest index reachable so far
        for i in range(len(nums)):
            if i > reach:                        # can't even get to i
                return False
            reach = max(reach, i + nums[i])      # from i, we can get as far as i + nums[i]
        return True                              # got through every index (including the last)

# Dry run on [3,2,1,0,4]:
#    i | i > reach? | reach after = max(reach, i + nums[i])
#   ---+------------+---------------------------------------
#    0 | 0 > 0 no   | max(0, 0+3) = 3
#    1 | 1 > 3 no   | max(3, 1+2) = 3
#    2 | 2 > 3 no   | max(3, 2+1) = 3
#    3 | 3 > 3 no   | max(3, 3+0) = 3
#    4 | 4 > 3 YES  | -> return False   (index 4 is beyond anything we can reach)
#
# Dry run on [2,3,1,1,4]:
#    i | i > reach? | reach after
#   ---+------------+------------
#    0 | no         | max(0, 2) = 2
#    1 | no         | max(2, 4) = 4     <- can already reach the last index
#    2 | no         | max(4, 3) = 4
#    3 | no         | max(4, 4) = 4
#    4 | no         | max(4, 8) = 8
#   loop finishes -> return True
#
# Both are O(n) time, O(1) space. Backward = "who can reach the goal?", forward = "how far can
# I get?". Same answer.
