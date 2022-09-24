class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #add +1 to range to cater for len(num)+1 i.e [0,1,2,3] output will be 4
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
        