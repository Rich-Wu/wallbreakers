from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int) -> None:
            rows = len(grid)
            cols = len(grid[0])
            sides = 0
            if row + 1 >= rows or grid[row + 1][col] == 0:
                sides += 1
            if row - 1 < 0 or grid[row - 1][col] == 0:
                sides += 1
            if col + 1 >= cols or grid[row][col + 1] == 0:
                sides += 1
            if col - 1 < 0 or grid[row][col - 1] == 0:
                sides += 1
            grid[row][col] = -1
            if row + 1 < rows and grid[row + 1][col] == 1:
                sides += dfs(row + 1, col)
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                sides += dfs(row - 1, col)
            if col + 1 < cols and grid[row][col + 1] == 1:
                sides += dfs(row, col + 1)
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                sides += dfs(row, col - 1)
            return sides
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)
