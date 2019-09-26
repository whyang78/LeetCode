# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一
# 考虑三种情况，将每种情况进行处理，过于复杂了

def plusOne(digits: list):
    if digits[-1] != 9:
        digits[-1] += 1
    # elif len(digits) == 1:
    #     digits[-1] = 0
    #     digits.insert(0, 1)
    else:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                continue
            break
        if digits[i] == 9:
            for j in range(0, len(digits)):
                digits[j] = 0
            digits.insert(0, 1)
        else:
            digits[i] += 1
            for k in range(i+1, len(digits)):
                digits[k] = 0
    return digits

# 参考别人的做法，更加简单，设置一个常量为1，从又开始遍历，若相加等于10，则令其等于0
# 不然则加一，令常量变成0，再与前面的元素相加不改变其值
def plusOne1(digits: list):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] + carry == 10:
            digits[i] = 0
        else:
            digits[i] = digits[i] + carry
            carry = 0
        if digits[0] == 0:
            return [1] + digits
    return digits


print(plusOne1([9, 9, 9]))
