class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # so for here we would create a hashset ,for new values we would add to it..if the value exist we would remove it from the hashset
#         create a hashset

#         newSet=set()
#         for i in nums:
#             if i in newSet:
#                 newSet.remove(i)
#             else:
#                 newSet.add(i)
#         return list(newSet)[0]
        
    
    # another solution is to use binary xOR..which just add the binary values together..the resulting answer convert to tens is the single number
        res=0
        for i in nums:
            res=i ^ res  #XOR
        return res
        
        
        
        