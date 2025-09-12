class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[0]*(m+1)

        for i in range(1,n+1):
            prev=0
            for j in range(1,m+1):
                temp=dp[j]
                if word1[i-1]==word2[j-1]:
                    dp[j]=1+prev
                else:
                    dp[j]=max(dp[j],dp[j-1])
                prev=temp
        return (n-dp[m])+(m-dp[m])