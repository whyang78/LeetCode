class Solution {
public:
    vector<int> twoSum(vector<int>& A, int t) {
        unordered_map<int, int> m;
        vector<int> res;
        for (int i = 0; i < A.size(); ++i) {
            m[A[i]] = i;
        }
        for (int i = 0; i < A.size(); ++i) {
            int v = t - A[i];
            if (m.find(v) != m.end() && m[v] > i) {
                res.push_back(i);
                res.push_back(m[v]);
            }
        }
        return res;
    }
};
