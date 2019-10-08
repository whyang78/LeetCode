"""
def garyCode(n: int):
    nums = [0]
    if n == 0:
        return nums
    else:
        length = 2 ** n
"""

# 用数学公式做
def grayCode(n: int):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n == 2:
        return [0, 1, 3, 2]
    else:
        return grayCode(n - 1) + [x + (2 ** (n - 1)) for x in grayCode(n - 1)[::-1]]  # 逆序


if __name__ == '__main__':
    x = int(input())
    print(grayCode(x))
