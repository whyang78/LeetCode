# 假设原数组已经排好序了,从第二个元素开始遍历，比较其左右两边的值
# 当不相等时，将i的值传给count下标的值

def removeDuplicates(nums):
    if len(nums) < 3:
        return len(nums)
    count = 1
    for i in range(1, len(nums) - 1):
        if nums[i - 1] != nums[i + 1]:
            nums[count] = nums[i]
            count += 1
    nums[count] = nums[-1]
    return count + 1


print(removeDuplicates([1, 1, 1, 1, 3, 3, 3, 4, 4, 5]))
