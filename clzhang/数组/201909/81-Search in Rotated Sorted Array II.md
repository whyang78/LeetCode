## 81 Remove Duplicates from Sorted Array II（搜索旋转排序数组 II）

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

**示例 1:**

```
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
```

## 分析

同样，有一边是递增（允许重复时可以说成是不减的），允许重复时，上一题中的mid大于等于lo的条件就不能推出递增，比如[1,3,1,1,1] ，但mid>lo肯定是能得到递增的，那就再加一个判断条件mid==lo看是个什么情况。

mid==lo,不定，但可以去掉原来的lo这个点因为mid点不是target才会执行下来，那么lo也不是，那就可以lo加1继续下一次。

最坏的情况，每次去除掉一个点，复杂度为
$$
\mathcal{O}(n)
$$


```c++
//2019/0917
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (nums.empty()) return false;	//空序列，返回false；
        int lo = 0, hi = nums.size();
        while (lo != hi) {
            int mid = lo + (hi - lo) / 2;	//找中点
            if (nums[mid] == target) return true;	//看是不是中点，是就返回
            if (nums[lo] < nums[mid]) {	//若左半边有序递增（即lo<mid）
                if (target >= nums[lo] && target < nums[mid]) { hi = mid; }
                else { lo = mid + 1; }
            }
            else if (nums[lo] > nums[mid]) {	//若右半边有序（即lo>mid旋转点在左边，那右边就是递增的）
                if (target>nums[mid] && target<=nums[hi-1]) {lo = mid + 1;}
                else { hi = mid; }
            }
            else lo++;	//mid=lo无法判断那一边递增，但可以去掉原来的lo这个点因为mid点不是target才会执行下来，那么lo也不是，lo加1继续
        }
        return false;
    }
};
```
