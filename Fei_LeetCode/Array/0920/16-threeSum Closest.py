def threeSumClosest(nums: list, target: int):
    list.sort(nums)
    rlt = nums[0] + nums[1] + nums[len(nums) - 1]
    for i in range(len(nums) - 2):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            three_sum = nums[i] + nums[start] + nums[end]
            if three_sum > target:
                end -= 1
            else:
                start += 1
            if abs(three_sum - target) < abs(rlt - target):
                rlt = three_sum
    return rlt


print(threeSumClosest([-1, 2, 1, -4], 1))

