class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        map_s1 = {}
        map_s2 = {}
        window_size = len(s1)

        for i in range(len(s1)):
            map_s1[s1[i]] = map_s1.get(s1[i], 0) + 1

        j = 0
        i = 0
        while j < len(s2):
            map_s2[s2[j]] = map_s2.get(s2[j], 0) + 1

            if j-i+1 > window_size:
                map_s2[s2[i]] -= 1
                if map_s2[s2[i]] == 0:
                    del map_s2[s2[i]]
                i+=1
            
            if map_s2 == map_s1:
                return True
            
            j+=1
        return False
