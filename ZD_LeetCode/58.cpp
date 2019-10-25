class Solution {
public:
    int lengthOfLastWord(string s) {
        reverse(s.begin(), s.end());
        s.erase(0, s.find_first_not_of(" "));
        int i = 0;
        for (;i < s.size() && s[i] != ' '; ++i);
        return i;
    }
};
