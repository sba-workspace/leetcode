class Solution:
    def numDecodings(self, s: str) -> int:
    
        d = defaultdict(int)
        for i in range(1,27): d[str(i)] = 1
        for i in range(10): d["*"+str(i)] = 1 + (i< 7)
        d['*'], d['**'], d['1*'], d['2*']  = 9,15,9,6

        n, M = len(s)-1, 10**9+7
        dp = [d[s[0]]] + [0]*n + [1]

        for i in range(n):
            one, two = s[i+1], s[i]+s[i+1]

            dp[i+1] = (d[one] * dp[i  ] + 
                       d[two] * dp[i-1])%M
            if not dp[i+1]: return 0
            
        return dp[-2]