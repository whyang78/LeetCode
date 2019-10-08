# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列
# 字典序的意思是 不同排列的先后关系是从左到右逐个比较对应的数字的先后来决定的
# 例如对于5个数字的排列 12354和12345，排列12345在前，排列12354在后
# 按照这样的规定，5个数字的所有的排列中最前面的是12345，最后面的是 54321

# 按照自己理解的下一个排列是
# 先找到最大元素以及其下标，如果刚好是逆序则直接调用sort()排序
# 如果不是则将最大值以及后面的值向前移一位，最大值前面的值放在末尾
# 但这样理解实现出来的是错的，等看看别人的思路再改
"""
def nextPermutation(nums: list):
    if len(nums) < 2:
        return
    max_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_index = i
    if max_val == nums[0]:
        list.sort(nums)
    else:
        val = nums[max_index-1]
        for j in range(max_index, len(nums)):
            nums[j - 1] = nums[j]
        nums[-1] = val
    return nums
"""
def nextPermutation(nums: list):
    length = len(nums)
    for i in range(length-1, 0, -1):  # 将步长改为-1即可从右往左开始遍历
        if nums[i] < nums[i+1]:
            for j in range():
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        while i + 1 < length-1:
            nums[i+1], nums[length-1] = nums[length-1], nums[i+1]
            i += 1
            length -= 1
        break
    return nums


print(nextPermutation([7, 5, 4, 6, 8, 2, 1, 0]))
