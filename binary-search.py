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
        