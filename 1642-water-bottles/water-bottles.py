class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            fullBottle = emptyBottles // numExchange
            drink += fullBottle

            emptyBottles = emptyBottles % numExchange
            emptyBottles += fullBottle
        
        return drink