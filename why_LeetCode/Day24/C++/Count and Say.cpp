class Solution {
public:
    string countAndSay(int n) {
        string result="1";
        while(--n)
        {
            result=getnext(result);
        }
        return result;
    }
private:
    string getnext(string &s)
    {
        stringstream ss;
        for(auto i=s.begin();i!=s.end();)
        {
            auto j=find_if(i,s.end(),bind1st(not_equal_to<char>(),*i));
            ss<<distance(i,j)<<*i;
            i=j;
        }
        return ss.str();
    }
};