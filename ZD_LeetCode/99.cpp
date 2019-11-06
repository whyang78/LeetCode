class Solution {
	public:
		void recoverTree(TreeNode* root) {
			pair<TreeNode*, TreeNode*> broken;
			TreeNode* prev = nullptr;
			TreeNode* cur = root;
			while (cur != nullptr) {
				if (cur->left == nullptr) {
					detect(broken, prev, cur);
					prev = cur;
					cur = cur->right;
				} else {
					auto node = cur->left;
					while (node->right != nullptr && node->right != cur)
						node = node->right;
					if (node->right == nullptr) {
						node->right = cur;

						cur = cur->left;
					} else {
						detect(broken, prev, cur);
						node->right = nullptr;
						prev = cur;
						cur = cur->right;
					}
				}
			}
			swap(broken.first->val, broken.second->val);
		}
		void detect(pair<TreeNode*, TreeNode*>& broken, TreeNode* prev,
		            TreeNode* current) {
			if (prev != nullptr && prev->val > current->val) {
				if (broken.first == nullptr) {
					broken.first = prev;
				}

				broken.second = current;
			}
		}
};
