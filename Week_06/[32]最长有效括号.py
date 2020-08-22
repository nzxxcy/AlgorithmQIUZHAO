class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if i-1 >= 0 and s[i-1] == '(':
                    dp[i] = (dp[i-2] if i-2 >= 0 else 0) + 2
                elif s[i-dp[i-1]-1] == '(' and i-dp[i-1]-1 >= 0:
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0) + 2
        return max(dp)