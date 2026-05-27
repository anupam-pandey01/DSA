from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        queue = deque([])
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for i in range(cols):
                if matrix[r][i] != 0:
                    matrix[r][i] = 0
            
            for j in range(rows):
                if matrix[j][c] != 0:
                    matrix[j][c] = 0
        