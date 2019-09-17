class Solution {
public:
    bool search(vector<int>& A, int t) {
        int l = 0, r = A.size();
        while (l != r) {
            const int m = l + (r - l) / 2;
            if (A[m] == t)
                return true;
            if (A[l] < A[m]) {
                if (A[l] <= t && t < A[m])
                    r = m;
                else
                l = m + 1;
            } else if (A[l] > A[m]) {
                if (A[m] < t && t <= A[r-1])
                    l = m + 1;
                else
                    r = m;
            } else
                l++;
        }
        return false;
    }
};
