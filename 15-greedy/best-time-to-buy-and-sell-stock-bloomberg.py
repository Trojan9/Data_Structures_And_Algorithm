class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice=0
        #could have used float("inf")
        lower=9999
        if len(prices)==0:
            return 0
        for price in prices:
            #if price is higher than present lower..we compare max values
            if price>lower:
                maxprice=max(maxprice,(price-lower))
                #else if its lower..it becomes new lower
            elif price<lower:
                lower=price
        return maxprice


#faster and more understandable solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # we cannot sell in the past
        maxPrice = 0
        #so we initialize at index 0, profit is 0 at this day
        lowest=prices[0]
        #index of going from index 0, we start from index 1
        for i in range(1, len(prices)):
            #if present price is greater than the current lowest price...we calculate the max profit between what we have before and what we have now
            if prices[i]>lowest:
                maxPrice = max(maxPrice,(prices[i]-lowest))
            #else if it is lower than what lower price we have now, this should become when we buy
            elif prices[i]<lowest:
                lowest = prices[i]
        return maxPrice

################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = float("inf")
        best = 0
        for val in prices:
            if val < mini:
                mini = val
            best = max(best, val - mini)
        return best



        
            





        
 
