class Solution {
public:
    bool isValid(string s) {
        string left="({[";
        string right=")}]";
        stack<char> st;

        for(auto c:s)
        {
            if(left.find(c)!=string::npos)
            {
                st.push(c);
            }
            else
            {   if(st.empty()||st.top()!=left[right.find(c)])
                {
                    return false;
                }
                else
                {
                    st.pop();
                }
            }
        }
        return st.empty();
    }
};