class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l, cost = 0, 0
        result = 0

        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))

            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            result = max(result, r - l + 1)
        
        return result