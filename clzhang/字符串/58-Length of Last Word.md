## 58 （[最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)）

给定一个仅包含大小写字母和空格 `' '` 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

**说明：**一个单词是指由字母组成，但不包含任何空格的字符串。

**示例:**

```
输入: "Hello World"
输出: 5
```

#### A

先去除末尾连续的空格，再从最后一个字符往前找，直到出现空格停止，返回单词长度。

```C++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = s.size();
        int i = len - 1, res = 0;
        while (i >= 0 && s[i] == ' ') i--;
        while (i >= 0 && s[i] != ' ') {
            res++;
            i--;
        }
        return res;
    }
};
```

