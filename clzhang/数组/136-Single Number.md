## 136. Single Number（只出现一次的数字）

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1:**

```
输入: [2,2,1]
输出: 1
```

**示例 2:**

```
输入: [4,1,2,1,2]
输出: 4
```

考察异或。

0 xor a = a，0 xor a xor a = 0，异或还可以交换，偶数次的异或抵消掉了，就只留下只出现一次的数。用1连续去异或所有的数，得到的结果就是single number。



```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int num = 0;
        for (int i = 0; i < nums.size(); ++i) {
            num ^= nums[i];
        }
        return num;
    }
};
```


