class Solution {
public:
    int myAtoi(string s) {
        int n = s.length();
        int num = 0;
        int i = 0;
        int sign = 1;
        
        while (s[i] == ' ' && i < n) ++i;
        
        if (s[i] == '+') {
            ++i;
        } else if (s[i] == '-') {
            ++i;
            sign = -1;
        }   
        
        while (i < n) {
            if (s[i] < '0' || s[i] > '9') break;
            if (num > INT_MAX / 10 || (num == INT_MAX / 10 && (s[i] - '0') > INT_MAX % 10))
                return sign == -1 ? INT_MIN : INT_MAX;
            num = num * 10 + (s[i] - '0');
            ++i;
        }
        return num * sign;
    }
};
