class Solution:
    def maxScore(self, n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
        colmax = [max(travelScore[i][j] for i in range(n)) for j in range(n)]
        dp = [max(stayScore[0][j], colmax[j]) for j in range(n)]
        for i in range(1, k):
            ndp = [0]*n
            for j in range(n):
                best = 0
                for u in range(n):
                    v = dp[u] + travelScore[u][j]
                    best = max(best, v)
                stay = dp[j] + stayScore[i][j]
                ndp[j] = max(best, stay)
            dp = ndp
        return max(dp)