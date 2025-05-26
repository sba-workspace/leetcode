class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        dp=[0]*(amount+1)

        for i in range(1,amount+1):
            minm=float('inf')
            for coin in coins:
                if i-coin<0:
                    break
                minm=min(minm,dp[i-coin]+1)
            dp[i]=minm
        
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1