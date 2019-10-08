# 题目要求给定一个target值，在一个数组内找到两个值使得它们的和等于target
# 返回两个值的下标
# 直接做，用两个for循环遍历即可（若时间复杂度要求在O（n）的话，需要用hash来做）
def twoSum(self, nums: list, target: int):
    for i in range(len(nums)):
        fx = target - nums[i]
        for j in range(i+1, len(nums)):
            if fx == nums[j]:
                return i, j
