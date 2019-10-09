class Solution:
    def removeelement(self, nums, val):
        i = 0
        # j = len(nums) - 1
        # while i <= j:
        #     if nums[i] == val:
        #         if nums[j] != val:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i = i + 1
        #             j = j - 1
        #         else:
        #             j = j - 1
        #     else:
        #         i = i + 1
        # return i
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i = i + 1
        return len(nums)


if __name__ == '__main__':
    a = Solution()
    num = [int(n) for n in input().split()]
    v = int(input())
    print(num)
    nl = a.removeelement(num, v)
    print(num[:nl])
