## 137. Single Number II（只出现一次的数字II）

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1:**

```
输入: [2,2,3,2]
输出: 3
```

**示例 2:**

```
输入: [0,1,0,1,0,1,99]
输出: 99
```

按bit位操作，对于每一位，某个数出现三次，就是3的倍数，忽略它，所有的数对应位相加，除3取余，就是single number这一位对应的结果，因为出现三次的数加完除3取余就不见了。最后，将这些位组合起来。

```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        const int W = sizeof(int) * 8;
        int count[W];
        fill_n(&count[0], W, 0);
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < W; ++j) {
                count[j] += (nums[i] >> j) & 1;
                count[j] %= 3;
            }
        }
        int res = 0;
        for (int i = 0; i < W; ++i) {
            res += (count[i] << i);
        }
        return res;
        
    }
};
```


