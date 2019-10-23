//方法一:分别排序，然后比对两个字符串
//时间复杂度：O(NlogN) 空间复杂度：O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        return s==t;
    }
};

//方法二:使用哈希表 分别统计两个字符串的各个字符出现的次数 进行对比
//时间复杂度：O(N) 空间复杂度：O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
       if(s.size()!=t.size())
            return false;

       unordered_map<char,int> map;
       for(int i=0;i<s.size();i++)
       {
            ++map[s[i]];
            --map[t[i]];
       }

       for(auto m:map)
       {
           if(m.second!=0)
            return false;
       }
       return true;
    }
};