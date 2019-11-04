//方法一：递归
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {   
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
            traversal(root->right,result);
            result.push_back(root->val);
        }
    }
};

//方法二：栈
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode *> node;
        TreeNode *p=root,*q=NULL;

        do{
            while(p!=NULL)
            {
                node.push(p);
                p=p->left;
            }
            q=NULL;
            while (!node.empty())
            {
                p=node.top();
                node.pop();
                if(p->right==q)
                {
                    result.push_back(p->val);
                    q=p;
                }
                else
                {
                    node.push(p);
                    p=p->right;
                    break;
                }  
            }
        }while(!node.empty());
        return result;
    }
};