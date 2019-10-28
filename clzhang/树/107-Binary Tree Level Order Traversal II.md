107  Binary Tree Level Order Traversal II（[二叉树的层次遍历 II](https://leetcode-cn.com/problems/Binary-Tree-Level-Order-Traversal-ii/)）

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

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

#### 上一道题的结果翻转

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<int> map;
        TreeNode* node = root;
        Order(root, 1);
        reverse(res.begin(), res.end());
        return res;
    } 
};
```

