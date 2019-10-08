def pivotIndex(nums):
    # 这样会超时
    """
    sum1 = 0
    n = len(nums)
    if len(nums) == 0:
        return -1
    if sum(nums[1:n]) == 0:
        return 0
    for i in range(1, len(nums)):
        sum1 += nums[i-1]
        sum2 = 0
        for j in range(i+1, len(nums)):
            sum2 += nums[j]
        if sum1 == sum2:
            return i
        if i == len(nums) - 1:
            return -1
    """

    nums = [0] + nums + [0]
    left, right = 0, sum(nums[2:])
    for index in range(1, len(nums)-1):
        if left == right:
            return index-1
        left += nums[index]
        right -= nums[index+1]
    return -1
