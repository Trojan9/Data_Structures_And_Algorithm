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


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #6: Product of Array Except Self (Medium)  [Arrays and Hashing]
#
from typing import List

# Brief: Each slot = product of all others, no division. `[1,2,3,4]` → `[24,12,8,6]`.
#
# In plain words: at each position, multiply every *other* number. The answer at i is (everything
# to the left of i, multiplied) × (everything to the right of i, multiplied), because those two
# groups together are every element except i. One pass left to right fills the left products; one
# pass right to left multiplies in the right products.
#
# Why it works: you write the left-product into a slot *before* folding that slot's own number
# into the running product, so a slot never includes itself. The second pass does the same from
# the right. No division, so zeros are no problem.
#
# Algorithm
# 1. `res` all 1s. 2. Left pass: store prefix, then `prefix *= nums[i]`. 3. Right pass: `res[i] *=
#    suffix`, then `suffix *= nums[i]`.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix              # product of everything BEFORE i
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix             # multiply in product of everything AFTER i
            suffix *= nums[i]
        return res

# Complexity: Time O(n), Space O(1) extra (output aside).
