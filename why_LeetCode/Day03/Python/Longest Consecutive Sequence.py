'''
类似于c++的第二种方法。
建立一个哈希表，key是区间端点，val是这段区间的长度。


线性扫描输入数组，如果当前元素已经在哈希表里，则跳过，


如果不在哈希表里，就看一下它左右两侧区间的长度left，right，
计算出它自身的区间长度length = 1 + left + right。


计算完之后更新新的左右端点的长度为，
len_dict[num - left] =length = len_dict[num + right],
len_dict[num]也赋值，为了占个位子。

重点：两个端点，以及区间长度。

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_dict={}
        longest=0
        
        for num in nums:
            if num not in len_dict:
                left=len_dict.get(num-1,0)
                right=len_dict.get(num+1,0)
                
                length=left+right+1;
                longest=max(longest,length)
                
                for i in [num-left,num,num+right]:
                    len_dict[i]=length
        return longest