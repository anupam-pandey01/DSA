class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False

        if(x == 0):
            return True
        
        pal_num = ""
        original = x

        while(x > 0):
            dig = x % 10
            x = x // 10

            pal_num += str(dig)
        
        if(int(pal_num) == original):
            return True
        else: 
            return False