## 144 94 145 二叉树遍历

> 给定一个二叉树，返回它的 前序 中序 后序 遍历。

## 递归法

### 前序

```C++
class Solution {
public:
    vector<int> res;
    void preorder(TreeNode* root) {
        if (root) {
            res.push_back(root->val);
            preorder(root->left);
            preorder(root->right);
        }
    } 
    vector<int> preorderTraversal(TreeNode* root) {
        preorder(root);
        return res;
    }    
       
};
```

### 中序

```C++
class Solution {
public:
    
    vector<int> res;
    void inorder(TreeNode* root) {
        if (root) {
            inorder(root->left);
            res.push_back(root->val);
            inorder(root->right);
        }
    } 
    vector<int> inorderTraversal(TreeNode* root) {
        inorder(root);
        return res;
    }    
    
};
```

### 后序

```C++
class Solution {
public:
    
    vector<int> res;
    void inorder(TreeNode* root) {
        if (root) {
            inorder(root->left);
            res.push_back(root->val);
            inorder(root->right);
        }
    } 
    vector<int> inorderTraversal(TreeNode* root) {
        inorder(root);
        return res;
    }    
    
};
```

