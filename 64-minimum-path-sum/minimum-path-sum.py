class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        #first row cumulative sums
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]

        # Fill dp for each subsequent row
        for i in range(1, m):
            dp[0] += grid[i][0]  # Update first column for current row
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[-1]