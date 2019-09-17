# 数组2

## Question: Remove Duplicates from Sorted Array II 

Follow up for ”Remove Duplicates”: What if duplicates are allowed at most twice?
For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3] 



增加一个计数变量来记录出现的次数即可。

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int n = 1, index = 0;	//n记录出现的次数；index新数组的索引
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[index] == nums[i]) {
                n++;
                if (n < 3) nums[++index] = nums[i];
            }
            else {
                nums[++index] = nums[i]; n = 1;
            }
        }
        return index+1;
    }
};
//
//增加一个计数变量，若和前一个数相等，计数加1，若不超过2，就记录，否则不记录
//已排序数组，若是新的数，肯定没出现过，直接加进来，计数为1

```

