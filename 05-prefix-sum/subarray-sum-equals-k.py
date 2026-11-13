# LeetCode 560: Subarray Sum Equals K (Medium)  [Prefix Sum + Hash Map]
# Video explanation: https://www.youtube.com/watch?v=WpHt8KW02jg
#
from typing import List

# Problem: given an integer array nums and an integer k, return how many CONTIGUOUS subarrays
# (no gaps, in order) add up to exactly k. Numbers can be negative.
#
#   nums = [1, 2, 3], k = 3  ->  2      ([1,2] and [3])
#   nums = [1, -1, 2, 3, -2, 4], k = 3  ->  3
#
# =============================================================================================
# KEY IDEA: IF THE RUNNING SUM UP TO HERE IS S, AND SOME EARLIER RUNNING SUM WAS S - K,
# THEN EVERYTHING BETWEEN THOSE TWO POINTS ADDS UP TO EXACTLY K.
#
#                         S  (prefix sum up to here)
#             |--------------------------------|
#             [ 1 | -1 |  2 |  3 | -2 ]  4              k = 3
#             |--------|-----------------------|
#               S - K              K
#           (seen before)   (the subarray we found)
#
# SO AT EACH STEP ASK: "HOW MANY TIMES HAVE I SEEN A PREFIX SUM OF (S - K) BEFORE?"
# EACH ONE IS A DIFFERENT START POINT OF A SUBARRAY THAT ENDS HERE AND SUMS TO K.
# A HASH MAP OF  prefix sum -> how many times seen  ANSWERS THAT IN O(1).
# =============================================================================================
#
# Prefix sum = the running total from index 0 up to the current index.
#   sum of a subarray = (prefix at its end) - (prefix just before its start)
#   we want that = k   ->   prefix just before start = prefix at end - k = S - K


# ---------------------------------------------------------------------------------------------
# Brute force (from the video): try every start, extend the end, count sums equal to k
# ---------------------------------------------------------------------------------------------
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for start in range(n):                  # every possible start
            total = 0
            for end in range(start, n):         # grow the subarray one element at a time
                total += nums[end]              # sum of nums[start..end]
                if total == k:
                    count += 1
        return count

# Complexity: Time O(n^2), Space O(1).


# ---------------------------------------------------------------------------------------------
# Optimal: prefix sum + hash map
# ---------------------------------------------------------------------------------------------
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0                              # running sum S from index 0 up to here
        seen = {0: 1}                           # prefix sum -> how many times it occurred
                                                # {0: 1} = "the empty prefix before index 0",
                                                # so a subarray starting at index 0 can be found
        for n in nums:
            prefix += n                         # S = sum of nums[0..current]
            count += seen.get(prefix - k, 0)    # every earlier prefix equal to S - K is a start
                                                # point of a subarray ending HERE with sum k
            seen[prefix] = seen.get(prefix, 0) + 1   # record S AFTER the lookup, for later steps
        return count

# Complexity: Time O(n) (one pass, O(1) map lookups), Space O(n) (the map).


