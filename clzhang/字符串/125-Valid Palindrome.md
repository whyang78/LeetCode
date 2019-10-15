## 125 Valid Palindrome（[验证回文串](https://leetcode-cn.com/problems/Valid-Palindrome/)）

> 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
>
> 说明：本题中，我们将空字符串定义为有效的回文串。
>

**示例 1:**

```
输入: "A man, a plan, a canal: Panama"
输出: true
```

**示例 2:**

```
输入: "race a car"
输出: false
```

双指针p1头部，p2尾部，判断p1，p2所指字符是否相等，不相等，返回false。相等的话p1右移1个，p2左移一个，继续判断。p1逐渐右移，p2左移。p1>=p2时停止

判断过程中，若某个指针指向的字符无效（逗号，句号等，不是字母或数字），忽略掉该字符，将该指针移至下一个字符。不区分大小写，toupper比较。

```C++
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while(left < right) {
            while (left < right && !(isdigit(s[left]) || isalpha(s[left]))) left++;
            while (left < right && !(isdigit(s[right]) || isalpha(s[right]))) right--;
            if (toupper(s[left]) != toupper(s[right])) return false;
            left++;
            right--;
        }
        return true;
    }
};
```

