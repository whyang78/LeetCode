150 Evaluate Reverse Polish Notation（[逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)）

根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

- 整数除法只保留整数部分。

- 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况

**示例 1：**

```
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
```


**示例 2：**

```
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
```

A

维护一个栈，遍历给定的vector，如果是+-*/运算符，则弹出栈顶两个元素进行运算，运算完之后压入栈；如果是数字则直接入栈，判断下一个。

```C++
class Solution {
public:
    stack<int> s;
    int toInt(string &s) {
        int res = 0, i = 1;
        int flag = 1;
        if (s[0] == '-') flag = -1;
        else res = s[0] - '0';
        
        while (i < s.size()) {
            int t = s[i] - '0';
            res = res * 10 + t;
            i++;
        }
        return flag * res;
        // stringstream ss(s);
        // int a;
        // ss >> a;
        // return a;
    }
    int evalRPN(vector<string>& tokens) {
        if (tokens.empty()) return 0;
        int i = 0, len = tokens.size();
        int x, y;
        while (i < len) {
            if (tokens[i] == "+") {
                y = s.top();
                s.pop();
                x = s.top();
                s.pop();
                s.push(x + y);
            }
            else if (tokens[i] == "-") {
                y = s.top();
                s.pop();
                x = s.top();
                s.pop();
                s.push(x - y);
            }
            else if (tokens[i] == "*") {
                y = s.top();
                s.pop();
                x = s.top();
                s.pop();
                s.push(x * y);
            }
            else if (tokens[i] == "/") {
                y = s.top();
                s.pop();
                x = s.top();
                s.pop();
                s.push(x / y);
            }
            else s.push(toInt(tokens[i]));
            i++;
        }
        return s.top();

    }
};
```