# =============================================================================================
# Dry run (the video's example): nums = [1, -1, 2, 3, -2, 4], k = 3
# =============================================================================================
# At every step:  1) prefix += n   2) look up (prefix - k) in the map   3) add prefix to the map
#
#   start:  prefix = 0, count = 0
#           map:  prefix sum | count
#                 -----------+------
#                      0     |  1          <- the empty prefix
#
# ---- n = 1 ----------------------------------------------------------------------------------
#   prefix = 0 + 1 = 1
#   prefix - k = 1 - 3 = -2   -> not in map, count stays 0
#   add 1:   map = {0: 1, 1: 1}
#
# ---- n = -1 ---------------------------------------------------------------------------------
#   prefix = 1 + -1 = 0
#   prefix - k = 0 - 3 = -3   -> not in map, count stays 0
#   add 0:   map = {0: 2, 1: 1}            <- prefix 0 seen TWICE now (before index 0, and after -1)
#
# ---- n = 2 ----------------------------------------------------------------------------------
#   prefix = 0 + 2 = 2
#   prefix - k = 2 - 3 = -1   -> not in map, count stays 0
#   add 2:   map = {0: 2, 1: 1, 2: 1}
#
# ---- n = 3 ----------------------------------------------------------------------------------
#   prefix = 2 + 3 = 5
#   prefix - k = 5 - 3 = 2    -> in map, seen 1 time  -> count = 0 + 1 = 1
#            which subarray?  prefix 2 was after [1,-1,2], so the part after it is  [3]  = 3 ✓
#   add 5:   map = {0: 2, 1: 1, 2: 1, 5: 1}
#
# ---- n = -2 ---------------------------------------------------------------------------------
#   prefix = 5 + -2 = 3
#   prefix - k = 3 - 3 = 0    -> in map, seen 2 times -> count = 1 + 2 = 3
#            which subarrays? prefix 0 happened twice:
#              - before index 0      -> everything so far: [1,-1,2,3,-2]  = 3 ✓
#              - after [1,-1]        -> the part after it:  [2,3,-2]      = 3 ✓
#   add 3:   map = {0: 2, 1: 1, 2: 1, 5: 1, 3: 1}
#
# ---- n = 4 ----------------------------------------------------------------------------------
#   prefix = 3 + 4 = 7
#   prefix - k = 7 - 3 = 4    -> not in map, count stays 3
#   add 7:   map = {0: 2, 1: 1, 2: 1, 5: 1, 3: 1, 7: 1}
#
#   return count = 3      the 3 subarrays:  [3],  [1,-1,2,3,-2],  [2,3,-2]
#
# Summary table:
#
#    n  | prefix | prefix - k | seen[prefix - k] | count | map after adding prefix
#   ----+--------+------------+------------------+-------+------------------------------------
#       |   0    |            |                  |   0   | {0:1}
#    1  |   1    |    -2      |        0         |   0   | {0:1, 1:1}
#   -1  |   0    |    -3      |        0         |   0   | {0:2, 1:1}
#    2  |   2    |    -1      |        0         |   0   | {0:2, 1:1, 2:1}
#    3  |   5    |     2      |        1         |   1   | {0:2, 1:1, 2:1, 5:1}
#   -2  |   3    |     0      |        2         |   3   | {0:2, 1:1, 2:1, 5:1, 3:1}
#    4  |   7    |     4      |        0         |   3   | {0:2, 1:1, 2:1, 5:1, 3:1, 7:1}
#
#
# =============================================================================================
# Small dry run: nums = [1, 2, 3], k = 3
# =============================================================================================
#    n | prefix | prefix - k | found?             | count | map
#   ---+--------+------------+--------------------+-------+-------------------
#      |   0    |            |                    |   0   | {0:1}
#    1 |   1    |    -2      | no                 |   0   | {0:1, 1:1}
#    2 |   3    |     0      | yes, 1 time ([1,2])|   1   | {0:1, 1:1, 3:1}
#    3 |   6    |     3      | yes, 1 time ([3])  |   2   | {0:1, 1:1, 3:1, 6:1}
#   return 2
#
#
# =============================================================================================
# The questions people get stuck on
# =============================================================================================
# 1. Why start the map with {0: 1}?
#    A subarray that starts at index 0 has nothing before it, so the "prefix before the start" is
#    0. Without {0: 1}, in [1, 2, 3] the subarray [1,2] (prefix 3, 3 - 3 = 0) would be missed.
#
# 2. Why store a COUNT and not just a set of prefixes?
#    The same prefix can happen more than once (prefix 0 appeared twice above). Each time is a
#    different start point, so each one is a different subarray. At n = -2 we added 2, not 1.
#
# 3. Why look up FIRST, then add the current prefix?
#    The start must be BEFORE the end. If we added first, then with k = 0 we'd match the current
#    prefix with itself and count an empty subarray. Look up, then record.
#
# 4. Why not a sliding window?
#    Sliding window needs "grow = sum goes up, shrink = sum goes down". With negative numbers
#    (like -1 and -2 here) adding an element can make the sum smaller, so you can't tell when to
#    shrink. Prefix sum + map doesn't care about signs.
