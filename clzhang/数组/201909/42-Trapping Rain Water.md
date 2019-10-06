## 42 Trapping Rain Water（接雨水）

给定n个非负整数表示每个宽度为1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

**示例:**

```
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
```

### 每个柱子所在位置的雨水量，跟它左右两侧最高的柱子有关，是他左右两侧最高的柱子的较小值与自己的差；但不能为负，所以找左右两侧最高的柱子时范围应包含自己；

### 最后将这些值累加。

```C++
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) return 0;
        int wide = height.size();
        vector<int> left_max(wide), right_max(wide);
        int ans = 0;
        left_max[0] = height[0];
        for (int i = 1; i < wide; i++) {
            left_max[i] = max(left_max[i - 1], height[i]);
        }
        right_max[wide - 1] = height[wide - 1];
        for (int i = wide - 2; i >= 0; i--) {
            right_max[i] = max(right_max[i + 1], height[i]);
        }
        //0 和wide-1 其实不用累加，两侧柱子肯定没有雨水
        for (int i = 0; i < wide; i++) {
            ans += min(right_max[i], left_max[i]) - height[i];
        }
        return ans;
    }
};

```

