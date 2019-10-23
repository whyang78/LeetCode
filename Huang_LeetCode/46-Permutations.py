class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[n] + sub for i, n in enumerate(nums)
                for sub in self.permute(nums[:i] + nums[i + 1:])] or [nums]