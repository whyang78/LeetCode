## Question: 3Sum Closest 

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2) .

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

---------

## Analysis

与上一题3Sum类似，排序，固定左侧一个值，然后左右夹逼，$\mathcal{O}(n)$。

```C++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int tmp;
        int res = nums[0] + nums[1] + nums[nums.size() - 1];
        cout << res << endl;
        for (int i = 0 ; i < nums.size(); ++i) {
            int fix = nums[i];
            int lp = i + 1, rp = nums.size() - 1;
            while (lp < rp) {
                tmp = fix + nums[lp] + nums[rp];
                // cout << "tmp = " << tmp << " ";
                if (abs(res - target) >= abs(tmp - target)) res = tmp;
                // cout << "res = " << res << " ";
                if (tmp > target) rp--;
                else if (tmp < target) lp++;
                else return res;
            } 
        }
        return res;
    }   
};
```

