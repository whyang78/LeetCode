class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for k in nums:
            x ^= k
        return x