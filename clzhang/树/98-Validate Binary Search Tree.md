## 98 Validate Binary Search Tree（[验证二叉搜索树](https://leetcode-cn.com/problems/Validate-Binary-Search-Tree/)）

```
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
```


**示例 1:**

```
输入:
    2
   / \
  1   3
输出: true
```


**示例 2:**

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

#### 中序遍历为有序的，判断是否出现乱序位置。

```C++
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
private:
    vector<int> map;
    void inOrder(TreeNode* root) {
        if (!root) return;
        inOrder(root->left);
        map.push_back(root->val);
        inOrder(root->right);
    }
public:
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        inOrder(root);
        for (int i = 0; i < map.size() - 1; i++) {
            if (map[i + 1] <= map[i]) return false;
        }
        return true;
    }
};
```



