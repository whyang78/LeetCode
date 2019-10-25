//方法一：纵向扫描
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())
            return "";
        
        for(int i=0;i<strs[0].size();i++)
        {
            for(int j=1;j<strs.size();j++)
            {
                if(strs[0][i]!=strs[j][i])
                {
                    return strs[0].substr(0,i);
                }
            }
        }
        return strs[0];
    }
};

//方法二：横向扫描
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())
            return "";
            
        int rightmost=strs[0].size()-1;
        for(int i=1;i<strs.size();i++)
        {
            for(int j=0;j<=rightmost;j++)
            {
                if(strs[i][j]!=strs[0][j])
                {
                    rightmost=j-1;
                }
            }
        }
        return strs[0].substr(0,rightmost+1);
    }
};