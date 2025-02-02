class Solution {
	public:
		void connect(TreeLinkNode *root) {
			if (root == nullptr) return;
			TreeLinkNode dummy(-1);
			for (TreeLinkNode *curr = root, *prev = &dummy;
			        curr; curr = curr->next) {
				if (curr->left != nullptr) {
					prev->next = curr->left;
					prev = prev->next;
				}
				if (curr->right != nullptr) {
					prev->next = curr->right;
					prev = prev->next;
				}
			}
			connect(dummy.next);
		}
};
