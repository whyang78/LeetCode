## 109 Convert Sorted List to Binary Search Tree（[有序链表转换二叉搜索树](https://leetcode-cn.com/problems/Convert-Sorted-list-to-Binary-Search-Tree/)）

```
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
```

**示例:**

```
给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

#### 与上一题数组转换二叉搜索树类似，只不过每次找中点时，遍历链表。

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return nullptr;
        if (!head->next) {
            TreeNode *res = new TreeNode(head->val);
            return res;
        }
        ListNode *left = head;
        ListNode *right = head;
        ListNode *left_pre = nullptr;

    
        while (right && right->next) {
            left_pre = left;
            left = left->next;
            right = right->next->next;
        }
        right = left->next;
        left_pre->next = nullptr;	//保证left_pre !=nullptr
        
        TreeNode *res = new TreeNode(left->val);
        TreeNode *LeftTree = sortedListToBST(head);
        TreeNode *RightTree = sortedListToBST(right);
        res->left = LeftTree;
        res->right = RightTree;
        return res;
    }
};
```

