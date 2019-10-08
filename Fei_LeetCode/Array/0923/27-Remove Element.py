# 题目要求：给定一个目标值，删除其在数组内的所有元素
# 思想：引入一个为0的新索引，遍历数组，如果不等，索引增加，相等则跳过
# 时间复杂度O(n),空间复杂度O（1）
def removeElement(nums: list, val: int):
    index = 0
    for i in range(len(nums)):
        if val != nums[i]:
            nums[index] = nums[i]
            index += 1
    return index


nums1 = [3, 2, 2, 3, 0, 1, 3, 0]
for j in range(removeElement(nums1, 3)):
    print(nums1[j])
