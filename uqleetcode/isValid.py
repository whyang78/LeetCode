class Solution:
    def isvalid(self, s):
        stack = [0]*len(s)    # 生成定长list
        top = -1
        if not s:
            return True
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                top += 1
                stack[top] = s[i]
            elif s[i] == ')' and stack[top] == '(':
                top -= 1
            elif s[i] == ']' and stack[top] == '[':
                top -= 1
            elif s[i] == '}' and stack[top] == '{':
                top -= 1
            else:
                return False
        if top == -1:
            return True
        else:
            return False

    def isvalid1(self, s):
        dic = {'(': ')', '[': ']', '{': '}', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    a = Solution()
    ks = input("请输入一段括号字符：")
    print(a.isvalid1(ks))
