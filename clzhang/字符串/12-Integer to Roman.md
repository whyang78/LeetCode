12 Integer to Roman（[整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)）

> 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
>

| 字符 | 数值 |
| ---- | ---- |
| I    | 1    |
| V    | 5    |
| X    | 10   |
| L    | 50   |
| C    | 100  |
| D    | 500  |
| M    | 1000 |

> 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
>
> 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
>

- I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
- X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
- C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

> 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

**示例 1:**

```
输入: 3
输出: "III"
```


**示例 2:**

```
输入: 4
输出: "IV"
```


**示例 3:**

```
输入: 9
输出: "IX"
```


**示例 4:**

```
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
```


**示例 5:**

```
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

### 定义一个map，包含所有基数（1,4,5,9,10,40,50,90,100,400,900,1000）

### 输入的num和最大基数比较，如果num更大，则字串加上基数对应的值，num减去该基数，直至num更小，此时和下一个基数比较，重复第二步

```C++
class Solution {
public:
    string intToRoman(int num) {
        int radix[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4 , 1};
        string symbol[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string roman;
        for (size_t i = 0; num > 0; ++i) {
            int count = num / radix[i];
            num %= radix[i];
            for (; count > 0; --count) roman += symbol[i];
        }
        return roman;
    }
};
```

> Down一个方法，写起来很简洁。

范围1~3999

1. 从最大基数1000开始看，有num / 1000个1000，范围1~3999最多有3个1000，定义string M[] = {"", "M", "MM", "MMM"}，表示1000,2000,3000
2. 继续算后面的剩下的数num%1000，在1~999之间，最多9个100。有(num%1000)/100个100，定义string C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}。表示一个100为C，2个100为CC，3个100为CCC......表示100,200,300，......900
3. 看剩下的数，有(num % 100) / 10个10，同样，定义string X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};表示10,20,30，......90
4. 剩余的数在1~9之间，定义string I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};表示1~9

将这些全部加起来。

代码：

```C++
class Solution {
public:
    string intToRoman(int num) {
        string M[] = {"", "M", "MM", "MMM"};
        string C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
    }
};
```

