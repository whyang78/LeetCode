class Solution {
public:
    int threeSumClosest(vector<int>& A, int t) {
        if (A.size() < 3) return 0;
        int res = A[0] + A[1] + A[2];
        int dif = abs(res - t);
        sort(A.begin(), A.end());
        for (int i = 0; i < A.size() - 2; ++i) {
            int l = i + 1, r = A.size() - 1;
            while (l < r) {
                int new_res = A[i] + A[l] + A[r];
                int new_dif = abs(new_res - t);
                if (new_dif < dif) {
                    dif = new_dif;
                    res = new_res;
                }
                if (new_res < t) ++l;
                else --r;
            }
        }
        return res;
    }
}; 
