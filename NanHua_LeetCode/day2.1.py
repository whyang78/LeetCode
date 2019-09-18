arr = list(input('输入一个排序后数组:'))
def char_int(a):
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,
           '6':6,'7':7,'8':8,'9':9
           }
    return dic[a]
arr = list(map(char_int,arr))
def seaerch(nums,target):
    if nums is None:
        return False
    left = 0
    right = len(nums)-1
    while(left != right):
        mid = (left + right) // 2
        if(nums[mid] == target):
            return mid
        elif(nums[mid]<target):
            left = mid

        else:
            right = mid
import random
tar = random.choice(arr)
print('array:{},target:{}'.format(arr,tar))
print(seaerch(arr,tar))
