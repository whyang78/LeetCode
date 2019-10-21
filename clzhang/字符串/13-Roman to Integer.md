## 13 Roman to Integer（[罗马数字转整数](https://leetcode-cn.com/problems/ROMAN-to-INTEGER/)）

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

> 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
>

**示例 1:**

```
输入: "III"
输出: 3
```


**示例 2:**

```
输入: "IV"
输出: 4
```


**示例 3:**

```
输入: "IX"
输出: 9
```


**示例 4:**

```
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```


**示例 5:**

```
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

> 从高位到低位逐个判断，当前位对应的数值若比前一位大，说明这一位与前一位组合在一起，值为当前位减去上一位，上一位的数值已经累加过了，所以应该加上当前位减去2*上一位的值。
>
> 否则该位与上一位无关，直接加上来。

```C++
class Solution {
public:
    int map (char s) {
        switch (s) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    int romanToInt(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i > 0 && map(s[i]) > map(s[i  -1])) res += map(s[i]) - 2 * map(s[i - 1]);
            else res += map(s[i]);
        }
        return res;
    }
};
```

