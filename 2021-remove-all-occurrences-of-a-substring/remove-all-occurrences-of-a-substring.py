class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        s_list = s.split()
        partLen = len(part)

        while part in s:
            idx = s.find(part)
            s = s[:idx] + s[(idx + partLen):]
        
        return s