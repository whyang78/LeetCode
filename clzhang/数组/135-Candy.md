## Candy （分糖果）

老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

**示例 1:**

```
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
```

一个vector，初始化为最少，全1。搞一个变量，记邻居娃糖的个数，初始化也为1。

相邻的孩子中，评分高的孩子必须获得更多的糖果。也就是每个娃跟他的左右邻居之间都满足这种关系。

先看左邻居。

从第二个娃开看始，如果比左邻居评分高，让个数比左邻居多1。否则，不变，看下一个娃。

再先看右邻居，左邻居的关系是从左往右推出来的，判断右邻居倒着从后往前看。方法相同。



左右邻居都应满足这种，每个娃取左右邻居判断的结果中，较大的数。

```C++
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> numbers(n, 1);
        for (int i = 1, inc = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1])
                numbers[i] = max(++inc, numbers[i]);
            else
                inc = 1;
        }
        for (int i = n - 2, inc = 1; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1])
                numbers[i] = max(++inc, numbers[i]);
            else
                inc = 1;
        }
        return accumulate(numbers.begin(), numbers.end(), 0);
    }
};
```



```C++
//std::accumulate, #include <numeric>

accumulate(numbers.begin(), numbers.end(), 0); //默认累加，也可以实现累乘，一连串与、或、异或等等。

std::accumulate(v.begin(), v.end(), 1, multiplies<int>()); //乘法
```

