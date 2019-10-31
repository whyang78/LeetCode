101 Symmetric Tree（[对称二叉树](https://leetcode-cn.com/problems/Symmetric-Tree/)）

> 给定一个二叉树，检查它是否是镜像对称的。
>

**例如，二叉树 [1,2,2,3,4,4,3] 是对称的。**

```
	1
   / \
  2   2
 / \ / \
3  4 4  3
```

**但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:**

```
	1
   / \
  2   2
   \   \
   3    3
```


说明:

- 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

> 树对称：
>
> 它的左右子树对称，也就是左右子树根结点相等，左子树的左子树与右子树的右子树对称，并且左子树的右子树与右子树的左子树对称。

- #### 递归：

```C++
class Solution {
public:
    bool Symmetric(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        return p->val == q->val
            && Symmetric(p->left, q->right) && Symmetric(p->right, q->left) ;
        
    }
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return Symmetric(root->left, root->right);
    }
};
```





