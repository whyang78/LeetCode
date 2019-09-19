# 数组4

## Question:  Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence. 

For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1, 

2, 3, 4]. Return its length: 4. 

Your algorithm should run in O(n) complexity.

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

## 分析

无序、$\mathcal{O}(n)$。哈希表。

以每个元素为中心，往两边寻找，出现过的数字不再使用。


```c++
//2019/0918
class Solution {    //最长连续序列
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, bool> used;  //哈希表used，用来存储每个元素是否使用过；使用true未使用false
        for (auto i : nums) used[i] = false;    //初始化false
        int longest = 0;
        for (auto i : nums) {
            if (used[i]) continue;
            int length = 1;
            used[i] = true;
            for (int j = i + 1; used.find(j) != used.end(); ++j) {	//正向找
                used[j] = true;
                length++;
            }
            for (int j = i - 1; used.find(j) != used.end(); --j) {	//反向找
                used[j] = true;
                length++;
            }
            longest = max(longest, length);
        }
        return longest;
    }
};
```
