class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        #using the [B-A] difference approach
        #time complexity is O(nlogn)..space is O(n)
        diff=[]
        mc=0
        #iterationns is O(n)
        for c1,c2 in costs:
            diff.append([c2-c1,c1,c2])
            #sorting is O(logn)
        diff.sort()
        for i in range(len(diff)):
            if i <len(diff)//2:
                mc+=diff[i][2]
            else:
                mc+=diff[i][1]
        return mc
        
    #we can further reduce space complexity by using the exact array we were given instead of creating a new one

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        #time complexity is O(nlogn)..space is O(n)
        
        mc=0
        #iterationns is O(n)
        for i in range(len(costs)):
            costs[i]=[costs[i][1]-costs[i][0],costs[i][0],costs[i][1]]
            #sorting is O(logn)
        costs.sort()
        for i in range(len(costs)):
            if i <len(costs)//2:
                mc+=costs[i][2]
            else:
                mc+=costs[i][1]
        return mc
        
#dynamic programming solution (Greedy)


        
        