class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])  # 行和列数
        cur = [0] * c
        cur[0] = 1 - obstacleGrid[0][0]  # 判断起始点是否有障碍(障碍处设为0,无障碍处设为1)
        for i in range(1, c):  # 依次填充第一列
            cur[i] = cur[i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):  # 从上到下按行填充每一列
            cur[0] *= 1 - obstacleGrid[i][0]
            for j in range(1, c):
                cur[j] = (cur[j - 1] + cur[j]) * (
                    1 - obstacleGrid[i][j]
                )  # 每一个格子的路径等于它上方和左方的路径之和,是障碍处则设为零
        return cur[-1]
