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
# ---------------------------------------------------------------------------------------------
# The idea: answer[i] = (product of everything to the LEFT of i) × (product of everything to the RIGHT of i)
# ---------------------------------------------------------------------------------------------
# "Every number except nums[i]" is just two groups glued together:
#   - all the numbers BEFORE index i  (the left side)
#   - all the numbers AFTER index i   (the right side)
# nums[i] itself is in neither group. So:
#
#   answer[i] = left[i] * right[i]
#
#   nums = [1, 2, 3, 4]
#
#   i = 2 (the 3):    [ 1, 2 ]   3   [ 4 ]
#                      left          right
#                      1*2 = 2       4
#                     answer[2] = 2 * 4 = 8      (= 1*2*4, everything except the 3)
#
# For every index:
#
#   index         0          1          2          3
#   nums          1          2          3          4
#   left        (none)=1     1         1*2        1*2*3
#               = 1          = 1        = 2        = 6
#   right       2*3*4       3*4         4        (none)=1
#               = 24         = 12       = 4        = 1
#   answer      1*24=24     1*12=12    2*4=8      6*1=6
#
# ("none" = nothing on that side, so we use 1, because multiplying by 1 changes nothing.)
#
# So we do two loops:
#   Loop 1, LEFT -> RIGHT:  for each i, store the product of everything BEFORE i.
#   Loop 2, RIGHT -> LEFT:  for each i, multiply in the product of everything AFTER i.
# After both loops, res[i] = left[i] * right[i] = the answer.
#
# Why no division: the "total / nums[i]" trick breaks on zeros (you can't divide by 0). This way
# never divides, so zeros just work. See dry run 2.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Start every slot at 1 (multiplying by 1 changes nothing), ready to be multiplied into.
        res = [1] * len(nums)

        # ---------------- Loop 1: LEFT -> RIGHT ----------------
        # prefix = product of every number we've walked past so far, i.e. everything to the LEFT
        # of the current index. It starts at 1 because nothing is to the left of index 0.
        prefix = 1
        for i in range(len(nums)):
            # Store the product of everything BEFORE i. We store it FIRST, before multiplying
            # nums[i] in, so res[i] never includes nums[i] itself.
            res[i] = prefix              # product of everything BEFORE i
            # Now add nums[i] to the running product, so the NEXT index (i + 1) sees it as part of
            # its left side.
            prefix *= nums[i]
        # Now res[i] = product of everything to the LEFT of i.

        # ---------------- Loop 2: RIGHT -> LEFT ----------------
        # suffix = product of every number to the RIGHT of the current index. We walk backwards so
        # we can build it up the same way. It starts at 1 because nothing is to the right of the
        # last index.
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            # res[i] already holds the left product. Multiply in the right product:
            # res[i] = left * right = everything except nums[i].
            # Again we use suffix FIRST, before multiplying nums[i] in, so nums[i] is left out.
            res[i] *= suffix             # multiply in product of everything AFTER i
            # Add nums[i] to the running right-side product for the next index to the left (i - 1).
            suffix *= nums[i]

        return res

# Complexity: Time O(n) (two passes), Space O(1) extra. The output array doesn't count, and we
# reuse it to hold the left products instead of making separate left[] and right[] arrays.

# ---------------------------------------------------------------------------------------------
# Dry run 1: nums = [1, 2, 3, 4]   -> [24, 12, 8, 6]
# ---------------------------------------------------------------------------------------------
#   start: res = [1, 1, 1, 1]
#
#   Loop 1 (left -> right), prefix starts at 1:
#     i=0: res[0] = prefix = 1   (nothing left of 0)     then prefix = 1 * 1 = 1
#     i=1: res[1] = prefix = 1   (just the 1)            then prefix = 1 * 2 = 2
#     i=2: res[2] = prefix = 2   (1*2)                   then prefix = 2 * 3 = 6
#     i=3: res[3] = prefix = 6   (1*2*3)                 then prefix = 6 * 4 = 24 (not used)
#     res = [1, 1, 2, 6]         <- product of everything to the LEFT of each index
#
#   Loop 2 (right -> left), suffix starts at 1:
#     i=3: res[3] = 6 * 1  = 6   (nothing right of 3)    then suffix = 1 * 4  = 4
#     i=2: res[2] = 2 * 4  = 8   (just the 4)            then suffix = 4 * 3  = 12
#     i=1: res[1] = 1 * 12 = 12  (3*4)                   then suffix = 12 * 2 = 24
#     i=0: res[0] = 1 * 24 = 24  (2*3*4)                 then suffix = 24 * 1 = 24 (not used)
#     res = [24, 12, 8, 6]       <- left × right = everything except itself
#
# ---------------------------------------------------------------------------------------------
# Dry run 2 (with a zero): nums = [-1, 1, 0, -3, 3]   -> [0, 0, 9, 0, 0]
# ---------------------------------------------------------------------------------------------
#   start: res = [1, 1, 1, 1, 1]
#
#   Loop 1 (left -> right):
#     i=0: res[0] = 1                  then prefix = 1 * -1 = -1
#     i=1: res[1] = -1                 then prefix = -1 * 1 = -1
#     i=2: res[2] = -1                 then prefix = -1 * 0 = 0    <- the zero is now in prefix
#     i=3: res[3] = 0                  then prefix = 0
#     i=4: res[4] = 0                  then prefix = 0
#     res = [1, -1, -1, 0, 0]
#
#   Loop 2 (right -> left):
#     i=4: res[4] = 0 * 1    = 0       then suffix = 1 * 3   = 3
#     i=3: res[3] = 0 * 3    = 0       then suffix = 3 * -3  = -9
#     i=2: res[2] = -1 * -9  = 9       then suffix = -9 * 0  = 0   <- the zero is now in suffix
#     i=1: res[1] = -1 * 0   = 0       then suffix = 0
#     i=0: res[0] = 1 * 0    = 0       then suffix = 0
#     res = [0, 0, 9, 0, 0]
#
#   Only index 2 (the zero itself) is non-zero: its left side (-1 * 1) and right side (-3 * 3) don't
#   contain the zero, so -1 * -9 = 9. Every other index has the zero on one side, so it gets 0.
#   No division anywhere, so the zero never caused a problem.
