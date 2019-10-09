## 66 Plus One（加一）

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

**示例 1:**

```
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
```

## Add

从低位到高位进位。最高位有溢出时，补一位。

```c++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();
        digits[len - 1] += 1;
        // cout << digits[len - 1] << endl;
        int flag = digits[len - 1]/10;
        digits[len - 1] = digits[len - 1]%10;
        // cout << digits[len - 1] << endl;
        // cout << flag;
        int i = len - 2;
        while (i >= 0) {
            digits[i] += flag;
            flag = digits[i]/10;
            digits[i] %= 10;
            i--;
        }
        if (flag) digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

