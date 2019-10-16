## 8 String to Integer (atoi)（[字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)）

> 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
>
> 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
>
> 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
>
> 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
>
> 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
>
> 在任何情况下，若函数不能进行有效的转换时，请返回 0。
>

说明：

> 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
>

**示例 1:**

```
输入: "42"
输出: 42
```

**示例 2:**

```
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
```

- ### 库函数，一顿骚操作。

```C++
class Solution {
public:
    int myAtoi(string str) {
        int digit = 0;
        istringstream str1(str);
        str1 >> digit;
        return digit;
    }
};
```

- ### 自己写。

#### 1 找数值起始位置；2 往后找连续的数字，直到出现非数字停止。

1.删除开头连续的空格，res = 0

2.第一个位置只能时数字或 + - 号，不是就返回0，是数字或+-号，就从此处开始计算。

​	（1）第一个位置是数字，继续往后加，直到出现不是数字为止。

​	（2）第一个是+-号，记录符号位flag。判断，若后一位不是数字，返回0，结束，后一位是数字往后判断，直到出现非数字位，注意往后连续判断时，判断是否溢出，也就是判断，若加上该位数字是否溢出。

溢出判断条件：

​	正数flag=1：当前res < INT_MAX/10，该位数字一定是小于等于9，加上不会溢出；

​				res > INT_MAX/10时，说明一定溢出，return；

​				res == INT_MAX/10时，该位数字若大于INT_MAX%10，会溢出；否则不会。



​	负数flag=-1：当前res > INT_MIN/10，该位数字一定是小于等于9，减去它不会溢出；

​				res < INT_MAX/10时，说明一定溢出，return；

​				res == INT_MAX/10时，该位数字若大于INT_MIN%10，会溢出；否则不会。

    //溢出返回条件
    t = str[i] - '0';//即将加上来的数字
    
    //正
    if (res > INT_MAX / 10 || res == INT_MAX / 10 && t > (INT_MAX%10)) return INT_MAX;
    
    //负
    if (res < INT_MIN / 10 || res == INT_MIN / 10 && t > (INT_MIN%10)) return INT_MIN;
    
    //否则将t添加上来
    res = res * 10 + flag * t;
```C++
class Solution {
public:
    int myAtoi(string str) {
        int digit = 0, len = str.size(), i = 0;
        while (i < len && str[i] == ' ') i++;   //排除开头的空格
        if (i == len) return 0;

        int num = 0, flag = 1;
        int res = 0;
        int max_res;
        
        if (str[i] == '-') {
            flag = -1;
        }
        else if (isdigit(str[i])) {
            res = str[i] - '0';
        }
        else if (str[i] != '+') return 0;
        
        while (++i < len && isdigit(str[i])) {
            int t = str[i] - '0';
            // 如果结果大于INT_MAX，返回INT_MAX
            if (res > INT_MAX / 10 || res == INT_MAX / 10 && t > 7) return INT_MAX;
            // 如果结果小于INT_MIN，返回INT_MIN
            if (res < INT_MIN / 10 || res == INT_MIN / 10 && t > 8) return INT_MIN;
            res = res * 10 + flag * t;
        }

        return res;

    }
};

// class Solution {
// public:
//     int myAtoi(string str) {
//         int digit = 0;
//         istringstream str1(str);
//         str1 >> digit;
//         return digit;
//     }
// };
```











