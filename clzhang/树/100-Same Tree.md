## 100 Same Tree（[相同的树](https://leetcode-cn.com/problems/same-Tree/)）

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 :

```
输入:      1          1
         /             \
        2               2
输出：false
```

#### 根节点相等，左右子树相等

```C++
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        return p->val == q->val
            && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

