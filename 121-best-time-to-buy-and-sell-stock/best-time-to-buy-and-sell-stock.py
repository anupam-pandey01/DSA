class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        maxprofit = 0

        for price in prices:
            bestbuy = min(bestbuy, price)

            if(price > bestbuy):
                maxprofit = max(maxprofit, price - bestbuy)
            
        return maxprofit