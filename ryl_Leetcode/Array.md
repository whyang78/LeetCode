## 26. Remove Duplicates from Sorted Array

题目描述：给定一个排序数组，移除数组中重复的元素，空间复杂度要求为O(1)

解题思路：引入一个标记变量，该标记变量用来记录数组中最终保留下的最新的元素的位置。该变量初始化为0位置，从1位置开始遍历整个数组。当array[i]!=array[index]时，index和i一起往后移动，需要注意的是array[i]的值应该是index+1位置上面的值，因为i在index的前面（这也是最后返回的时候是index+1，而不是index的原因）。如果相等，只移动i。只移动i相当于把重复的元素给略过了。

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty())  return 0; 
        
        int index = 0;
        for (int i = 1; i<nums.size(); i++)
        {
            if(nums[index] != nums[i])
                nums[++index] = nums[i];
        }
        return index + 1; 
    }
};
```

## 80. Remove Duplicates from Sorted Array II 

题目描述：与Remove Duplicates from Sorted Array基本是一样的，只不过这里允许最多重复的数字为2

结题思路：结题思路也与I很相似，只不过这里需要在I的基础上在引入一个变量来记录重读的次数。这里最多允许有两个重复，言下之意就是在代码实现的时候最多只允许跳过一次重复的数。这里可以继续扩展到最多允许3个或者n个重复数字，在代码实现的时候就是允许跳过n-1次重复的数字，在这之后只能如果还出现重复的数字，那么就应该将循环变量往后面移动，将多余的重复的数字去掉。

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<2) return nums.size();
        
        int len = nums.size();
        int count = 1;
        int index = 0;
        for (int i=1; i<len; i++)
        {
            if(nums[index] == nums[i] && count<2)
            {
                count++;
                nums[++index] = nums[i];
            }
            else if(nums[index] != nums[i])
            {
                count = 1;
                nums[++index] = nums[i];
            }
        }
        
        return index+1;
    }
};
```

