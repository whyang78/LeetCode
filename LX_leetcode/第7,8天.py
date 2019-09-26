 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        import operator
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i] += 1
        count = sorted(dict1.items(),key = operator.itemgetter(1),reverse = True)
        return count[0][0]

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            res += (ord(s[i])-64) * (26**(n-i-1))
        return res

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        # nums = sorted(nums)
        for i in range(n):
            nums.remove(0)
            nums.append(0)
        # return nums

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = 1
        while res < n:
            res *= 3
        return res == n
