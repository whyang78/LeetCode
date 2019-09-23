# 题目要求在一个数组里找到所有三个数相加等于0的值并返回
# 思路：先将数组进行排列，然后从左右两边开始逼近,将三个数的和与0相比较，从而控制左右的移动
def threeSum(nums):
    fx = 0
    rly = []  # 用于接收符合要求的值
    nums_sort = sorted(nums)
    for i in range(int(len(nums_sort) - 2)):  # 将数组进行排序,因为是3个数相加，当遍历到倒数第三个数时即可停止
        j = i + 1
        k = len(nums_sort) - 1  # k从最右边开始
        while j < k:
            sum_three = nums_sort[i] + nums_sort[j] + nums_sort[k]
            if fx == sum_three:
                rly.append([nums_sort[i], nums_sort[j], nums_sort[k]])
                j += 1
                k -= 1
            elif sum_three > fx:
                k -= 1
            else:
                j += 1
    return set(tuple(row) for row in rly)


print(threeSum([-1, 0, 1, -2, 2, 3]))
