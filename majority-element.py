class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myMap={}
        
        for i in nums:
            if i in myMap:
                myMap[i]+=1
            else:
                myMap[i]=1
        return max(myMap, key=myMap.get) #this is to get the max value in a dictionary
            
        