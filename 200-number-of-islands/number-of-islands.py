class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c, grid, visited, rows, cols):
            visited[r][c] = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = dx + r
                nc = dy + c

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if grid[nr][nc] == "0":
                    continue
                if visited[nr][nc] == 1:
                    continue
                
                dfs(nr, nc, grid, visited, rows, cols)

        rows = len(grid)
        cols = len(grid[0])
        visited = [[ 0 for _ in range(cols)] for _ in range(rows)]
        island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    island += 1
                    dfs(i, j, grid, visited, rows, cols)

        return island