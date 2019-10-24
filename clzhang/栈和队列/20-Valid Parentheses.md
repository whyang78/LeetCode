## 20 Valid Parentheses（[有效的括号](https://leetcode-cn.com/problems/Valid-Parentheses/)）

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

**示例 1:**

```
输入: "()"
输出: true
```


**示例 2:**

```
输入: "()[]{}"
输出: true
```


**示例 3:**

```
输入: "(]"
输出: false
```

**示例 4:**

```
输入: "([)]"
输出: false
```


**示例 5:**

```
输入: "{[]}"
输出: true
```

> 判断
>
> 1. 前括号，压入。
> 2. 后括号，判断是否可以pop和是否有匹配的前括号

```C++
class Solution {
public:
    bool isValid(string s) {
    if (s.empty()) return true;
    if (s.length() %2 != 0) return false;
    stack<char> ss;
    for(auto i:s) {
        if (i=='{' || i=='('|| i=='[') ss.push(i);
        else {
            if (ss.size() == 0 && (i == ']' || i == '}' || i == ')')) return false;
            else if ((i == '}' && ss.top() != '{') || (i == ']' && ss.top() != '[') || (i == ')' && ss.top() != '(') )
                return false;
            else
                ss.pop();
        }
    }
    if (ss.size() != 0 ) return false; 
    return true;
    }
};
```

