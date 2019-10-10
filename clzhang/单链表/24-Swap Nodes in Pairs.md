24 Swap Nodes in Pairs （[ 两两交换链表中的节点](https://leetcode-cn.com/problems/Swap-Nodes-in-Pairs/)）

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



**示例:**

```
给定 1->2->3->4, 你应该返回 2->1->4->3.
```

- ## 迭代法

先将1,2节点交换，再交换3,4，一直交换下去。。。

### Code

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
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(-1);
        ListNode *res = &dummy;
        res->next = head;
        while(head != nullptr && head->next != nullptr) {
            ListNode* tmp = head->next->next;
            res->next = head->next;
            res = res->next;
            res->next = head;
            res = res->next;
            res->next = tmp;
            head = tmp;
        }
        return dummy.next;
    }
};
```

- ## 递归法

交换前两个，然后将剩下的串作为参数，递归调用这个函数，终止条件为当链表长度小于等于1时返回链表本身。

### Code

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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *tail = head->next->next;
        ListNode dummy(-1);
        ListNode *res = &dummy;
        res->next = head->next;
        res = res->next;
        res->next = head;
        res = res->next;
        res->next = (tail) ? swapPairs(tail) : nullptr;
        return dummy.next;
    }
};
```







