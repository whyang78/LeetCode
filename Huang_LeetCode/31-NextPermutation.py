class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        # 从右到左遍历,找到交换点索引
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            return nums.reverse()  # 如果完全递减,将数字排成最小的序列
        else:
            nums[i:] = sorted(nums[i:])  # 交换点后的数字进行升序排列
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]  #交换
                    break