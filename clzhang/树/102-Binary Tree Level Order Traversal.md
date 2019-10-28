## 102 Binary Tree Level Order Traversal（[二叉树的层次遍历](https://leetcode-cn.com/problems/Binary-Tree-Level-Order-Traversal/)）

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```


返回其层次遍历结果：

> [ [3],
>   [9,20],
>   [15,7]]

#### 层次遍历时，多一个变量，指定所在的层，这样就元素插入到对应的层中去。

```C++
class Solution {
public:
    vector<vector<int>> res;
    void Order(TreeNode* root, int i) {
        if (root) {
            if (res.size() < i) {
                vector<int> map;
                map.push_back(root->val);
                res.push_back(map); 
            }
            else {
                res[i-1].push_back(root->val);
            }
            if (root->left) {
                Order(root->left, i + 1);
            }
            if (root->right) {
                Order(root->right, i + 1);
            }
        }
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<int> map;
        TreeNode* node = root;
        Order(root, 1);
        return res;
    }    
};
```

