## 33 Search in Rotated Sorted Array（搜索旋转排序数组）

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中***不存在重复的元素***。

你的算法时间复杂度必须是 ***O(log n)*** 级别。

## 分析

根据复杂度要求，须得用二分查找，但旋转数组不是有序的。二分查找每次需要排除一半的序列。

左右边界的确定！下一次在哪一半中搜索？

发现取中间位置mid，总有一边是有序的，因为一边要是含有旋转点，另一边就是有序的递增的，这时只用比较这另一边的两端点与target值的大小，就能判断target在不在有序的这半边，这样就能去掉一半序列，就能完成二分查找。

```c++
//2019/0917
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;	//空序列，返回-1；
        int lo = 0, hi = nums.size();
        while (lo != hi) {
            int mid = lo + (hi - lo) / 2;	//找中点
            if (nums[mid] == target) return mid;	//看是不是中点，是就返回
            if (nums[lo] <= nums[mid]) {	//若左半边有序（即lo<mid）
                if (target >= nums[lo] && target < nums[mid]) { hi = mid; }
                else { lo = mid + 1; }
            }
            else {	//若右半边有序（即mid>hi）
                if (target > nums[mid] && target <= nums[hi-1]) { lo = mid + 1; }
                else { hi = mid; }
            }
        }
        return -1;
    }
};
```

