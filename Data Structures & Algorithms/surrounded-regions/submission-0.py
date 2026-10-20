class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r not in range(ROWS) or c not in range(COLS)
                or board[r][c] != "O"):
                return

            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)
        
        # 1. (DFS) capture unsurrounded regions [O -> T]
        for r in range(ROWS):
            for c in range(COLS):
                if ((r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1) and board[r][c] == "O"):
                    capture(r, c)
        
        # 2. capture surrounded regions [O -> X]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. uncapture surrounded regions [T -> O]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"