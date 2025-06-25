import numpy as np

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        grid = np.asarray(grid)
        ones_row = grid.sum(axis=1) * 2 - len(grid)
        ones_column = grid.sum(axis=0) * 2 - len(grid[0])

        out = ones_row[:, None] + ones_column

        return out.tolist()