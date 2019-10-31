## 99 Recover Binary Search Tree（[恢复二叉搜索树](https://leetcode-cn.com/problems/Recover-Binary-Search-Tree/)）

> 二叉搜索树中的两个节点被错误地交换。
>
> 请在不改变其结构的情况下，恢复这棵树。
>

**示例 1:**

```
输入: [1,3,null,null,2]
   1
  /
 3
  \
   2

输出: [3,1,null,null,2]
   3
  /
 1
  \
   2
```

### 中序遍历，寻找乱序的两个位置，交换。空间复杂度

$$
\mathcal{O}(n)
$$



```C++
class Solution {
public:
    vector<TreeNode*> node;
    void inOrder(TreeNode* root) {
        if (root) {
            inOrder(root->left);
            node.push_back(root);
            inOrder(root->right);
        }
    }
    void recoverTree(TreeNode* root) {
        inOrder(root);
        int i = 0;
        for (; i < node.size() - 1; i++) {
            if (node[i + 1]->val < node[i]->val) break;
        }
        int j = node.size() - 1;
        for (; j >= 0; j--) {
            if (node[j - 1]->val > node[j]->val) break;
        }
        swap(node[i]->val, node[j]->val);
    }
};
```

