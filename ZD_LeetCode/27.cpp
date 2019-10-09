class Solution {
public:
    int removeElement(vector<int>& A, int v) {
        int j = -1;
        for (int i = 0; i < A.size(); ++i) {
            if (A[i] != v) A[++j] = A[i];
        }
        return j + 1;
    }
};
