from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)  # Memoization using Python's built-in cache
        def dp(i: int, j: int) -> bool:
            # If pattern is finished, string must also be finished
            if j == len(p):
                return i == len(s)

            # Check if first character matches
            first_match = (i < len(s) and (s[i] == p[j] or p[j] == '.'))

            # If next char in pattern is '*'
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Two options: skip '*' or use '*' if first char matches
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Move to next characters in both
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)