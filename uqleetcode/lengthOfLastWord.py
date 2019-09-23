class Solution:
    def lengthoflastword(self, s):
        return len(s.rstrip().split(" ")[-1])


if __name__ == '__main__':
    a = Solution()
    sw = input()
    print(a.lengthoflastword(sw))
