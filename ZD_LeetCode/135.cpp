class Solution {
public:
    int candy(vector<int>& childern) {
        int n = childern.size();
        vector<int> A(n, 1);
        for (int i = 0; i < n - 1; ++i) {
            if (childern[i + 1] > childern[i])
                A[i + 1] = A[i] + 1;
        }
        for (int i = n - 1; i > 0; --i) {
            if (childern[i - 1] > childern[i])
                A[i - 1] = max(A[i] + 1, A[i - 1]);
        }
        int res = 0;
        for (int i: A) res += i;
        return res;
    }
}; 
