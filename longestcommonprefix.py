class Solution:
    def longestCommonPrefix(self, s):
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res) - 1]
            i += 1
        return res


if __name__ == '__main__':
    S = Solution()
    list = []
    while True:
        item = input()
        if item == 'quit':
            break
        else:
            list.append(item)
    print("最长公共前缀为：%s"%S.longestCommonPrefix(list))



