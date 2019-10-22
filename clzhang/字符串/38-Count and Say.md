## 38 Count and Say（[报数](https://leetcode-cn.com/problems/Count-and-Say/)）

> 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
>
> 1. 1
> 2. 11
> 3. 21
> 4. 1211
> 5. 111221
>    1 被读作  "one 1"  ("一个一") , 即 11。
>    11 被读作 "two 1s" ("两个一"）, 即 21。
>    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

> 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
>
> 注意：整数顺序将表示为一个字符串。
>

**示例 1:**

```
输入: 1
输出: "1"
```

**示例 2:**

```
输入: 4
输出: "1211"
```

#### 从头判断，计数设为一，看下一个数与当前数是否相等，相等计数加一，继续往后判断；不相等则停止，将当前数的个数及数字加到字符串中，再判断后面的数。

```C++
class Solution {
public:
    string countAndSay(int n) {
        string res = "1";
        for (int i = 1 ; i < n; i++) {
            res = getNext(res);
        }
        return res;
    }
    string getNext(string s) {
        string res;
        for (int i = 0; i < s.size(); i++) {
            int count = 1;
            while (i < s.size() - 1 && s[i+1] == s[i]) {
                count++;
                i++;
            }
            res += '0' + count;
            res += s[i];
        }
        return res;
    }
};
```

