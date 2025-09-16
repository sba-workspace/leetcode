class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        # Initialize first row
        dp = [j for j in range(m + 1)]
        
        for i in range(1, n + 1):
            prev = dp[0]  # dp[i-1][0]
            dp[0] = i     # converting word1[:i] -> empty string needs i deletions
            for j in range(1, m + 1):
                temp = dp[j]  # store current dp[j] before updating
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(
                        dp[j] + 1,    # delete
                        dp[j - 1] + 1, # insert
                        prev + 1       # replace
                    )
                prev = temp
        return dp[m]
