class Solution:
    def minInsertions(self, s: str) -> int:
        t=s[::-1]
        n=len(s)
        dp=[0]*(n+1)

        for i in range(1,n+1):
            prev=0
            for j in range(1,n+1):
                temp=dp[j]
                if s[i-1]==t[j-1]:
                    dp[j]=1+prev
                else:
                    dp[j]=max(dp[j],dp[j-1])
                prev=temp
        return n-dp[n]