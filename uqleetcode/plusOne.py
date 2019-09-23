class Solution:
    def plusone(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        num = num + 1
        d = []
        sn = str(num)
        for j in range(len(sn)):
            d.append(int(sn[j]))
        return d


if __name__ == '__main__':
    a = Solution()
    n = [int(n) for n in input().split(" ")]
    print(a.plusone(n))
