class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        bottle = numBottles
        while(bottle >= numExchange):
            emptyBottle = bottle % numExchange
            fullBottle = bottle // numExchange

            result += fullBottle
            bottle = fullBottle + emptyBottle
        
        return result