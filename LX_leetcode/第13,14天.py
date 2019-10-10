class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a = a^i
        return a


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        n = len(digits)
        for i in range(n):
            nums +=digits[i]*10**(n-i-1)
        nums += 1
        result =[]
        for i in range(len(str(nums))):
            result.append(nums%10)
            nums = nums//10
        return result[::-1]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        ans = []
        for i in nums1:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] +=1
        for i in nums2:
            if i in hashMap and hashMap[i]!=0:
                ans +=[i]
                hashMap[i] -=1
        return ans
