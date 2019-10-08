def rotate(matrix):
    row = len(matrix)
    col = 0
    if matrix[0]:
        col = len(matrix[0])  # 第一维度

    for i in range(row):
        for j in range(i + 1, col):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for r in matrix:
        r.reverse()
    return matrix


print(rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
