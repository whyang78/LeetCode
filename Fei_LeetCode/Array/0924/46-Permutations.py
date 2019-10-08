# 输入一个数组实现其全排列输出

def permute(self, nums: list[int]) -> list[list[int]]:
    level = 0
    solution = []  # 用来存储生成的新列表
    self.permutation(nums, level, solution)
    return solution


def permutation(self, nums, level, solution):
    if level == len(nums):
        new_list = nums[:]
        solution.append(new_list)
    for i in range(level, len(nums)):
        self.swap(nums, level, i)
        self.permutation(nums, level + 1, solution)
        self.swap(nums, i, level)


# 交换两个值
def swap(self, nums, a1, a2):
    tmp = nums[a1]
    nums[a1] = nums[a2]
    nums[a2] = tmp
