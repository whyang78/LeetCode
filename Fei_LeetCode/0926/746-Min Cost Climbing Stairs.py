# 使用动态规划解法
# 初始化
# i=0时，只有一个阶梯，因此到达该阶梯顶部需要的能量即为到达该阶梯所需能量，为cost[0]；
# i=1时，有两个阶梯，我们可以迈两步，跳过第一级台阶，到达该阶梯所需要的能量为到达第二级台阶所需能量，为cost[1]；
# dp[i]表示到达下标为i的阶梯需要消耗的最小能量。这里需要注意，顶部阶梯实际上是被题目缺省掉的，
# 即到达顶部阶梯所需要消耗的能量为零，我们需要补回来

# 状态转移方程
# i>1时，到达第i级台阶只有两种选择，一种是从第i-1级台阶迈一步，另一种是从i-2级台阶迈两步，
# 这两种选择消耗的最少能量分别是dp[i-1]+cost[i]和dp[i-2]+cost[i]，我们取两者的最小值，即为到达下标为i的台阶所需的最少能量：
# dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
def minCostClimbingStairs(cost: list):
    if not cost:
        return 0
    if len(cost) <= 2:
        return min(cost)

    cost.append(0)
    dp = [None for _ in range(len(cost))]
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
    print(dp)
    return dp[-1]
