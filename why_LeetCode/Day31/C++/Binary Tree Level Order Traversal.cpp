//方法一：递归
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        traverse(root,1,result);
        return result;
    }
private:
    void traverse(TreeNode *root, size_t level, vector<vector<int>> &result) {
        if (!root) return;
        if (level > result.size())
        result.push_back(vector<int>());
        result[level-1].push_back(root->val);
        traverse(root->left, level+1, result);
        traverse(root->right, level+1, result);
}
};

//方法二：迭代
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode*> q;
        if(root==NULL) return result;
        q.push(root);

        TreeNode *p;
        while(!q.empty())
        {
            vector<int> temp;
            int width=q.size();
            for(int i=0;i<width;i++)
            {
                p=q.front();
                q.pop();
                temp.push_back(p->val);
                if(p->left!=NULL) q.push(p->left);
                if(p->right!=NULL) q.push(p->right);
            }
            result.push_back(temp);
        }
        return result;
    }
};