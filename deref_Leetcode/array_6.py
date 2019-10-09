'''
力扣128
最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''
'''
官方题解：
'''
#方法一：时间复杂度为o(n^3),
#思路： 可以枚举每个数字作为序列的第一个数字，搜索所有的可能性。
class Solution1():
    def longest(self,nums):
        longest_streak=0
        for num in nums:
            current_nums = num
            current_streak = 1
            while current_nums+1 in nums:
                current_nums +=1
                current_streak +=1
            longest_streak=max(longest_streak,current_streak)
        return longest_streak

#方法二：O(nlgn)
#排序：将数组中的数字升序迭代，找连续数字会变得十分容易。为了将数组变得有序，我们将数组进行排序
class Solution2():
    def longest2(self,nums):
        if not nums:
            return 0
        nums.sort()
        longest_streak = 1
        current_streak =1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak +=1
                else:
                    longest_streak = max(longest_streak,current_streak)
                    current_streak=1
        return max(longest_streak,current_streak)
#方法三：哈希表使用，
#这些数字用一个 HashSet 保存（或者用 Python 里的 Set），实现 O(1)时间的查询，
# 同时，我们只对 当前数字 - 1 不在哈希表里的数字，作为连续序列的第一个数字去找对应的最长序列，
# 这是因为其他数字一定已经出现在了某个序列里。
class Solution3():
    def longest3(self,nums):
        longest_streak=0
        num_set = set(nums)
        for num in num_set:
            current_num = num
            current_streak=1
            while current_num+1 in num_set:
                current_num+=1
                current_streak+=1

            longest_streak = max(longest_streak, current_streak)
        return longest_streak
nums=[100,2,3,1,5,7,8,6,21,45,2,1,]
a=Solution1()
b=Solution2()
c=Solution3()
print(a.longest(nums))
print(b.longest2(nums))
print(c.longest3(nums))
