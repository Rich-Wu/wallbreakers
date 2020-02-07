from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[x][y] for x in range(len(A))] for y in range(len(A[0]))]