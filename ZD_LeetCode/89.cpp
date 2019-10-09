class Solution {
	public:
		vector<int> grayCode(int n) {
			vector<int> result;
			const size_t size = 1 << n; // 2^n
			result.reserve(size);
			for (size_t i = 0; i < size; ++i)
				result.push_back(binary_to_gray(i));
			return result;
		}
	private:
		static unsigned int binary_to_gray(unsigned int n) {
			return n ^ (n >> 1);
		}
};
