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



