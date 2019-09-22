'''
力扣 18
四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 arget相等？
找出所有满足条件且不重复的四元组。
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
'''
思路：先将数组排序固定两个元素在用两个指针，一个指向头，一个指向尾，
看四数之和为多少，太大了右指针左移，太小了左指针右移，因为有可能存在重复的数组，先将结果保存在set中，最后在转为list输出

'''

def foursum(nums,target):
    '''

    :param nums: List[int]
    :param target: int
    :return: List[List[int]]
    '''
    
    nums.sort()
    ans=set()
    for i in range(len(nums)-3):
        for j in range(i+1,len(nums)-2):
            left = j+1#左指针
            right=len(nums)-1#右指针
            while(right>left):
                temp=nums[i]+nums[j]+nums[left]+nums[right]
                if temp==target:
                    ans.add((nums[i],nums[j],nums[left],nums[right]))
                    left+=1
                    right-=1
                if temp>target:right-=1
                if temp<target:left+=1
    rec=[]
    for i in ans:
        rec.append(list(i))
    return rec

nums = [1, 0, -1, 0, -2, 2]
target=0
print(foursum(nums,target))