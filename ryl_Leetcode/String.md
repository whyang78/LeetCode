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

