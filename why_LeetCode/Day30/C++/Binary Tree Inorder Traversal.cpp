//方法一：递归
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        traversal(root,result);
        return result;
    }
private:
    void traversal(TreeNode* root,vector<int>& result)
    {
        if(root!=NULL)
        {
            traversal(root->left,result);
            result.push_back(root->val);
            traversal(root->right,result);
        }
    }
};

//方法二：栈
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode *> node;
        TreeNode *temp=root;

        while(!node.empty()||temp!=NULL)
        {
            if(temp!=NULL)
            {
                node.push(temp);
                temp=temp->left;
            }
            else
            {
                temp=node.top();
                node.pop();
                result.push_back(temp->val);
                temp=temp->right;
            }
        }
        return result;
    }
};
