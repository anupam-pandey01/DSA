class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        maxprofit = 0
        i = 0

        while(i < len(prices)):
            bestbuy = min(bestbuy, prices[i])
            if(prices[i] > bestbuy):
                maxprofit = max(maxprofit, prices[i] - bestbuy)

            i+=1
        return maxprofit
                