class Solution:
    def newjewelsinstone(self, J, S):
        n = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    n = n + 1
        return n


if __name__ == '__main__':
    a = Solution()
    sj = input()
    ss = input()
    print(a.newjewelsinstone(sj, ss))
