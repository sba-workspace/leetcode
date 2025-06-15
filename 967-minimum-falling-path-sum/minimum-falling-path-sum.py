class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])

        dp=[[0]*m for i in range(n)]

        dp[0]=matrix[0][:]

        for i in range(1,n):
            for j in range(m):
                if j==0:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
                elif j==(m-1):
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+matrix[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
        
        return min(dp[-1])