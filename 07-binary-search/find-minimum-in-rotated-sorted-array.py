# Amazon SDE-I 50, #24: Find Minimum in Rotated Sorted Array (Medium)  [Binary Search]
#
from typing import List

# Brief: Min of a sorted array rotated at an unknown pivot. `[4,5,6,7,0,1,2]` → `0`.
#
# In plain words: a sorted array was cut and the front moved to the back, making two sorted runs
# with one "cliff" where it drops from big to small. The minimum sits right after the cliff. Use
# binary search: compare the middle to the rightmost element, if middle is bigger, the cliff is to
# the right; otherwise it's at the middle or left.
#
# Why it works: rotation creates exactly one drop, and `nums[mid] > nums[r]` means mid is still on
# the high run so the min (just past the cliff) is to the right; otherwise mid is on the low run
# so the min is at mid or left.
#
# Algorithm
# 1. `res = nums[0]`. 2. If the range is already sorted (`nums[l] < nums[r]`), take its left and
#    stop. 3. Else move toward the rotated half, tracking the min.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:           # already sorted → left is the min here
                res = min(res, nums[l])
                break
            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:           # left half clean → drop is to the right
                l = m + 1
            else:
                r = m - 1
        return res

# Complexity: Time O(log n), Space O(1).
