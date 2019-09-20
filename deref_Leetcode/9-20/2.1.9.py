'''
力扣  16
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与target最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

'''
'''
思路：双指针的解法，建立l和r两个指针，然后进行遍历nums
'''
def threesums(nums,target):
    '''

    :param nums:List[]
    :param target: int
    :return: List[]
    '''
    result=list()
    nums.sort()
    for i,m in enumerate(nums[0:-2]):
        l,r = i+1,len(nums)-1
        if nums[l] + nums[l+1] +m>target:
            result.append(nums[l]+nums[l+1]+m)
        elif nums[r]+nums[r-1]+m<target:
            result.append(nums[r]+nums[r-1]+m)
        else:
            while l<r:
                result.append(nums[r]+nums[r]+m)
                if nums[l]+nums[r]+m<target:
                    l+=1
                elif nums[l]+nums[r]+m>target:
                    r-=1
                else:
                    return target
    result.sort(key=lambda x :abs(x-target))
    return result[0]
nums =[-1,-2,4,1]
target=1
print(threesums(nums,target))