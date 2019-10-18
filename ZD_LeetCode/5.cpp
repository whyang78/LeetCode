class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, length = 1;
        for (int i = 0; i < s.size(); ++i) {
            for (int j = i + 1; j < s.size(); ++j) {
                int l, r;
                for (l = i, r = j; l < r; ++l, --r) {
                    if (s[l] != s[r]) break;
                }
                if (l >= r && j - i + 1 > length) {
                    start = i;
                    length = j - i + 1;
                }
            }
        }
        return s.substr(start, length);
    }
};
