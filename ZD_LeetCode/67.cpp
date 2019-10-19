class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        int n = a.length() > b.length() ? a.length() : b.length();
        int carry = 0;
        string res;
        for (int i = 0; i < n; ++i) {
            int x = i < a.length() ? a[i] - '0' : 0;
            int y = i < b.length() ? b[i] - '0' : 0;
            res += (x + y + carry) % 2 + '0';
            carry = (x + y + carry) / 2;
        }
        if (carry != 0) res += '1';
        reverse(res.begin(), res.end());
        return res;
    }
};
