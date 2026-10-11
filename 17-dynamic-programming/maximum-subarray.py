from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        cumsum=0
        for i in range(len(nums)):
            if cumsum<0:
                cumsum=0
            cumsum+=nums[i]
            maxsub=max(maxsub,cumsum)
        return maxsub