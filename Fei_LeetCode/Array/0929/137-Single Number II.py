# 创建字典来存储数组中每个元素，并用键值来计数
# 找到只存储一次的值
def singleNumber2(nums):
    occur = {}
    ret = []
    for num in nums:
        if num not in occur:
            occur[num] = 1
        else:
            occur[num] += 1
    for elem in occur:
        if occur[elem] == 1:
            ret.append(elem)
            break
    return ret[0]


if __name__ == '__main__':
    print(singleNumber2([3, 3, 3, 2, 1, 1, 1]))