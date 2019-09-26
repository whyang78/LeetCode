class Solution {
	public:
		vector<int> plusOne(vector<int>& A) {
			int n = A.size();
			for (int i = n - 1; i >= 0; --i) {
				A[i] = A[i] + 1;
				int r = A[i] / 10;
				if (r == 0) break;
				else {
					A[i] = 0;
				}
			}
			return A;
		}
};
