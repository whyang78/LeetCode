# 返回数组中不重复的元素个数
# 设置两个下标，index作为参照，i下标从头到尾开始遍历
# 当两个下标对应的值不相等时，开始进行交换
def removeDuplicates(nums):
    if not nums:
        return 0
    index = 0
    for i in range(len(nums)):
        if nums[index] != nums[i]:
            index = index + 1
            nums[index] = nums[i]
    return index + 1


print(removeDuplicates(sorted([1, 2, 3, 2, 2, 3, 1])))

