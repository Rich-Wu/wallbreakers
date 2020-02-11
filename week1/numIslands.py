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
    def numIslands(self, grid: List[List[str]]) -> int:
        # Creates another 2-D grid containing a new DSN if the space in grid is "1" else the grid space is empty
        mapping = [[DisjointSetNode() if space == '1' else None for space in row] for row in grid]
        # Iterates through each space in grid searching for "1"
        for row_i, row in enumerate(grid):
            for col_i, block in enumerate(row):
                # If "1" is found, search() is run
                if block == '1':
                    self.search(grid, mapping, row_i, col_i)
        islands = set()
        # Iterates over mapping
        for row_i, row in enumerate(mapping):
            for col_i, node in enumerate(row):
                # If DSN is found at coordinate, node is added to islands set
                if node:
                    islands.add(node.find())
        # Final answer is the number of entries in islands set
        return len(islands)
                    
    # Adjacent sides of the space are checked for other "1"s and if they're found, those nodes' parent pointers are pointed to the original DSN
    def search(self, grid: List[List[str]], mapping: List[List['DisjointSetNode']], row: int, col: int) -> None:
        # Left
        if col - 1 >= 0 and grid[row][col - 1] == '1':
            mapping[row][col].union(mapping[row][col - 1])
        # Right
        last_col = len(grid[0]) - 1
        if col + 1 <= last_col and grid[row][col + 1] == '1':
            mapping[row][col].union(mapping[row][col + 1])
        # Top
        if row - 1 >= 0 and grid[row - 1][col] == '1':
            mapping[row][col].union(mapping[row - 1][col])
        # Bottom
        last_row = len(grid) - 1
        if row + 1 <= last_row and grid[row + 1][col] == '1':
            mapping[row][col].union(mapping[row + 1][col])