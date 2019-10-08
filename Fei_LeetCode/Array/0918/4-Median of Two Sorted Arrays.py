# 将两个已经分好类的数组进行合并，返回合并后的数组中位数
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    sorted_list = list(sorted(nums1 + nums2))
    length = len(sorted_list)
    half_index = length // 2  # //除法表示整数除法，/表示浮点除法
    if length % 2 == 0:
        return (sorted_list[half_index - 1] + sorted_list[half_index]) / 2.0
    else:
        return float(sorted_list[half_index])
