class Solution:
    def reverse(self, x: int) -> int:
        # x // max(1, abs(x)) 相当于cmp函数
        r = x // max(1, abs(x)) * int(str(abs(x))[::-1])
        return r if r.bit_length() < 32 or r == -2**31 else 0