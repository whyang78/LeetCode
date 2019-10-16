class Solution {
public:
    int strStr(string h, string n) {
        int i = 0, j = 0;
        while (i < h.size() && j < n.size()) {
            if (h[i] == n[j]) {
                ++i;
                ++j;
            } else {
                i = i - j + 1;
                j = 0;
            }
        }
        if (j == n.size()) return i - j;
        else return -1;
    }
};
