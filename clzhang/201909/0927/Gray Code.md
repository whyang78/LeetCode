## Question: Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of
gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2 

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

## A

由n位推导n+1位结果时，n+1位结果包含n位结果，同时包含n位结果中在高位再增加一个位1所形成的令一半结果，但是这一半结果需要与前一半结果镜像排排列。

```C++
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result(1);
        result[0] = 0;
        for(int i = 1; i <= n; i++){
            int e = 1 << (i - 1);                           //i - 1位结果前增加一位1
            for(int j = result.size() - 1; j >= 0; j--){    // 镜像排列
                result.push_back(e + result[j]);
            }
        }
        return result;
    }
};
```

