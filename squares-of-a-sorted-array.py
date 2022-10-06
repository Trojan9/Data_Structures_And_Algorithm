class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #now the idea is to use the same array as we were given to reduce space complexity
        for i in range(len(nums)):
            #here we get the square of this value and store it back in the array index
            nums[i]=nums[i]*nums[i]
        #here we need to sort it again
        nums.sort()
        return nums
    
    
    #time complexity is O(2n)..if i am correct
        
        