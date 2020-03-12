from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_i in range(len(board)):
            for col_i in range(len(board[row_i])):
                if board[row_i][col_i] == word[0]:
                    if self.dfs(board, word[1:], (row_i, col_i), [(row_i, col_i)]):
                        return True
        return False
    
    def dfs(self, board, word: str, coords: tuple, used: List[tuple]) -> bool:
        row, col = coords
        if word == "":
            return True
        if (row + 1, col) not in used and row + 1 < len(board) and board[row + 1][col] == word[0]:
            if self.dfs(board, word[1:], (row + 1, col), used + [(row + 1, col)]): return True
        if  (row - 1, col) not in used and row - 1 >= 0 and board[row - 1][col] == word[0]:
            if self.dfs(board, word[1:], (row - 1, col), used + [(row - 1, col)]): return True
        if (row, col + 1) not in used and col + 1 < len(board[0]) and board[row][col + 1] == word[0]:
            if self.dfs(board, word[1:], (row, col + 1), used + [(row, col + 1)]): return True
        if (row, col - 1) not in used and col - 1 >= 0 and board[row][col - 1] == word[0]:
            if self.dfs(board, word[1:], (row, col - 1), used + [(row, col - 1)]): return True
        return False