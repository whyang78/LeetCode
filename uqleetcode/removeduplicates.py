class Solution:
    def removeduplicates(self, nums):
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j = j + 1
            else:
                nums[i+1] = nums[j]
                i = i + 1
                j = j + 1
        return i+1


if __name__ == '__main__':
    a = Solution()
    num = [int(n) for n in input().split()]
    l = a.removeduplicates(num)
    print(num[:l])
