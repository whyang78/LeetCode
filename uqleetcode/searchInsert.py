class Solution:
    def searchinsert(self, nums, target):
        # i = 0
        # if target > nums[len(nums) - 1]:
        #     return len(nums)
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         break
        # return i
        nums.append(target)
        nums.sort()
        return nums.index(target)


if __name__ == '__main__':
    a = Solution()
    num = [int(n) for n in input().split()]
    t = int(input())
    print(a.searchinsert(num, t))
