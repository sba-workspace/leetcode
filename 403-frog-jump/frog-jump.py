class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N=len(stones)

        dp=[[0]*(N+1) for _ in range(N)]
        dp[0][1]=1

        for i in range(N):
            for j in range(i):
                diff=stones[i]-stones[j]

                if(diff<0 or diff>N or (not(dp[j][diff]))):
                    continue
                dp[i][diff]=1
                if(diff-1>=0):
                    dp[i][diff-1]=1
                if(diff+1<=N):
                    dp[i][diff+1]=1
                if(i==N-1):
                    return True
        return False
