#### 95 Unique Binary Search Trees II（[不同的二叉搜索树 II](https://leetcode-cn.com/problems/Unique-Binary-Search-Trees-ii/)）

```
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
```

**示例:**

```
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

#### 与上一题类似，以小于等于n的每个元素为根节点，再算left和right两两组合成一个树。

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
public:
    vector<TreeNode*> generateTrees(int n) {
        if(n == 0) {
            vector<TreeNode*> res;
            return res; 
        }
        return helper(1, n);
    }
private:
    vector<TreeNode*> helper(int start,int end){
        vector<TreeNode*> res;
        if (start > end) {
            res.push_back(nullptr);
            return res;
        }
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> left = helper(start, i - 1);
            vector<TreeNode*> right = helper(i + 1, end);
            for (auto l : left) {
                for (auto r : right) {
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};
```

