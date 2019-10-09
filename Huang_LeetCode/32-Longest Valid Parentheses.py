class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        stack = [-1]

        for k, ch in enumerate(s):
            if ch == '(':
                stack.append(k)
            else:
                stack.pop()
                if stack:
                    maxLength = max(maxLength, k - stack[-1])
                else:
                    stack.append(k)
        return maxLength