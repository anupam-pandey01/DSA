class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        i = 0
        j = len(word) - 1

        while i < j:
            if word[i] == "":
                i+=1
                continue
            
            if word[j] == "":
                j -= 1
                continue
            
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        
        return " ".join(word)