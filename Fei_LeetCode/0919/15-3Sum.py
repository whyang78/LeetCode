# 题目要求在一个数组里找到所有三个数相加等于0的值并返回
# 思路：先将数组进行排列，然后从左右两边开始逼近,将三个数的和与0相比较，从而控制左右的移动
def threeSum(nums):
    fx = 0
    rly = []  # 用于接收符合要求的值
    for i in range(int(len(sorted(nums)) - 2)):  # 将数组进行排序,因为是3个数相加，当遍历到倒数第三个数时即可停止
        j = i + 1
        k = len(nums) - 1  # k从最右边开始
        while j < k:
            sum_three = nums[i] + nums[j] + nums[k]
            if fx == sum_three:
                rly.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif sum_three > fx:
                k -= 1
            else:
                j += 1
    return rly

