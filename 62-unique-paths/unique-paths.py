class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Space complexity O(n) TC-O(mXn)
        dp = [1] * n  


        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]  # Current cell = above (dp[j]) + left (dp[j-1])

        return dp[-1]