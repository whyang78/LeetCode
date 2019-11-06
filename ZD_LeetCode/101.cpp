/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* r) {
        if (!r) return true;
        stack<TreeNode*> s;
        s.push(r->left);
        s.push(r->right);
        while (!s.empty()) {
            TreeNode* p = s.top(); s.pop();
            TreeNode* q = s.top(); s.pop();
            
            if (!p && !q) continue;
            if (!p || !q) return false;
            if (p->val != q->val) return false;
            s.push(p->left);
            s.push(q->right);
            s.push(q->left);
            s.push(p->right);
        }
        return true;
    }
};
