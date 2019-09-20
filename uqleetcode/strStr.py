class Solution:
    def strstr(self, haystack, needle):
        c = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                c = i
                break
        return c


if __name__ == '__main__':
    a = Solution()
    h = input()
    n = input()
    print(a.strstr(h, n))
