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