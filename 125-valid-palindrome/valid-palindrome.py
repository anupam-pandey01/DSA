class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphabet(ch):
            if (
                (ch >= "0" and ch <= "9") or
                (ch >= "a" and ch <= "z") or
                (ch >= "A" and ch <= "Z")
            ):
                return True

            return False
        
        st = 0
        end = len(s) - 1

        while st < end:
            if not isAlphabet(s[st]):
                st+=1
                continue
            
            if not isAlphabet(s[end]):
                end -= 1
                continue
            
            if s[st].lower() != s[end].lower():
                return False
            
            st += 1
            end -= 1
        
        return True