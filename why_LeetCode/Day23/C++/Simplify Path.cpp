class Solution {
public:
    string simplifyPath(string path) {
        vector<string> st;

        for(auto i=path.begin();i!=path.end();)
        {
            i++;
            auto j=find(i,path.end(),'/');
            auto dir=string(i,j);
            if(!dir.empty()&&dir!=".")
            {
                if(dir=="..")
                {
                    if(!st.empty())
                    {
                        st.pop_back();
                    }
                }
                else
                {
                    st.push_back(dir);
                }
            }
            i=j;
        }

        stringstream ss;
        if(st.empty())
        {
            ss<<"/";
        }
        else
        {
            for(auto s : st)
            {
                ss<<'/'<<s;
            }
        }
        return ss.str();   
    }
};