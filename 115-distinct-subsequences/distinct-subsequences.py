class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        dp=[0]*(m+1)

        dp[m]=1
        
        for i in range(n-1,-1,-1):
            prev=1
            for j in range(m-1,-1,-1):
                temp=dp[j]
                if s[i]==t[j]:
                    dp[j]+=prev
                prev=temp
            
        return dp[0]