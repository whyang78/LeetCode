class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 0-9的阶乘
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 康托编码
        res = ''
        k -= 1
        for i in reversed(range(n)):
            cur = self.nums[k // self.fac[i]]
            res += str(cur)
            self.nums.remove(cur)
            if i != 0:
                k %= self.fac[i]
                self.fac[i] //= i
        return res
