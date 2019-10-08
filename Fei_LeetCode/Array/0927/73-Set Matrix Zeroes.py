# 设置两个集合来存放矩阵里元素等于0的行列
# 在遍历完后在集合进行寻找
def setMatrixZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])
    row_nums, col_nums = set(), set()
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row_nums.add(i)
                col_nums.add(j)

    for i in range(row):
        for j in range(col):
            if i in row_nums or j in col_nums:
                matrix[i][j] = 0
    return matrix


if __name__ == '__main__':
    print(setMatrixZeroes([
        [1, 2, 0],
        [1, 1, 1],
        [0, 3, 9]
    ]))
