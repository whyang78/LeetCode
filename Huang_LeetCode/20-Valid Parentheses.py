class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '[': ']', '{': '}'}
        for k in s:
            if k in '{([':
                stack.append(k)
            else:
                if not stack or d[stack.pop()] != k:
                    return False
        return not stack