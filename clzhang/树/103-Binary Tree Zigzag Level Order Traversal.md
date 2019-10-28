## 103 Binary Tree Zigzag Level Order Traversal（[二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/Binary-Tree-Zigzag-Level-Order-Traversal/)）

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```

返回锯齿形层次遍历如下：

> [ [3],
>   [20,9],
>   [15,7]]

#### 将层次遍历的结果，从第二层开始，每隔一层翻转

```c++
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<int> map;
        TreeNode* node = root;
        Order(root, 1);
        for (int i = 1; i < res.size(); i+=2) {
            reverse(res[i].begin(), res[i].end());
        }
        return res;
    }
};
```

