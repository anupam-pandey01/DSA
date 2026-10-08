class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s): 
            return []
        
        map_s = {}
        map_p = {}
        result = []

        for i in range(len(p)):
            map_p[p[i]] = map_p.get(p[i], 0) + 1
        
        i = 0
        j = 0
        while j < len(s):
            map_s[s[j]] = map_s.get(s[j], 0) + 1
            if j - i + 1 == len(p):
                if map_s == map_p: 
                    result.append(i)
                map_s[s[i]]-=1
                if map_s[s[i]] == 0:
                    del map_s[s[i]]
                
                i += 1 
            j+=1        
        return result
        

        
