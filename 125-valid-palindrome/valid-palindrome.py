class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        def helper(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return helper(left + 1, right - 1)
        
        return helper(0, len(s) - 1)