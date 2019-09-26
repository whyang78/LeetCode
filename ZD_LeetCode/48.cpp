class Solution {
public:
    void rotate(vector<vector<int>>& A) {
        int n = A.size();
        for (int i = 0; i < n / 2; ++i)
            for (int j = 0; j < n; ++j)
                swap(A[i][j], A[n - 1 - i][j]);
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                swap(A[i][j], A[j][i]);
    }
};
