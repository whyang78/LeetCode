# 递减栈+哈希表
def nextGreaterElement(self, nums1: list, nums2: list):
    stack, hashmap = list(), dict()
    res = []
    for n2 in nums2:
        while stack and stack[-1] < n2:
            hashmap[stack.pop()] = n2
        stack.append(n2)
    for n1 in nums1:
        res.append(hashmap.get(n1, -1))
    return res


# 暴力法
def nextGreaterElem(self, nums1, nums2):
    res = []
    for n1 in nums1:
        temp = -1
        for n2 in nums2[nums2.index(n1):]:
            if n2 > n1:
                temp = n2
                break
        res.append(temp)
    return res
