class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        while left < right:
            res, left, right = (max(res, height[left] * (right - left)),
                                left + 1,
                                right) if height[left] < height[right] else (
                                    max(res, height[right] * (right - left)),
                                    left, right - 1)
        return res