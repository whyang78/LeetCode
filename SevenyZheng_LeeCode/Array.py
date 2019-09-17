# -*- coding: utf-8 -*-


"""
2.1.1 Remove Duplicates from Sorted Array

题目描述：给定一个排序后的数组，删除重复项，使得每个元素只出现一次，并返回新数组长度。
不要分配额外的数组空间，必须在使用常量内存的地方执行此操作，空间复杂度要求为O(1)。

思路：因为是有序数组，故只要比较数组中前后两两元素是否相等，若相等删除其中一个。

"""

class Solution:
    def removeDuplicates(self,nums:list[int]) -> int:
        index = 0
        while index < len(nums) -1:
            if nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1
        lens = len(nums)
		return(lens) 
	



"""
2.1.2 Remove Duplicates from Sorted Array II

题目描述：给定一个排序后的数组，删除重复项，使得每个元素最多可出现二次，并返回新数组长度。
不要分配额外的数组空间，必须在使用常量内存的地方执行此操作，空间复杂度要求为O(1)。

思路：同上题I，且新增一个变量count，用以记录数组中重复元素的出现次数，每当count>2时，删除一个重复元素。

"""

class Solution:
	def removeDuplicates(self,nums:list[int]) -> int:
		index = 0
		count = 1
		while index < len(nums) - 1:
			if nums[index] = nums[index + 1]:
				count += 1
				if count > 2:
					nums.pop(index)
				else:
					index += 1
			else:
				index += 1
				count = 1
		return len(nums)

		
"""
2.1.3 Search in Rotated Sorted Array

题目描述：假设一个排序后的数组在某个未知的轴上旋转。（例：0,1,2,4,5,6,7 变成 4,5,6,7,0,1,2）。
给定要搜素的目标值，如果在数组中找到，返回它的索引，否则返回-1。
你可以假设数组中无重复元素。

思路1：二分查找

思路2：每旋转一次，即每次将数组中第一个元素截取出来，放到数组的最后一个位置上。因此，旋转k次，即将数组中前k个元素截取出来，不改变顺序地放到数组的末尾。故可采用list自带的切片功能，将旋转k次后切片的数组 与 剩余的数组 拼接起来，形成新的数组。

"""



#思路二
class Solution:
    def Rotated(self,nums,target_value):
        index = 0
		while index < len(nums):
			if target_value == nums[index]:
				k = index + 1
				nums[:] = nums[(len(nums)-k-1):] + nums[:(len(nums)-k-1)]
				break
			else:
				index += 1
	
			if index >= len(nums):
				return(-1)
				break
	
		return(k,nums)	

	def Rotated(nums,target_value):
		index = 0
		while index < len(nums):
			if target_value == nums[index]:
				k = index + 1
				nums[:] = nums[(len(nums)-k-1):] + nums[:(len(nums)-k-1)]
				break
			else:
				index += 1
	
			if index >= len(nums):
				return(-1)
				break
	
		return(k,nums)		
		

