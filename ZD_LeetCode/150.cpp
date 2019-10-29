class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        int res = tokens.size() == 0 ? 0 : atoi(tokens[0].c_str());
        for (int i = 0; i < tokens.size(); ++i) {
            if (tokens[i] == "+") {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                res = b + a;
                s.push(res);
            } else if (tokens[i] == "-") {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                res = b - a;
                s.push(res); 
            } else if (tokens[i] == "*") {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                res = b * a;
                s.push(res);
            } else if (tokens[i] == "/") {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                res = b / a;
                s.push(res);
            } else {
                int a = atoi(tokens[i].c_str());
                s.push(a);
            }
        }
        return res;
    }
};
