class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([i for i in nums if i < target])

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
