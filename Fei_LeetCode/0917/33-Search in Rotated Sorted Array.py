# 在无重复的数组中找到给定值的下标
# 应该用二分法来做，下次改进
# 时间复杂度O(log n),空间复杂度O（1）

def search(nums: list, target: int):
    if target in nums:
        return nums.index(target)
    else:
        return -1
