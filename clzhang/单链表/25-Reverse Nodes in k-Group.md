## 25 Reverse Nodes in k-Group（[K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)）

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

**说明 :**

```
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
```



### 指针往后移，若链表长度不够k个，return head。否则先将前k个反转， 再将k+1及其之后的递归。

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1) return head;
        int count = 1;
        ListNode *pre = head;
        ListNode *tail = head;
        while (tail && count < k) {
            tail = tail->next;
            count++;
        }
        if (tail == NULL) return head;
        ListNode *next = tail->next;
        tail->next = NULL;
        ListNode *res = reverseList(pre);
        if (next != nullptr) pre->next = reverseKGroup(next, k);
        return res;
    }
    ListNode *reverseList(ListNode *node) {
        ListNode *p2 = node, *p3 = nullptr;
        
        while(p2 != nullptr) {
            if (p2->next == nullptr) {
                p2->next = p3;
                return p2;
            }
            ListNode *cur = p2->next;
            p2->next = p3;
            p3 = p2;
            p2 = cur;
        }
        return p2;
    }
};
```

