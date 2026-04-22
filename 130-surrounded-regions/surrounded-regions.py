class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def marker(r, c):
            n_row = r
            n_col = c
            if n_row < 0 or n_row >= rows or n_col < 0 or n_col >= cols:
                return

            if visited[n_row][n_col] == 1 or board[n_row][n_col] != "O":
                return
                

            visited[n_row][n_col] = 1

            marker(n_row - 1, n_col)
            marker(n_row + 1, n_col)
            marker(n_row, n_col + 1)
            marker(n_row, n_col - 1)


        # Top
        for i in range(cols):
            if board[0][i] == "O":
                marker(0, i)

        # Bottom row
        for j in range(cols):
            if board[rows - 1][j] == "O":
                marker(rows - 1, j)  

        # Right 
        for i in range(1, rows - 1):
            if board[i][cols - 1] ==  'O':
                marker(i, cols - 1)
        
        # Left
        for j in range(1, rows - 1):
            if board[j][0] == "O":
                marker(j, 0)

        
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"
        

