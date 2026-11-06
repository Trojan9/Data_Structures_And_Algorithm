class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if ((target-nums[i]) in nums) and (nums.index(target-nums[i])!=i) :
                return [i,nums.index(target-nums[i])]
            

# another solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make an empty map
        prevMap={}  #val:index
        # get index and val
        for i,n in enumerate(nums):
            diff=target-n
            # from here we will mostly get our result when we get to the second value
            # [1,2,3,4]...target=4....we will get our result at 3.....4-3=1, by then 1 has been added to the map, 
            # we will return index of 1 and 3
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #1: Two Sum (Easy)  [Arrays and Hashing]
#
from typing import List

# Brief: Return indices of the two numbers that add to `target`. `[2,7,11,15], 9` → `[0,1]`.
#
# In plain words: find two numbers that add up to the target and give back their positions. As you
# walk the list, each number `n` needs a specific partner, `target − n`. Keep a lookup table of
# numbers you've already passed. If the partner you need is in it, you've found the pair. Example:
# at `7` (target 9), you need `2`; `2` is already in the table at index 0, so answer `[0,1]`.
#
# Why it works: every pair has a first and second element; by the time you reach the second, the
# first is in the table, so you find each pair exactly once. Store *after* checking so a number
# never pairs with itself.
#
# Algorithm
# 1. Empty map `seen` (value → index).
# 2. For each `i, n`: if `target - n` is in `seen`, return `[seen[target-n], i]`.
# 3. Else store `seen[n] = i`.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []

# Complexity: Time O(n) (one pass), Space O(n) (the map).
