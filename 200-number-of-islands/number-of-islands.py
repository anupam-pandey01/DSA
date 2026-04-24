from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
                    count += 1

                    while queue:
                        r, c = queue.popleft()

                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr = r + dx
                            nc = c + dy

                            if 0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                visited[nr][nc] = 1
                    
        return count