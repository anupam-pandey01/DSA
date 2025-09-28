class Solution:
    def countDigits(self, num: int) -> int:
        numCopy = num
        count = 0
        while(num > 0):
            val = num % 10
            if(numCopy % val == 0):
                count+=1
            num = num // 10
        
        return count