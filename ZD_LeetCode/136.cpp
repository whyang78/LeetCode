class Solution {
public:
    int singleNumber(vector<int>& A) {
        int res = 0;
        for (int i: A) 
            res ^= i;
        return res;
    }
};
