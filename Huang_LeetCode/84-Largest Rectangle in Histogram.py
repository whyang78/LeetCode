class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        ans = 0
        for k, height in enumerate(heights):
            while height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = k - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(k)
        heights.pop()
        return ans