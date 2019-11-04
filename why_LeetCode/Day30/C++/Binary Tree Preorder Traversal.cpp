//方法一：递归
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
       vector<int> result;
       traversal(root,result);
       return result;
    }
private:
    void traversal(TreeNode* root,vector<int>& result)
    {
        if(root==NULL)  return;
        result.push_back(root->val);

        traversal(root->left,result);
        traversal(root->right,result);
    }
};

//方法二：栈实现
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
       vector<int> result;
       stack<TreeNode *> node;
       if(root!=NULL) node.push(root);

       while(!node.empty())
       {
           TreeNode *temp=node.top();
           result.push_back(temp->val);
           node.pop();

            //栈：先进后出 故先右后左
           if(temp->right!=NULL) node.push(temp->right);
           if(temp->left!=NULL) node.push(temp->left);
       }    
       return result;
    }
};