'''
力扣 4
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
'''
class Solution():
    def findMedian(self,nums1,nums2):
        '''

        :param nums1:List[int]
        :param nums2: List[int]
        :return: float
        '''
        m,n=len(nums1),len(nums2)
        A=nums1
        B=nums2
        #让n成为那个长度大的数组
        if m>n:
            A, B, m, n = B, A, n, m
        if n==0:
            raise ValueError
        #在【0，m】区间进行查找
        imin=0
        imax=m
        half_len=int((m+n+1)/2)
        while imin <= imax:
            i=int((imin+imax)/2)
            j=half_len-i
            if i <m and B[j-1] >A[i]:
                imin = i+1
            elif i > 0 and A[i-1] >B[j]:
                imax=i-1
            else:
                if i==0:
                    max_of_left = B[j-1]
                elif j==0:
                    max_of_left = A[i-1]
                else:
                    max_of_left=max(A[i-1],B[j-1])
                if (m+n)%2==1:
                    return max_of_left
                if i==m:
                    min_of_right = B[j]
                elif j==n:
                    min_of_right=A[i]
                else:
                    min_of_right=min(A[i],B[j])
                return (max_of_left+min_of_right)/2.0




nums1 = [1, 3]
nums2 = [2]
a=Solution()
print(a.findMedian(nums1,nums2))
'''
思路：
1.有序数组中有一半的元素小于等于数组的中位数，有一半的元素大于等于中位数（如果数组中元素个数是奇数，
那么这里的一半并不是严格意义的1/2）
2.如果我们去掉其中一个数组比中位数小的k个数，再去掉另一个数组中比中位数大的k个数，得到的合并子数组的中位数和原来的中位数相同。
解：
'''