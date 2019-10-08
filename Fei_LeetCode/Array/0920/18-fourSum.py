# 通过两个循环遍历，左右逼近
# 但这样做会超时
def fourSum(nums, target):
    list.sort(nums)
    rlt = []
    for i in range(len(nums)-3):
        start = i + 2
        end = len(nums) - 1
        for j in range(i+1, len(nums)-2):
            while start < end:
                four_sum = nums[i] + nums[j] + nums[start] + nums[end]
                if four_sum == target:
                    rlt.append([nums[i], nums[j], nums[start], nums[end]])
                elif four_sum > target:
                    end -= 1
                else:
                    start += 1
    return set(tuple(row) for row in rlt)


print(fourSum([-2, -1, 0, 0, 1, 2], 0))
