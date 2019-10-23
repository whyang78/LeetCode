'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
def find(target,array):
    i=0
    j=len(array[0])-1
    while i < len(array) and j>=0:
        base = array[i][j]
        if target == base:
            return i,j
        elif target >base:
            i += 1
        else:
            j-=1
    return False
print(find(10,[[1,2,8,9],[2,4,10,11],[3,5,12,13]]))

