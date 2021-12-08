from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi=math.prod(nums)
        value=[]
        for x in nums:
            if x is 0:
                var=nums.copy()
                var.remove(x)
                value.append(math.prod(var))
                
            else:
                value.append(int(multi/x))
        return value
        