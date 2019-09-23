class Solution:
    def trap(self, height: List[int]) -> int:
        # 找到最高的柱子,处理左边一半,处理右边一半
        max = 0
        for i in range(len(height)):
            if height[i] > height[max]:
                max = i
        water, peak, top = 0, 0, 0
        for i in range(max):
            if height[i] > peak:
                peak = height[i]
            else:
                water += peak - height[i]
        for i in range(len(height) - 1, max, -1):
            if height[i] > top:
                top = height[i]
            else:
                water += top - height[i]
        return water
