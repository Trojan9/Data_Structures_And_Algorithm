Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

 

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.
Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3



####first o(n)2 ####but time limit exceeded

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = float("-inf")
        for i in range(len(houses)):
            mini = float("inf")
            for j in range(len(heaters)):
                sub = abs(heaters[j] - houses[i])
                mini = min(mini,sub)    
            res = max(res,mini)
        
        print(res)
        return res



#####use this ...optimum solution.... #######




import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = float("-inf")
        houses = sorted(houses)
        heaters = sorted(heaters)
        for i in range(len(houses)):
            #this will find the index of the first item that is greater than houses[i]
            idx = bisect.bisect_left(heaters,houses[i])
            print(idx)
            #so imagine the house value is placed between the first value that is greater than it and the last value that is lesser than it 
            left = abs(houses[i] - heaters[idx - 1]) if idx > 0 else float("inf") #last value lesser tha
            right = abs(houses[i] - heaters[idx]) if idx < len(heaters) else float("inf") #first value greater than
            #so we want the house placed in the minimum distance from the heater
            #then find the maximum of the minimums gotten
            res = max(res, min(left,right))
        return res
        
