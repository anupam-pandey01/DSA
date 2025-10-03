class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def safe(board, n, row, col):
            # horizontal Direction Check
            for j in range(n):
                if board[row][j] == "Q":
                    return False
            
            # vertical Directin Check
            for i in range(n):
                if board[i][col] == "Q" :
                    return False
            
            r = row
            c = col
            # diagonal Left
            while(r >= 0 and c >= 0):
                if(board[r][c] == "Q"):
                    return False
                r -= 1
                c -= 1
            
            r = row 
            c = col
            # diaginal Right
            while(r >= 0 and c < n):
                if(board[r][c] == "Q"):
                    return False
                
                r -= 1
                c += 1
            
            return True

        def backtrack(board, n, ans, row):
            if row == n:
                ans.append(["".join(r) for r in board])  
                return

            for i in range(0, n):
                if safe(board, n, row, i):
                    board[row][i] = "Q"
                    backtrack(board, n, ans, row + 1)
                    board[row][i] = "."
    
        backtrack(board, n, ans, 0)
        return ans