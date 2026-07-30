class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = {}
        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if t[i] in map_s:
                map_s[t[i]] -= 1
            
                if map_s[t[i]] == 0:
                    del map_s[t[i]]
            else:
                return False
        return len(map_s) == 0