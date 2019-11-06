## 96 Unique Binary Search Trees（[不同的二叉搜索树](https://leetcode-cn.com/problems/Unique-Binary-Search-Trees/)）

```
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
```

**示例:**

```
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

#### 以某一个小于等于n的数为根节点，计算left个数和right个数相乘；再将所有不同根节点的树相加。

```c++
class Solution {
public:
    int numTrees(int n) {
        if (n <= 1) return 1;
        vector<int> map {1, 1};
        for (int i = 2; i <= n; i++) {
            int tmp = 0;
            for (int j = 1; j <= i; j++) {
                int left = map[j - 1];
                int right = map[i - j];
                tmp += left * right;
            }
            map.push_back(tmp);
        }
        return map[map.size() - 1];
    }
};
```

