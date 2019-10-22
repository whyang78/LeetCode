## 65 Valid Number（[有效数字](https://leetcode-cn.com/problems/Valid-Number/)）

> 验证给定的字符串是否可以解释为十进制数字。
>
> 例如:
>
> "0" => true
> " 0.1 " => true
> "abc" => false
> "1 a" => false
> "2e10" => true
> " -90e3   " => true
> " 1e" => false
> "e3" => false
> " 6e-1" => true
> " 99e2.5 " => false
> "53.5e93" => true
> " --6 " => false
> "-+3" => false
> "95a54e53" => false
>
> 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
>
> 数字 0-9
> 指数 - "e"
> 正/负号 - "+"/"-"
> 小数点 - "."
> 当然，在输入中，这些字符的上下文也很重要。

## 1

首先去除开头的空格。

2

判断e之前是否有效，先取第一位，是数字，有效，表示e之前有数字；若是 . ，有效；若是+-，也有效；其余无效，返回false

第二位往后，某一位有效的条件：数字+-.e，其实只能为数字，e，和小数点.

该位是数字，有效； 

```
(s[i] >= '0' && s[i] <= '9')
//数字，有效，设为has_front_num = true; 
```

//该位是+-号，无效，因为第一位有效已经是数字或是+-或是.，此后不能有+-，也就是+-只能出现在首位；

该位是.，小数点.不能在前面出现过，小数点 . 只能出现一次；

```
!has_e && !has_dot && s[i] == '.'
//若.有效，则设为has_dot = true;
```

该位是e，之前必须是有效的数字；

```
has_front_num && !has_e && s[i] == 'e'
//若该位是有效的e，将has_e = true;同时break;判断e之后是否有效
```

```C++
        while (i < s.size() && ((s[i] >= '0' && s[i] <= '9') || 
                (has_front_num && !has_e && s[i] == 'e') ||
                (!has_e && !has_dot && s[i] == '.'))) {
            if (s[i] == 'e') {//若是有效的e，将has_e = true;
                has_e = true;
                ++i;
                break;
            } else if (s[i] == '.') {
                has_dot = true;
            } else {
                has_front_num = true; 
            }
            ++i;
        }
```

此时，若has_e有效，则判断e之后的数是否有效：

e之后只能为纯数字，或是+-号加上数字。

```C++
class Solution {
public:
    bool isNumber(string s) {
        bool has_dot = false;
        bool has_e = false;
        bool has_front_num = false;
        int i = 0;
        // skip front space
        while (s[i] == ' ') ++i;
        // check first char
        if (s[i] == '.') {
            has_dot = true;
        } else if (s[i] >= '0' && s[i] <= '9') {
            has_front_num = true;
        } else if (s[i] != '+' && s[i] != '-') {
            return false;
        }
        ++i;
        // check char before 'e'
        while (i < s.size() && ((s[i] >= '0' && s[i] <= '9') || 
                (has_front_num && !has_e && s[i] == 'e') ||
                (!has_e && !has_dot && s[i] == '.'))) {
            if (s[i] == 'e') {
                has_e = true;
                ++i;
                break;
            } else if (s[i] == '.') {
                has_dot = true;
            } else {
                has_front_num = true; 
            }
            ++i;
        }
        // check after 'e'
        if (has_e) {
            if (i >= s.size())
                return false;
            bool has_tail_num = false;
            if (s[i] >= '0' && s[i] <= '9') {
                has_tail_num = true;
            } else if (s[i] != '-' && s[i] != '+') {
                return false;
            }
            ++i;
            while (i < s.size() && s[i] >= '0' && s[i] <= '9') {
                has_tail_num = true;
                ++i;
            }
            if (!has_tail_num)
                return false;
        }
        // skip tail space
        while (i < s.size() && s[i] == ' ') ++i;
        // final result
        return has_front_num && i >= s.size();
    }
};
```

