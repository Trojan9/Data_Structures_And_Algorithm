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
        
        