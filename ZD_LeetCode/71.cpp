class Solution {
public:
    string simplifyPath(string str) {
        stack<char> s;
        for (size_t i = 0; i < str.size(); ++i) {
            if (str[i] == '/') {
                if (!s.empty() && s.top() == '/')
                    continue;
                else 
                    s.push(str[i]);
            } else if (str[i] == '.') {
                if (i + 1 < str.size() && str[i + 1] == '.') {
                    s.pop();
                    while (!s.empty() && s.top() != '/') {
                        s.pop();
                    }
                    ++i;
                } else {
                    continue;
                }
            } else {
                s.push(str[i]);
            }
        }
       
        string res;
        if (!s.empty() && s.top() == '/') s.pop();
        while (!s.empty()) {
            res += s.top();
            s.pop();
        }
        if (res != "")
            reverse(res.begin(), res.end());
        else
            res = "/";
       
        return res;
    }
};
