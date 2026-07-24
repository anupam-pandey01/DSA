class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def isAlphabet(ch):
            if ( (ch >= "a" and ch <= "z") or
                (ch >= "A" and ch <= "Z") or
                (ch >= "0" and ch <= "9") ):
               return True
            
            return False

        while i < j:
            if not isAlphabet(s[i]):
                i += 1
                continue

            if not isAlphabet(s[j]):
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
            