class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid) and len(grid[0])

        for i in range(1, n):  # 遍历第一行
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):  # 遍历第一列
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]