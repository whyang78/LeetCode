class Solution {
public:
    bool isValid(string s) {
        if (s.length() == 1) return 0;
        if (s == "") return 1;
        stack<char> ss;
        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                ss.push(s[i]);
            } else {
                if (ss.empty()) 
                    return false;
                if (s[i] == ')' && ss.top() == '(' || s[i] == ']' && ss.top() == '[' || s[i] == '}' && ss.top() == '{') {
                    ss.pop();
                    continue;
                }
                else 
                    return false;
            }
        }
        if (!ss.empty()) return 0;
        return true;
    }
};
