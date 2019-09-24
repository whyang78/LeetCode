class Solution {
public:
    string getPermutation(int n, int k) {
        string s;
        int c = 1;
        vector<int> A;
        for (int i = 0; i < n; ++i) {
            A.push_back(i + 1);
        }
        do {
            if (c == k) break;
            ++c;
        } while(next_permutation(A.begin(), A.end()));
        for (int i = 0; i < n; ++i) {
            char tmp = A[i] + '0';
            s += tmp;
        }
        return s;
    }
};
