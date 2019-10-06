## 80 Remove Duplicates from Sorted Array II（删除排序数组中的重复项 II）

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。



## 与Remove Duplicates from Sorted Array类似，增加一个计数变量来记录出现的次数即可。

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

