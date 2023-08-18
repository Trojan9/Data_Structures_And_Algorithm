class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if ((target-nums[i]) in nums) and (nums.index(target-nums[i])!=i) :
                return [i,nums.index(target-nums[i])]
            

# another solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make an empty map
        prevMap={}  #val:index
        # get index and val
        for i,n in enumerate(nums):
            diff=target-n
            # from here we will mostly get our result when we get to the second value
            # [1,2,3,4]...target=4....we will get our result at 3.....4-3=1, by then 1 has been added to the map, 
            # we will return index of 1 and 3
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return 
        