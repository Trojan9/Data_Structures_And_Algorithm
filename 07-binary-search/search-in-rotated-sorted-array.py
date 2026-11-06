# Amazon SDE-I 50, #25: Search in Rotated Sorted Array (Medium)  [Binary Search]
#
from typing import List

# Brief: Find target in a rotated sorted array, or -1. `[4,5,6,7,0,1,2], 0` → `4`.
#
# In plain words: same rotated array, but find a target's index. At any middle, one of the two
# halves is a clean sorted run (you can tell which by comparing the left value to the middle).
# Check whether the target falls inside that sorted half's range; if yes search there, if no
# search the other half.
#
# Why it works: a single rotation guarantees one side of any mid has no cliff, so it's a normal
# sorted range where you can test "is the target between these two ends?" in one comparison, then
# halve correctly.
#
# Algorithm
# 1. Standard loop. 2. Left half sorted (`nums[l] <= nums[mid]`): target in `[nums[l], nums[mid])`
#    → go left, else right. 3. Else mirror on the right.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:             # left half is sorted
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:                                 # right half is sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

# Complexity: Time O(log n), Space O(1).
