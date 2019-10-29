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

## 144. Binary Tree Preorder Traversal

![1572005410205](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1572005410205.png)

**解题思路：**

使用递归的方法：理解二叉树的前序遍历

使用非递归的方法：后面在补充

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorderTraversal(root, res);
        return res;
    }
    
    void preorderTraversal(TreeNode* root,  vector<int>& res)
    {
        if (!root) return;
        
        res.push_back(root->val);
        preorderTraversal(root->left, res);
        preorderTraversal(root->right, res);
    }
};
```

## 94. Binary Tree Inorder Traversal

![1572005701992](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1572005701992.png)

**解题思路：**

使用递归的方法：理解二叉树的中序遍历

使用非递归的方法：后面在补充

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorderTraversal(root, res);
        return res;
    }
    void inorderTraversal(TreeNode* root, vector<int>& res)
    {
        if (!root) return;
        inorderTraversal(root->left, res);
        res.push_back(root->val);
        inorderTraversal(root->right, res);
    }
    
};
```

## 145. Binary Tree Posterorder Traversal

![1572005957601](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1572005957601.png)

**解题思路：**

使用递归的方法：理解二叉树的后序遍历

使用非递归的方法：后面在补充

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorderTraversal(root, res);
        return res;
    }
    
    void postorderTraversal(TreeNode* root, vector<int>& res)
    {
        if (!root) return; 
        postorderTraversal(root->left, res);
        postorderTraversal(root->right, res);
        res.push_back(root->val);
    }
};
```

## 102. Binary Tree Level Order Traversal

![image-20191028155644966](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191028155644966.png)

解题思路：

这题是二叉树的层次遍历，其实有两种方法都可以实现二叉树的层次遍历，BFS（广度优先搜索）， DFS(深度优先搜索), 使用深度优先搜索是一种递归的写法，代码看起来更加的简洁。

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // BFS 
        if (!root) return {};
        vector<vector<int>> ans;
        // curr 和 next 分别表示的是当前遍历的这一层，和下一次将要遍历的层 
        vector<TreeNode*> curr, next;
        curr.push_back(root);
        while(!curr.empty())
        {
            // 动态的增加一行
            ans.push_back({});
            for(TreeNode* node : curr)
            {
                // 每次都是最后一行添加元素
                ans.back().push_back(node->val);
                // 每次添加完一个元素之后都判断其左边和右边是否还有元素，有的话，先添加左边在添加右边
                if (node->left) next.push_back(node->left);
                if (node->right) next.push_back(node->right);
            }
            swap(curr, next);
            next.clear();
        }
        
        return ans;
    }
};
```

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // DFS
        vector<vector<int>> ans;
        levelOrder(root, 0, ans);
        
        return ans;
    }
    
    void levelOrder(TreeNode* root, int depth, vector<vector<int>>& ans)
    {
        if (!root) return;
        while(ans.size() <= depth) ans.push_back({});
        ans[depth].push_back(root->val);
        levelOrder(root->left, depth + 1, ans);
        levelOrder(root->right, depth + 1, ans);
    }
};
```

## 112. Path Sum

![image-20191029161328941](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191029161328941.png)

**解题思路：**

这道题是求解一个从根节点到叶子节点的某一条路径上的所有节点的和加起来为某个数。可以使用递归的方法，每次在访问了一个节点之后将sum减去这个节点的值作为新的sum，然后分别递归左子树和右子树。当且仅当访问的叶子节点（左右子树都为空）时sum的值等于当前节点的值说明存在一个path满足题意。

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
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root) return false;
        if(!root->left && !root->right) return root->val == sum;
        int new_sum = sum - root->val;
        
        return hasPathSum(root->left, new_sum) || hasPathSum(root->right, new_sum);
    }
};
```

## 226. Invert Binary Tree

![image-20191029162225212](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191029162225212.png)

解题思路：

逆转二叉树，从题意可以看出就是将二叉树的左右子树进行反转。只需要使用递归的方法将左右子节点分别进行逆转就可以。

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
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return 0;
        swap(root->left, root->right);
        invertTree(root->left), invertTree(root->right);
        return root;
    }
};
```

