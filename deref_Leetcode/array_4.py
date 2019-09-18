'''
搜索排序数组，力扣81
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:
这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
'''
class Solution():
    def search(self,nums,target):
        '''

        :param nums: List[int]
        :param target: [int]
        :return:boolean
        '''
        #若第一个数和最后一个数不相等，那么和上一题没有区别
        #若第一个数和最后一个数相等，而且等于target，return ture
        #若第一个数和最后一个数相等，但是不等于target。那么就需要遍历两个升序数组的其中一个。以确定target
        if not nums:
            return  False
        if nums[0] != nums[-1]:
            return self.search1(nums,target)
        if nums[0]==nums[-1]:
            if nums[0]==target:
                return True
            else:
                for num in nums:#直接遍历整个数组
                    if num==target:
                        return True
                return False
                #return self.search2(nums,target)

    def search1(self,nums,target):
        size = len(nums)
        # 特判
        if size == 0:
            return -1
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid
        return True if nums[left] == target else False
nums = [2,5,6,0,0,1,2]
target = 4
a=Solution()
print(a.search(nums,target))