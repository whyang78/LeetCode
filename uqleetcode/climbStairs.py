class Solution:
    def climbStairs(self, n):
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])    # f(i)=f(i-1)+f(i-2),因为走到i阶楼梯的方法数是走到i-1阶楼梯方法数加上走到i-2阶楼梯方法数
        return f[n-1]


if __name__ == '__main__':
    a = Solution()
    N = int(input())
    print(a.climbStairs(N))
