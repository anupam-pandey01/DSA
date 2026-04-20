from copy import deepcopy
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        grid_copy = deepcopy(grid)
        queue = deque([])
        fresh_org = 0

        for i in range(rows):
            for j in range(cols):
                if grid_copy[i][j] == 1:
                    fresh_org += 1
                if grid_copy[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        
        while len(queue) != 0 and fresh_org > 0:
            minutes += 1
            total_rotten = len(queue)

            for _ in range(total_rotten):
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni = i + dx
                    nj = j + dy

                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                        continue
                    
                    if grid_copy[ni][nj] == 2 or grid_copy[ni][nj] == 0:
                        continue
                    
                    grid_copy[ni][nj] = 2
                    queue.append((ni, nj))
                    fresh_org -= 1

        if fresh_org > 0:
            return -1
        
        return minutes
            
         
