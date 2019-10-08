class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] =nums[len(nums)-k:] +nums[:len(nums)-k]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        pro = 0
        for i in range(0,m-1):
            if prices[i] < prices[i+1]:
                pro -= prices[i]
                pro += prices[i+1]
        return pro
