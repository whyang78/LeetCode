'''
题目说明：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，
返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例：
给定 nums = [1,1,1,2,2,3]
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素
'''

#方法一
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #array长度小于2的话直接返回原array
        if len(nums) <= 2:
            return len(nums)

        j = 0
        count = 1
        Max = 2
        #从index=1开始判断
        for i in range(1, len(nums)):
            #遇到相同的数字且出现次数没有达到最大值
            if nums[j] == nums[i] and count < Max:
                j += 1
                count += 1
                nums[j] = nums[i]
            #遇到新数字
            elif nums[j] != nums[i]:
                count = 1 #重置计数值
                j += 1
                nums[j] = nums[i]
        return j + 1

#方法二
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        index = 2
        for i in range(2, len(nums)):
            if nums[index - 2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index