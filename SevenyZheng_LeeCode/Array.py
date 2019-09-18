# -*- coding: utf-8 -*-


"""
2.1.1 Remove Duplicates from Sorted Array

题目描述：给定一个排序后的数组，删除重复项，使得每个元素只出现一次，并返回新数组长度。
不要分配额外的数组空间，必须在使用常量内存的地方执行此操作，空间复杂度要求为O(1)。

思路：因为是有序数组，故只要比较数组中前后两两元素是否相等，若相等删除其中一个。

"""

class Solution:
    def removeDuplicates(self,nums) -> int:
        index = 0
        while index < len(nums) -1:
            if nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1
        print("去重后数组为：",nums,"列表长度为：",len(nums))
        return 
	



"""
2.1.2 Remove Duplicates from Sorted Array II

题目描述：给定一个排序后的数组，删除重复项，使得每个元素最多可出现二次，并返回新数组长度。
不要分配额外的数组空间，必须在使用常量内存的地方执行此操作，空间复杂度要求为O(1)。

思路：同上题I，且新增一个变量count，用以记录数组中重复元素的出现次数，每当count>2时，删除一个重复元素。

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        count = 1
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                count += 1
                if count > 2:
                    nums.pop(index)
                else:
                    index += 1
            else:
                index += 1
                count = 1
        print("去重后数组为：",nums,"列表长度为：",len(nums))
        return

		
"""
2.1.3 Search in Rotated Sorted Array

题目描述：假设一个排序后的数组在某个未知的轴上旋转。（例：0,1,2,4,5,6,7 变成 4,5,6,7,0,1,2）。
给定要搜素的目标值，如果在数组中找到，返回它的索引，否则返回-1。
你可以假设数组中无重复元素。

思路1：利用数组被切分成两部分升序空间的特性，找到两段空间的交错点；再分别对两段空间实行二分查找

思路2：每旋转一次，即每次将数组中第一个元素截取出来，放到数组的最后一个位置上。因此，旋转k次，即将数组中前k个元素截取出来，不改变顺序地放到数组的末尾。故可采用list自带的切片功能，将旋转k次后切片的数组 与 剩余的数组 拼接起来，形成新的数组。

"""

#思路一
class Solution:
    def binary_search(self,target_value,nums):
        """
        正常二分法查找代码
        """
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target_value:
                l = mid + 1
            elif nums[mid] > target_value:
                r = mid - 1
            else:
                index = mid
                break
        return index

    def Rotated(self,nums,target_value):
        """
        :type nums:list[int]
        :type target_value:int
        :rtype:int
        """
        pol = len(nums) - 1 #从数组末尾开始找第二段升序空间的七点
        while pol > 0 and nums[pol] >= nums[pol - 1]:
            pol -= 1
            ans = self.binary_search(target_value,nums[:pol])#对前面这段升序空间实行二分查找
            if ans == -1:#若未找到
                ans = self.binary_search(target_value,nums[pol:])#继续在后面的升序空间实行二分查找
                if ans != -1:#第二次找到
                    return True
                else:
                    return False
            else:
                return True
            
        

#思路二
class Solution:
    def Rotated(self,nums,target_value):
        index = 0
        while index <= len(nums) -1:
            if nums[index] == target_value:
                k = index + 1
                nums[:] = nums[index+1:] + nums[:index+1]
#                nums[:] = nums[(len(nums)-k-1):] + nums[:(len(nums)-k-1)]
                break
            else:
                index += 1
                if index >= len(nums):
                    return(-1)
                    break
                    
                else:
                    continue
            
        print("目标值为：",target_value,"旋转后的数组为：",nums,"旋转次数为：",k)
        return


"""
2.1.4 Search in Rotated Sorted Array II
题目描述：假设一个排序后的数组在某个未知的轴上旋转。（例：0,1,2,4,5,6,7 变成 4,5,6,7,0,1,2）。
给定要搜素的目标值，如果在数组中找到，返回它的索引，否则返回-1。
假设数组中有重复元素。

思路1：代码同上题。利用数组被切分成两部分升序空间的特性，找到两段空间的交错点；再分别对两段空间实行二分查找

思路2：代码同上题。每旋转一次，即每次将数组中第一个元素截取出来，放到数组的最后一个位置上。因此，旋转k次，即将数组中前k个元素截取出来，不改变顺序地放到数组的末尾。故可采用list自带的切片功能，将旋转k次后切片的数组 与 剩余的数组 拼接起来，形成新的数组。
注意，思路2 这里是返回重复元素中的第一个

"""		

#思路一
class Solution:
    def binary_search(self,target_value,nums):
        """
        正常二分法查找代码
        """
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target_value:
                l = mid + 1
            elif nums[mid] > target_value:
                r = mid - 1
            else:
                index = mid
                break
        return index

    def Rotated(self,nums,target_value):
        """
        :type nums:list[int]
        :type target_value:int
        :rtype:int
        """
        pol = len(nums) - 1 #从数组末尾开始找第二段升序空间的七点
        while pol > 0 and nums[pol] >= nums[pol - 1]:
            pol -= 1
            ans = self.binary_search(target_value,nums[:pol])#对前面这段升序空间实行二分查找
            if ans == -1:#若未找到
                ans = self.binary_search(target_value,nums[pol:])#继续在后面的升序空间实行二分查找
                if ans != -1:#第二次找到
                    return True
                else:
                    return False
            else:
                return True
            
            
"""
2.1.5 Median of Two Sorted Arrays
题目描述：存在两个排序数组A和B，其数组长度分别为m和n。找出这两数组合并后的中位数。

思路1：将两数组合并后排序，设合并后数组长度为l。若l为奇数时，中位数的下标为l/2；若l为偶数，中位数的下标为l/2-1和下标l/2两个元素的平均值。

思路2：

"""	


