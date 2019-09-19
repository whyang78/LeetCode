class Solution {
public:
    int removeDuplicates(vector<int>& A) {
        for (int i = 1; i < A.size(); ++i) {
            int flag = 1;
            if (A[i] == A[i - 1]) {
                while (i + 1 < A.size() && A[i] == A[i + 1]) {
                    A.earse(A[i + 1]);
                }
            }
        }
    }
}; 
