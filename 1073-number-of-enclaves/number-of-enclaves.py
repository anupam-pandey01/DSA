from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        for i in range(cols):
            if grid[0][i] == 1:
                queue.append((0, i))
                visited[0][i] = 1
        
        for j in range(cols):
            if grid[rows - 1][j] == 1:
                queue.append((rows - 1, j))
                visited[rows - 1][j] = 1
        
        for i in range(1, rows - 1):
            if grid[i][0] == 1:
                queue.append((i, 0))
                visited[i][0] = 1
        
        for j in range(1, rows - 1):
            if grid[j][cols - 1] == 1:
                queue.append((j, cols - 1))
                visited[j][cols - 1] = 1

        # BFS 
        while queue:
            r, c = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dx
                nc = c + dy

                if 0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0 and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count += 1

        return count


        
