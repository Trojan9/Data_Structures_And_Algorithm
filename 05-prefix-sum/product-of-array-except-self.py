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



###   Input: nums = [1,2,3,4]
###   Output: [24,12,8,6]

#Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeroSum=0
        allSum=1
        #get summ without 0
        for x in nums:
            if x != 0:
                allSum = allSum * x
            else:
                zeroSum +=1
        #loop through
        for i in range(len(nums)):
            #if no 0 , dividing total with the integer gives the result without that integer
            if zeroSum == 0:
                nums[i] = allSum//nums[i]
            # if 0 is more than 1 then every where will result to 0, no matter what
            if zeroSum >1:
                nums[i]= 0
            #now if only 1, other items will be 0
            elif zeroSum == 1 and nums[i] != 0:
                nums[i] = 0
            #the value at that 0 will be the sum without the 0....since 0 is ignored in the sum calc
            elif zeroSum ==1 and nums[i] ==0:
                nums[i] = allSum

        return nums
