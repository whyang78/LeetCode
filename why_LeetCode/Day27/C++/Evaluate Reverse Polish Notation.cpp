class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> st;
        for(auto token : tokens)
        {
            if(!isoperator(token))
            {
                st.push(token);
            }
            else
            {
                int x=stoi(st.top());
                st.pop();
                int y=stoi(st.top());
                st.pop();
                if(token[0]=='+')   y+=x;
                else if(token[0]=='-') y-=x;
                else if(token[0]=='*') y*=x;
                else    y/=x;
                st.push(to_string(y));
            }
        }
        return stoi(st.top());
    }
private:
    bool isoperator(string &s)
    {
        return s.size()==1 && string("+-*/").find(s)!=string::npos;
    }
};