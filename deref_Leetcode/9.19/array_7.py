'''
力扣 1
两数之和：

'''
#方法-
def twosums1(nums,target):
    '''

    :param nums:List[int]
    :param target: int
    :return: int
    '''
    #解题关键是nums2=target-nums1 是否也在list中
    #nums2 in nums 返回true
    #nums.index(num2)
    lens=len(nums)
    j=-1
    for i in range(1,lens):
        temp = nums[:1]
        if (target-nums[i]) in temp:
            j=temp.index(target-nums[i])
            break
    if j >=0:
        return [j,i]
nums=[2,3,4,6,7]
target=6
print(twosums1(nums,target))


#方法二：通过哈希来求解，这里通过字典来模拟哈希查询的过程
def twosums2(nums,target):
    '''

    :param nums: List[int]
    :param target: int
    :return: List[]
    '''
    hashmap={}
    for key,value in enumerate(nums):
        hashmap[value]=key
    for i ,num in enumerate(nums):
        j=hashmap.get(target-num)
        if j is not None and i!=j:
            return [i,j]
nums=[2,3,4,6,7]
target=6
print(twosums2(nums,target))
#方法三：同样是字典法，只不过和方法一类似，不在整个字典中查找。而是在nums1之前的字典中查找
def twosums3(nums,target):
    '''

    :param nums:List[int]
    :param target: [int]
    :return: List[]
    '''
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target-num) is not None:
            return [hashmap.get(target-num),i]
        hashmap[num]=i
nums=[2,3,4,6,7]
target=6
print(twosums3(nums,target))
#换一种写法：
def twosum4(nums,target):
    '''

       :param nums:List[int]
       :param target: [int]
       :return: List[]
       '''
    dict={}
    for i,num in enumerate(nums):
        if target-i in dict:
            return [dict[target-i],i]
        dict[num]=i
nums=[2,3,4,6,7]
target=6
print(twosum4(nums,target))
#为什么不是从0开始呢