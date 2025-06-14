class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                # Update each element to be: current + min(child1, child2)
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
        
        # The top of the triangle now contains the minimum path sum
        return dp[0]