class Solution:
    def longestValidParentheses(self, s: str) -> int:
    # Initialize max_len to track the longest valid substring length
        max_len = 0
        # Stack to hold indices of unmatched characters, start with -1 as base
        stack = [-1]
        # Iterate through each character in the string with its index
        for i in range(len(s)):
            # If current char is '(', push its index onto the stack
            if s[i] == '(':
                stack.append(i)
            else:
                # For ')', pop the last unmatched '(' index
                stack.pop()
                # If stack is empty, this ')' is unmatched, push current i as new base
                if not stack:
                    stack.append(i)
                else:
                    # Calculate length of current valid substring: i - top of stack
                    max_len = max(max_len, i - stack[-1])
        # Return the maximum length found
        return max_len