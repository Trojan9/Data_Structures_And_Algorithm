class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
#         run the cummulative
# i.e [1,2,3,4] becomes [0,1,3,6,10]
#between (1,3) =9     ..using the cummulative right+1 -left = 10-1=9
        sum=0
        self.newarray=[0]
        for num in nums:
            sum+=num
            self.newarray.append(sum)
        

    def sumRange(self, left, right):
        
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.newarray[right+1]-self.newarray[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)