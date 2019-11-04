class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s) + 1, len(t) + 1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]