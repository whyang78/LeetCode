class Solution {
public:
    int removeDuplicates(vector<int>& A) {
        return unique(A.begin(), A.end()) - A.begin();
    }
};
