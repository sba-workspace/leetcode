class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo={0:0}

        def min_coins(amt):

            if amt in memo:
                return memo[amt]
            minm=float('inf')
            for coin in coins:
                diff=amt-coin
                if diff<0:
                    break
                minm=min(minm,1+min_coins(diff))
            
            memo[amt]=minm
            return minm


        res=min_coins(amount)
        if res<float('inf'):
            return res
        else:
            return -1