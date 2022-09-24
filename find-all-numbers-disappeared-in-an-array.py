class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums=set(nums)
        output=[]
        
        for i in range (1,len(nums)+1):
            if i not in setNums:
                output.append(i)
        return output
            
        