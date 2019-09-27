class Solution:
    def addBinary(self, a, b):
        a, b = int(a, 2), int(b, 2)
        ans = bin(a+b)
        ans = str(ans)
        return ans[2:]


if __name__ == '__main__':
    s = Solution()
    ia = input()
    ib = input()
    print(s.addBinary(ia, ib))
