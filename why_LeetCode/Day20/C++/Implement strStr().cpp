//暴力求解法一
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty())
            return 0;

        const int m=haystack.size(),n=needle.size();
        for(int i=0;i<=m-n;i++)
        { 
            int j=0;
            for(int x=i; j<n && x<m && haystack[x]==needle[j] ;j++,x++);

            if(j==n)
                return i;          
        }
        return -1;      
    }
};

//暴力求解法二
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty())
            return 0;

        const int m=haystack.size(),n=needle.size();
        for(int i=0;i<=m-n;i++)
        { 
            if(haystack.substr(i,n)==needle)
                return i;          
        }
        return -1;      
    }
};

//find内置方法
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty())
            return 0;

        int pos=haystack.find(needle);
        return pos;      
    }
};