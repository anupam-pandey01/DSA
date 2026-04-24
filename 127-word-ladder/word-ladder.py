from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level

            idx = 0

            while idx < len(word):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    # if word[idx] == c:
                    #     continue

                    newWord = word[:idx] + c + word[idx+1:]
                    if newWord in wordSet:
                        queue.append((newWord, level + 1))
                        wordSet.remove(newWord)
                idx += 1
            
        return 0
            