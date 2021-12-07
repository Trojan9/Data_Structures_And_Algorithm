from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: 
            return 0        
        else:
            buy = 99999 # represent minimum price so far
            profit = 0
            for price in prices:
                if price > buy:
                    if price - buy > profit:
                        profit = price - buy                        
                elif price < buy:
                    buy = price
                
            return profit