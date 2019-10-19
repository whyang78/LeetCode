## 20. Valid Parentheses

![1571148634174](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571148634174.png)

解题思路：

括号匹配是典型的stack的应用，所以直接使用一个stack来完成即可，不过这里为了简化代码使用了一个unordered_map.

```cpp
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> mp;
        mp[']'] = '[', mp[')'] = '(', mp['}'] = '{';
        
        stack<char> st;
        for (int i = 0; i < s.size(); i++)
        {
            if (!mp[s[i]]) st.push(s[i]);
            else
            {
                if (st.empty() || st.top() != mp[s[i]]) return false;
                st.pop();
            }
        }
        
        return st.empty();
    }
};
```



## 14. Longest Connon Prefix

![1571149182567](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571149182567.png)

解题思路：

这道题求解最长的前缀，可以用暴力的方法，把第一个字符串当做是目标，让其他的所有字符串的每一个字符都与第一个字符串的每一个进行比较

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string ans;
        
        for (int i = 0; i < strs[0].size(); i++)
        {
            for (auto s : strs)
            {
                if (s[i] != strs[0][i]) return ans;       
            }
            ans += strs[0][i];
        }
            
        return ans;
    }
};
```

## 28. Implement strStr()

![1571150087695](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571150087695.png)

解题思路：

1. 目前还没有学习KMP的做法，直接使用暴力的做法。遍历字符串中的每一个字符进行一一匹配。

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        const int n1 = haystack.size(), n2 = needle.size();
        if (n2 == 0) return 0;
        
        for (int i = 0; i < n1 - n2 + 1; i++)
        {
            if (haystack[i] == needle[0])
            {
                bool check = true;
                for (int j = 0; j < n2; j++)
                {
                    if (haystack[i + j] != needle[j]) check = false;
                }
                if (check) return i;                
            }
        }
        return -1;
    }
};
```



## 344. Reverse String

![1571235818870](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571235818870.png)

解题思路：

倒转字符串和倒转数组是一样的，但是和倒链表由很大的不同（由于链表的性质）

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        const int n = s.size();
        int l = 0, r = n - 1;
        while(l <= r)
        {
            swap(s[l], s[r]);
            l++, r--;
        }
    }
};
```

## 13. Roman to Integer

![1571236468335](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571236468335.png)

解题思路 ：

观察罗马数字的组合，如果前一个小于后一个，说明使用这两个数表示后一个减去前一个的值，如果前一个数大于后一个数就是正常的，将他们代表的数字进行相加。但是为了计算方便使用了一个map来对罗马数字到整数的转换。

```cpp
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mp;
        mp['I'] = 1, mp['V'] = 5, mp['X'] = 10;
        mp['L'] = 50, mp['C'] = 100, mp['D'] = 500, mp['M'] = 1000;
        
        const int n = s.size();
        int ans = 0;
        for(int i = 0; i < n; i++)
        {
            if(i < n - 1 && mp[s[i]] < mp[s[i + 1]])
            {
                ans += mp[s[i + 1]] - mp[s[i]];
                i++;
            }
            else ans += mp[s[i]];
        }
        
        return ans;
    }
};
```



## 67. Add Binary

![1571302413160](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571302413160.png)

解题思路：

这道题和两个列表求和是一个思路：每次的和都是两个链表中分别哪一个元素出来，加上进位。如果某个链表没有元素了，那么就用0代替。这里只不过是输入的是字符串，有一个技巧就是字符串减去‘0’就从字符串变成了整数值。

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0, i = a.size() - 1, j = b.size() - 1;
        string ans;
        while(i >= 0 || j >= 0)
        {
            int sum = (i >= 0 ? a[i--] - '0' : 0) + 
                      (j >= 0 ? b[j--] - '0' : 0) + carry;
            carry = sum >> 1;
            ans += '0' + (sum % 2);
        }
        
        if(carry) ans += '1';
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

```

## 5. Longest Palindromic Substring

![1571304405603](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571304405603.png)

解题思路：

暴力的方法，遍历每一个字符，让其作为中心，然后往前和往后进行匹配，但是需要注意回文子串是奇数和偶数的情况。

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        string ans;
        int len = 0;
        for (int i = 0; i < s.size(); i++)
        {
            
            for (int j = 0; i - j >= 0 && i + j < s.size(); j++)
            {
                if (s[i - j] == s[i + j])
                {
                    if (j * 2 + 1 > len)
                    {
                        len = j * 2 + 1;
                        ans = s.substr(i - j, j * 2 + 1);
                    }
                }
                else break;
            }
            
            
            for (int j = i, k = i + 1; j >= 0 && k < s.size(); j--, k++)
            {
                if (s[j] == s[k])
                {
                    if (k - j + 1 > len)
                    {
                        len = k - j + 1;
                        ans = s.substr(j, k - j + 1);
                    }
                }
                else break;
            }
        }
        
        return ans;
    }
};
```

## 58. Length of Last word

![1571304927078](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571304927078.png)

解题思路：

因为是找最后一个单词的长度，所有可以直接从后面开始往前面找，但是需要注意的是，可能最后面又空格，所以在计算最后一个单词的长度之前需要把空格去掉

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int ans = 0, i = s.size() - 1;
        while(i >= 0 && s[i] == ' ') i--;
        while(i >= 0 && s[i] != ' ')
        {
            ans++; i--;
        }
        return ans;
    }
};
```

## 3. Longest Substring Without Repeating Characters

![23231571496496297](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571496496297.png)

解题思路

hash table与滑动窗口

定义两个指针i, j,表示的是这两个指针扫描到的区间是s[i, j],在维护一个hash table来记录每一个字符出现的次数，如果s[j]>1则让i往后面移动，直到s[i]<=1此时在计算ans=max(ans, j - i + 1)

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_map<char, int> hash;
        
        for (int i = 0, j = 0; j < s.size(); j++)
        {
            hash[s[i]] ++;
            while(hash[s[i]] > 1) hash[s[i++]] --;
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
```

