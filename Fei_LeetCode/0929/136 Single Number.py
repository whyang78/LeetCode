# 在一个数组里面查找只出现一次的数
# 用异或来做最简单
def singleNumber(nums):
    r = 0
    for i in nums:
        r ^= i
    return r


if __name__ == '__main__':
    print(singleNumber([1, 2, 1]))
