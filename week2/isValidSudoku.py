from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for row in board]
        cols = [set() for col in board[0]]
        square = [set() for num in range(0, 9)]
        for row_i, row in enumerate(board):
            for col_i, block in enumerate(row):
                square_num = calc_squ_num(row_i, col_i)
                if block != '.':
                    if block in rows[row_i]:
                        return False
                    if block in cols[col_i]:
                        return False
                    if block in square[square_num]:
                        return False
                    rows[row_i].add(block)
                    cols[col_i].add(block)
                    square[square_num].add(block)
        return True
    
def calc_squ_num(row: int, col: int) -> int:
    if row <= 2:
        if col <= 2:
            return 0
        elif 3 <= col <= 5:
            return 1
        elif col >= 6:
            return 2
    elif 3 <= row <= 5:
        if col <= 2:
            return 3
        elif 3 <= col <= 5:
            return 4
        elif col >= 6:
            return 5
    elif row >= 6:
        if col <= 2:
            return 6
        elif 3 <= col <= 5:
            return 7
        elif col >= 6:
            return 8
    return  
