class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        return -1
        

#optimum solution using binary tree

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #start from edge of the array
        l,r=0,len(nums)-1
        #they shouldn't cross over each other....they meet at center and stop
        while l<=r:
            m=l+((r-l)//2)#this prevents overflow in case of large bits of array
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m #hence num[m]==target
        return -1 #else nothing sup..return -1


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #22: Binary Search (Easy)  [Binary Search]
#
from typing import List

# Brief: Index of target in a sorted array, or -1.
#
# In plain words: find a value in a sorted array fast. Look at the middle; if it's the target,
# done. If the target is bigger, it can only be in the right half, so throw away the left half
# (and vice versa). Each step halves what's left.
#
# Why it works: sortedness means comparing the target to the middle tells you which side it's on,
# so discarding the other half never loses it. log n steps total. `l + (r-l)//2` is an overflow-
# safe midpoint (a habit from other languages).
#
# Algorithm
# 1. `l=0`, `r=len-1`. 2. While `l<=r`, check mid; equal → return. 3. Too small → `l=mid+1`; too
#    big → `r=mid-1`.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

# Complexity: Time O(log n), Space O(1).
