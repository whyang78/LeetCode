'''
从排序数组中删除重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
'''

class List(object):
    pass

class Solution():
    def removeDuplicates(self,nums):
        '''
        :type nums:List[int]
        '''
        if len(nums)==0:
            return 0
        New_nums=[]
        i=0

        for j in range(1,len(nums)):
            if (nums[j]!=nums[i]):
                i+=1
                nums[i]=nums[j]
                New_nums.append(nums[i])
        return i+1,New_nums



nums= [1,1,1,2,2,2,2,3]
a=Solution()
print(a.removeDuplicates(nums))
'''
此题是一个双指针问题，i是慢指针，j是快指针。
两个指针，一个指向遍历的元素，一个指向可以写入的位置，后者的大小是小于等于前者的。
其中i是可以写入的位置，j是指向遍历的
有问题，怎么样输出剩余数组
'''