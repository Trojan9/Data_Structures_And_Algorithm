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
        

        #another solution

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #created my helper function
        def getProduct(nums):
            allsum=nums[0]
            for i in range(1,len(nums)):
                allsum=allsum*nums[i]
            return allsum
        #then array to house my result
        value=[]
        #get the sum
        allsum=getProduct(nums)
        for x in nums:
            #if value is zero...anything divided by zero is infinity which will prevent us from getting product of other elements
            if x is 0:
                var=list(nums)
                #we remove this zero
                var.remove(x)
                #then find product of the rest
                value.append(getProduct(var))
                
            else:
                #esle everything works fine
                value.append(allsum/x)
        return value