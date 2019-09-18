'''
搜索旋转排序数组：力扣33
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例：
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''
'''
解：二分查找：线性表必须采用顺序结构，而且表中元素按关键字有序排列
1：假设表中元素按升序排列，将表中间位置记录的关键字与查找关键字比较，若两者相等将查找成功
2：否则，利用中间位置记录将表分成前后两个子表，若中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找
后一子表。
3：重复以上过程，直到满足条件的记录，查找成功；或者直到子表不存在为止。
'''
## 中间元素和右边界比较，使用右中位数
class Solution():
    def search(self,nums,target):
        '''

        :param nums: List[int]
        :param target: [int]
        :return: [int]
        '''
        size=len(nums)
        #特判
        if size==0:
            return -1
        left=0
        right=size-1
        while left<right:
            mid=left+(right-left+1)//2
            if nums[mid]<nums[right]:
                if nums[mid]<=target<=nums[right]:
                    left=mid
                else:
                    right=mid-1
            else:
                if nums[left]<=target<=nums[mid-1]:
                    right=mid-1
                else:
                    left=mid
        return left if nums[left]==target else -1
nums =[4,5,6,7,0,1,2]
target = 0
a=Solution()
print(a.search(nums,target))
#关于二分法的模板
class Solution_m():
    def search(self,nums,target):
        '''

        :param nums: List[int]
        :param target: int
        :return: int
        '''
        size=len(nums)
        if size==0:
            return 0
        left = 0
        right=size-1
        while left <right:
            mid=left+(right-left+1)//2
            if nums[mid]<target:
                left=mid+1
            else:
                assert nums[mid]>=target
                right=mid
        return left
nums=[1,2,3,5,7,9]
target=3
b=Solution_m()
print(b.search(nums,target))
