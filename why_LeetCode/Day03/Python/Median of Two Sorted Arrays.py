class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        a=sorted(nums)
        total=len(a)-1
        key=total//2
        if total%2==0:
            return float(a[key])
        else:
            return float(a[key]+a[key+1])/2.0