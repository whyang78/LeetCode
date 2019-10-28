//方法一：使用栈
//时间复杂度：O(N) 空间复杂度：O(N)
class Solution {
public:
    int longestValidParentheses(string s) {
        int max_len=0,last=-1;
        stack<int> st;

        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                st.push(i);
            }
            else
            {
                if(st.empty())
                {
                    last=i;
                }
                else
                {
                    st.pop();
                    if(st.empty())
                    {
                        max_len=max(max_len,i-last);
                    }
                    else
                    {
                        max_len=max(max_len,i-st.top());
                    }
                }   
            }     
        }
        return max_len;
    }
};

//方法二：两边扫描
//时间复杂度：O(N) 空间复杂度：O(1)
class Solution {
public:
    int longestValidParentheses(string s) {
        int max_len=0;

        int depth=0,start=-1;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                depth++;
            }
            else
            {
                depth--;
                if(depth<0)
                {
                    start=i;
                    depth=0;
                }
                else if(depth==0)
                {
                    max_len=max(max_len,i-start);
                }
            }
        }

        depth=0;
        start=s.size();
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]==')')
            {
                depth++;
            }
            else
            {
                depth--;
                if(depth<0)
                {
                    start=i;
                    depth=0;
                }
                else if(depth==0)
                {
                    max_len=max(max_len,start-i);
                }
            }
        }
        return max_len;
    }
};