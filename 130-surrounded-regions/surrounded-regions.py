from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque([])

        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[rows - 1][c] == "O":
                queue.append((rows - 1, c))
        
        for r in range(1, rows - 1):
            if board[r][0] == "O":
                queue.append((r, 0))
            
            if board[r][cols - 1] == "O":
                queue.append((r, cols - 1))
        
        while queue:
            r, c = queue.popleft()
            visited[r][c] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr = r + dx
                nc = c + dy

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if visited[nr][nc] == 1 or board[nr][nc] == "X":
                    continue
                
                queue.append((nr, nc))
        
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"