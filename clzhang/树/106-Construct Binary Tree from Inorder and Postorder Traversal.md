## 106 Construct Binary Tree from Inorder and Postorder Traversal（[从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/Construct-Binary-Tree-from-inorder-and-postorder-Traversal/)）

根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

```
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
```


返回如下的二叉树：

```
	3
   / \
  9  20
    /  \
   15   7
```

#### 递归法；postorder最后一个元素为根节点，再分离出left和right对应的inorder和postorder。

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
    
    TreeNode* helper(vector<int>& inorder, int b1, int e1, vector<int>& postorder, int b2, int e2) {
        if (b2 > e2) return nullptr;
        if (b2 == e2) return new TreeNode(postorder[e2]);
        TreeNode* root = new TreeNode(postorder[e2]);
        int m = 0;
        while (b1 + m <= e1) {
            if (inorder[b1 + m] == postorder[e2]) break;
            m++;
        }
        root->left = helper(inorder, b1, b1 + m - 1, postorder, b2, b2 + m - 1);
        root->right = helper(inorder, b1 + m + 1, e1, postorder, b2 + m, e2 - 1);
        return root;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (postorder.empty()) return nullptr;
        return helper(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }
};
```

