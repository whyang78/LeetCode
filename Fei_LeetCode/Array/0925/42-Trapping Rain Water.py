# 用栈来实现
def trap(self, height: list[int]) -> int:
    res, curr, stack = 0, 0, []
    while curr < len(height):
        while stack and height[curr] > height[stack[-1]]:
            top = height[stack.pop()]
            if not stack: break
            distance = curr - stack[-1] - 1
            h = min(height[curr], height[stack[-1]]) - top
            res += distance * h
        stack.append(curr)
        curr += 1
    return res
