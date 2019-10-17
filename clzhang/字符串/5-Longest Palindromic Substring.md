## 5 Longest Palindromic Substring（[最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/) ）

> 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
>

**示例 1：**

```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```

**示例 2：**

```
输入: "cbbd"
输出: "bb"
```

> 思路：
>
> 计算以每个元素为中心的最长回文子串 复杂度n，这样包含了所有的可能，并且判断以某个元素为中心的最长回文子串的复杂度最多为n/2，但是要分奇数和偶数，因此总的复杂度最多为

$$
\mathcal{O}(n^2)
$$

- ### 判断某个位置元素为中心的最长回文子串，返回长度

```C++
int isPalindrome(string &s, int mid, int mid2) {
	//返回以mid，mid2为中心（mid==mid2时，以mid==mid2为中心）的最长回文子串的长度
	int left = mid2 - 1,right = mid + 1;
	while(left >= 0 && right < s.size()) {
		if (s[left] != s[right]) return right - left - 1;
		left--;
		right++;
	}
	return right - left - 1;
}
```

- ### 循环计算分别以n个元素为中心的最长回文子串

```C++
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() <= 1) return s;
        int start = 0;//记录回文子串起始位置
        int end = 0;//记录回文子串终止位置
        for (int i = 0; i < s.size(); i++) {
            int len1 = isPalindrome(s, i, i + 1);	//计算偶数长度
            int len2 = isPalindrome(s, i, i);		//计算奇数长度
            int mlen = max(len1,len2);
            if (mlen > end - start + 1) {
                start = i - (mlen - 1)/2;
                end = i + mlen/2;
            }
        }
        return s.substr(start, end - start + 1);
        
    }
    int isPalindrome(string &s, int mid, int mid2) {
        //返回以mid，mid2为中心（mid==mid2时，以mid==mid2为中心）的最长回文子串的长度
        int left = mid2 - 1,right = mid + 1;
        while(left >= 0 && right < s.size()) {
            if (s[left] != s[right]) return right - left - 1;
            left--;
            right++;
        }
        return right - left - 1;
    }
};
```



















