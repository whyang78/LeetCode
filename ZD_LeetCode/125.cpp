class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        int n = s.size();
        int i = 0, j = n - 1;
        while (i < j) {
            if (!::isalnum(s[i])) {
                ++i;
            } else if (!::isalnum(s[j])) {
                --j;
            } else if (s[i] == s[j]) {
                ++i;
                --j;
            } else {
                return false;
            }
        }
        return true;
    }
};
