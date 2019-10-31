class Solution {
	public:
		vector<vector<int> > levelOrder(TreeNode *root) {
			vector<vector<int>> result;
			traverse(root, 1, result);
			return result;
		}
		void traverse(TreeNode *root, size_t level, vector<vector<int>> &result) {
			if (!root) return;
			if (level > result.size())
				result.push_back(vector<int>());
			result[level-1].push_back(root->val);
			traverse(root->left, level+1, result);
			traverse(root->right, level+1, result);
		}
};
