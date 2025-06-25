from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        
        onesRow = [sum(row) for row in grid]
        onesCol = [sum(grid[i][j] for i in range(n)) for j in range(m)]
        
        # diff = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                grid[i][j] = 2 * (onesRow[i] + onesCol[j]) - n - m
        
        return grid
