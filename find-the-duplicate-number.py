class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for x in nums:
            if x in dict:
                return x
            else:
                dict[x]=1