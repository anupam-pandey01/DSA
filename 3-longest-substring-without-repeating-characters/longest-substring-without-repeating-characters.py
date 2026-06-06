class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0 
        mySet = set()
        maxLen = 0

        while j < len(s):
            while s[j] in mySet:
                mySet.remove(s[i])
                i+=1

            mySet.add(s[j])
            maxLen = max(maxLen, j-i+1) 
            j+=1
            
        return maxLen              