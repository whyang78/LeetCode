# 在一个为sorted的数组内找到最长连续的子序列，并返回其length
def longestConsecutive(self, nums: list[int]) -> int:
    # for each num I will check whether num-1 exists
    # if yes, then I ignore this num
    # Otherwise if num-1 doesn't exist, then I will go till I can find num+1
    # so in a way I am only checking each number max once and once in set.

    st = set(nums)
    mx = 0
    for num in nums:
        if num - 1 not in st:
            tmp = 1
            while num + 1 in st:
                tmp += 1
                num += 1
            mx = max(mx, tmp)

    return mx