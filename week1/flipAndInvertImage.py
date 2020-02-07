from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        cols = []
        for i in range(0, len(A)):
            row = []
            for j in range(len(A[i]) - 1, -1, -1):
                row.append(0) if A[i][j] == 1 else row.append(1)
            cols.append(row)
        return cols