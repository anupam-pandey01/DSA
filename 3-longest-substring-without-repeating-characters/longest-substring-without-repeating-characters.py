class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0

        i=0
        j=0

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1

            seen.add(s[j])
            maxLength = max(len(seen), maxLength)
            j+=1
        
        return maxLength