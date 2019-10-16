class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s[-1] == ' ':
            return 0
        else:
            return len(s.split(' ')[-1])

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <=1:
            return x
        r = x
        while r > x/r:
            r = (r+x/r)//2
        return int(r)
