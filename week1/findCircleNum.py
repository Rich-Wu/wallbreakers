from typing import List

# Naive Union Find Object with just parent reference
class DisjointSetNode:
    def __init__(self):
        self.parent = self
        
    def find(self) -> 'DisjointSetNode':
        while (self.parent != self):
            self = self.parent
        return self

    def union(self, node2: 'DisjointSetNode') -> None:
        self = self.find()
        node2_root = node2.find()
        if self != node2_root:
            node2_root.parent = self
        else:
            return

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        circles = [DisjointSetNode() for x, _ in enumerate(M)]
        for row_i, row in enumerate(M):
            for col_i, col in enumerate(row[row_i:]):
                if col == 1:
                    circles[col_i].union(circles[row_i])
        print(circles)

Solution.findCircleNum(Solution, [[1,1,0,1], [1,1,0,1], [0,0,1,0], [1,1,0,1]])