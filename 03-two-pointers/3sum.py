# Amazon SDE-I 50, #11: 3Sum (Medium)  [Two Pointers]
#
from typing import List

# Brief: All unique triplets summing to zero. `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`.
#
# In plain words: find all trios that add to zero, no duplicates. Sort the list. Fix one number,
# then use the two-pointer trick (like Two Sum II) on the rest to find pairs that cancel it out.
# Skip repeated values so you don't list the same trio twice.
#
# Why it works: fixing `nums[i]` turns it into "find two numbers after i summing to `-nums[i]`".
# Sorting puts equal values together so the skip checks remove duplicate triplets cleanly.
#
# Algorithm
# 1. Sort. 2. For each i (skip duplicate anchors), two-pointer `l,r`. 3. Adjust by the sum's sign;
#    on a hit, record and skip duplicates.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate anchor
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:   # skip duplicate lefts
                        l += 1
        return res

# Complexity: Time O(n²), Space O(1) (output aside).
