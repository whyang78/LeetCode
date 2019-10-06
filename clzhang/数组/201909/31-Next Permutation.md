## 31 Next Permutation（下一个排列）

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

-----------------

## Analysis

从最低位考虑，找到第一个不满足从低到高位逐渐增大的数，例如02431从最低位1到高位不满足逐渐增大的第一个数就是2，说明2以后的三个数（431）已经是这三个数能 组成的最大的数了，所以下一个排列肯定要把2考虑进去，而2之前的0就不用考虑了。既然要把2考虑进去，就说明要用一个数来替换2，取431中比2大的最小的那个数字即3（这个过程是一个在有序数组里进行查找的过程，可以用二分）， 然后将3和2替换得到3421，然后再将421 reverse得到3124即可。3124是刚好比2431大的排列。

```C++
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() > 1) {
            int i = nums.size() - 1;
            while (i > 0 && nums[i - 1] >= nums[i]) i--;    //找最后一个nums[i - 1] < nums[i]的位置
            if (i == 0) {
                sort(nums.begin(), nums.end());
            }
            else {
                int mid, low = i, high = nums.size() - 1;
                while(low <= high){ // 二分查找比nums[i]大的数
                    mid = low + (high - low) / 2;
                    if(nums[mid] <= nums[i - 1]) high = mid - 1;
                    else low = mid + 1;
                }; 
                swap(nums[i-1], nums[high]);    //找比nums[i]大的数，交换
                reverse(nums.begin() + i, nums.end());
            }
            
        }
    }
};
```

