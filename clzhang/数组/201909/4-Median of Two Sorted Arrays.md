## Question: Median of Two Sorted Arrays

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted 

arrays. The overall run time complexity should be O(log(m + n))

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

## bu dong

```c++
//2019/1006
class Solution {
public:
    double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        if (m > n) return findMedianSortedArrays(B, A);
        int lo = 0, hi = m, half = (m + n + 1) / 2;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int mid_2 = half - mid;
            //一端到端点，结果可以得到了，另外考虑。
            if (mid < hi && B[mid_2 - 1] > A[mid]) {
                //条件 mid < hi， 确保在移动lo时，lo=mid+1存在，最多和hi相等，不会溢出
                //此外 mid == hi时，也说明找到了。
                lo = mid + 1;
            }
            else if (mid > lo && B[mid_2] < A[mid - 1]) {
                //条件 mid > lo， 确保在移动lo时，hi=mid-1存在，最多和lo相等，不会溢出
                //此外 mid == lo时，也说明找到了。
                hi = mid - 1;
            }
            else {
                int maxLeft = 0;
                if (mid == 0) { maxLeft = B[mid_2 - 1]; }
                else if (mid_2 == 0) { maxLeft = A[mid - 1]; }
                else { maxLeft = max(A[mid - 1], B[mid_2 - 1]); }
                if ( (m + n) % 2 == 1 ) return maxLeft;
                cout << maxLeft << endl;
                int minRight = 0;
                if (mid == m) { minRight = B[mid_2]; }
                else if (mid_2 == n) { minRight = A[mid]; }
                else { minRight = min(B[mid_2], A[mid]); }
                cout << minRight << endl;

                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
};
```

