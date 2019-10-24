## 647 Palindromic Substrings（[回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)）

> 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
>
> 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
>

**示例 1:**

```
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
```

**示例 2:**

```
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
```


注意:

1. 输入的字符串长度不会超过1000。


#### A

计算以每个元素为中心的回文子串的个数，并相加，注意奇数和偶数都要算。

```c++
class Solution {
public:
    int countSubstrings(string s) {
        int i = 0, res = 0;
        while (i < s.size()) {
            res += getNum(s, i, i);
            res += getNum(s, i, i + 1);
            i++;
        }
        return res;
    }
    int getNum(string &s, int left, int right) {
        int res = 0;
        while (left >= 0 && right < s.size()) {
            if (s[left] == s[right]) {
                res++;
                left--;
                right++;
            }
            else break;
        }
        return res;
        
    }
};
```

