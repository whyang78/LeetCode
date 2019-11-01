## 105 Construct Binary Tree from Preorder and Inorder Traversal（[从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/Construct-Binary-Tree-from-preorder-and-inorder-Traversal/)）

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```


返回如下的二叉树：

```
	3
   / \
  9  20
    /  \
   15   7
```

#### 递归法；inorder最后一个元素为根节点，再分离出left和right对应的preorder和inorder。

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode 
 *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* helper(vector<int>& preorder, int b1, int e1, vector<int>& inorder, int b2, int e2) {
        if (b1 > e1) return nullptr;
        if (b1 == e1) return new TreeNode(preorder[b1]);
        TreeNode* root = new TreeNode(preorder[b1]);
        int m = 0;
        while (b2 + m <= e2) {
            if (inorder[b2 + m] == preorder[b1]) break;
            m++;
        }
        root->left = helper(preorder, b1 + 1, b1 + m, inorder, b2, b2 + m - 1);
        root->right = helper(preorder, b1 + m + 1, e1, inorder, b2 + m + 1, e2);
        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty()) return nullptr;
        return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
};
```

