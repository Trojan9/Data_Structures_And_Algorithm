from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # brute force method
        
        # output=False
        # hashset=set()
        # for i in range(len(nums)):
        #     if nums[i] in hashset:
        #         output=True
        #     hashset.add(nums[i])
        # return output
        
        #another thinking idea from flutter
        
        hashset=set(nums) #sets removes every duplicate like in flutter where we use .toSet() to remove duplicates
        
        if(len(nums)!=len(hashset)):
            return True
        return False


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #2: Contains Duplicate (Easy)  [Arrays and Hashing]
#
from typing import List

# Brief: Return `True` if any value appears at least twice.
#
# In plain words: does a number repeat? Keep a bag (set) of what you've seen; add numbers one at a
# time, and if one is already in the bag, that's a duplicate. `[1,2,3,1]` → the second `1` is
# already there → True.
#
# Why it works: a set holds each value once, so the first failed add proves you've seen it before,
# the definition of a duplicate.
#
# Algorithm
# 1. Empty set. 2. For each number, True if present, else add. 3. False at the end.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# Complexity: Time O(n), Space O(n).
