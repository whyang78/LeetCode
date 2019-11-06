## 108  Convert Sorted Array to Binary Search Tree（[将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/Convert-Sorted-Array-to-Binary-Search-Tree/)）

```
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
```

**示例:**

```
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

#### 递归

#### 以数组中心值为根节点，左侧的数来构造左子树，右侧的数来构造右子树。

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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        return sortedArrayToBSTHelper(nums, 0, nums.size() -1);
        
    }
private:
    TreeNode* sortedArrayToBSTHelper(vector<int>& nums, int left, int right) {
        if (left > right) return nullptr;
        if (left - right == 0) {
            TreeNode *res = new TreeNode(nums[left]);
            return res;
        }
        int mid = left + (right - left)/2;
        TreeNode *res = new TreeNode(nums[mid]);
        res->left = sortedArrayToBSTHelper(nums, left, mid - 1);
        res->right = sortedArrayToBSTHelper(nums, mid + 1, right);
        return res;
    }
};
```

