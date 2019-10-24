# Tree

## 100. Same Tree

![1571892088074](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571892088074.png)

解题思路：

判断两棵树是不是相同的，需要满足的是树的每一个节点以及节点上的值都相等，主要需要注意一下特殊情况，关于树的题都是使用递归来做的，这道题的递归出口是，只要有一个树上的节点为空，就比较另一个节点是不是也为空，如果是的话，说明是相同的，否则直接返回false。在递归的过程中，由于先判断了两个节点非空，所以接下来需要判断两个节点的上的值是否相等，如果相等的话继续递归的判读这两课数的左右子树是否也相同。

```cpp
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p || !q) return !p && !q;
        else return p->val == q->val && isSameTree(p->left, q->left)
                    && isSameTree(p->right, q->right);
    }
};
```

## 101. Symmetric Tree

![1571892500833](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571892500833.png)

解题思路：

首先需要理解对称树的概念，与100题判断是否是一颗相同的树一样的思路，只不过在判断完两个节点非空之后，需要判断的是第一棵树的做孩子应该等于右边的孩子节点（上面那道题就是左边还等于左边，右边还等于右边）

```cpp
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
    bool isSymmetric(TreeNode* root) {
        return check(root, root);
    }
    bool check(TreeNode* p, TreeNode* q)
    {
        if (!p || !q) return !p && !q;
        else return p->val == q->val && check(p->left, q->right) && check(p->right, q->left);
    }
};
```

## 104. Maximum Depth of Binary Tree

![1571893001322](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571893001322.png)

解题思路：

求解树的最大深度，使用递归的思想就是求的最大深度的子树的深度加1 ，就是整个树的最大深度。

```cpp
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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        else return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};
```

