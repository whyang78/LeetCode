class Solution:
    def movezeros(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow = slow + 1
        return nums


if __name__ == '__main__':
    a = Solution()
    num = [int(n) for n in input().split()]
    print(a.movezeros(num))
