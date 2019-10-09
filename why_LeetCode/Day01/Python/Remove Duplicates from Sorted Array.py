'''
题目要求：
给定一个排序数组，你需要在原数组中删除重复出现的元素，使得每个元素只出现一次，
返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例：
给定数组 nums = [1,1,2]
函数应该返回新的长度 2, 并且原数组nums的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(0, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
