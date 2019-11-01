class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 状态转移方程 dp[k][i]:到底i天经过k次交易得到的最大利润
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):  # k 为交易次数
            pre_max = -prices[0]  # 处理边界情况
            for i in range(1, n):  # i 为交易天数
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]