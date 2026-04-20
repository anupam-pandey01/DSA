from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = 1
        
        while len(queue) != 0:
            i, j, d = queue.popleft()
            distance[i][j] = d

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i + dx
                nj = j + dy
                if (0 <= ni < rows) and (0 <= nj < cols) and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, d + 1))
        return distance