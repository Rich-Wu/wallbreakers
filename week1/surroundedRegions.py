from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        # Iterate over first and last rows and flag O's on the border as "S" (safe)
        for i in range(len(board[0])):
            last_row = len(board) - 1
            if board[0][i] == "O":
                board[0][i] = "S"
                self.search(board, 0, i)
            if board[last_row][i] == "O":
                board[last_row][i] = "S"
                self.search(board, last_row, i)
        # Iterate over first and last columns (exclude those of the first and last rows) and mark them "S"
        for i in range(1, len(board) - 1):
            last_col = len(board[0]) - 1
            if board[i][0] == "O":
                board[i][0] = "S"
                self.search(board, i, 0)
            if board[i][last_col] == "O":
                board[i][last_col] = "S"
                self.search(board, i, last_col)
        # All O's ajoined to a safe block has been marked safe
        # All remaining O's are to be marked X's 
        for row_i in range(len(board)):
            for col_i in range(len(board[0])):
                if board[row_i][col_i] == "O":
                    board[row_i][col_i] = "X"
                elif board[row_i][col_i] == "S":
                    board[row_i][col_i] = "O"
                    
    def search(self, board: List[List[str]], row: int, col: int) -> None:
        # Left
        if col - 1 > 0 and board[row][col - 1] == "O":
            board[row][col - 1] = "S"
            self.search(board, row, col - 1)
        # Right
        last_col = len(board[0]) - 1
        if col + 1 < last_col and board[row][col + 1] == "O":
            board[row][col + 1] = "S"
            self.search(board, row, col + 1)
        # Top
        if row - 1 > 0 and board[row - 1][col] == "O":
            board[row - 1][col] = "S"
            self.search(board, row - 1, col)
        # Bottom
        last_row = len(board) - 1
        if row + 1 < last_row and board[row + 1][col] == "O":
            board[row + 1][col] = "S"
            self.search(board, row + 1, col)
