## Question: Permutation Sequence 

The set [1,2,3,... ,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive. 

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

## Analysis

从最小排列（升序）开始，共找k-1次nextPermutation即可。

```c++
class Solution {
public:
    string getPermutation(int n, int k) {
        string s(n, '0');
        for (int i = 0; i < n; ++i)
            s[i] += i+1;
        for (int i = 0; i < k-1; ++i)
            nextPermutation(s);
        return s;
    }
    
private:
    void nextPermutation(string& nums) {
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

