## 67 Add Binary（[二进制求和](https://leetcode-cn.com/problems/Add-Binary/)）

> 给定两个二进制字符串，返回他们的和（用二进制表示）。
>
> 输入为非空字符串且只包含数字 1 和 0。
>

**示例 1:**

```
输入: a = "11", b = "1"
输出: "100"
```


**示例 2:**

```
输入: a = "1010", b = "1011"
输出: "10101"
```

### 由低位到高位，做带进位加法，也就是从字符串末尾往前，倒着加，每一位结果拼接在res后面，最高位若有进位，在res最后添加一位1，最终将res翻转返回。

```C++
class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int flag = 0;
        for (int i = a.size() - 1, j = b.size() - 1;
               i >= 0 || j >= 0;
               i--, j--) {
            // cout << i << ",  " << j << endl;
            int ai = (i >= 0) ? a[i] - '0' : 0;
            int bj = (j >= 0) ? b[j] - '0' : 0;
            int tmp = ai + bj + flag;
            flag = tmp / 2;
            res += (tmp % 2 == 0)?'0':'1';            
        }
        if (flag)
            res += '1';
        reverse(res.begin(), res.end());
        return res;
               
    }
};
```

