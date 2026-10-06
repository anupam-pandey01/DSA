class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0 
        j = 0
        maxFreq = 0
        maxLen = 0
        map = {}
        
        while j < len(s):
            map[s[j]] = map.get(s[j], 0) + 1
            maxFreq = max(maxFreq, map[s[j]])

            if ((j-i+1) - maxFreq) > k:
                map[s[i]] -= 1
                i+=1
            maxLen = max(maxLen, j-i+1)
            j+=1
        return maxLen