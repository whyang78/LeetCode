206 Reverse Linked List （[反转链表](https://leetcode-cn.com/problems/reverse-linked-List/)）

反转一个单链表。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

迭代法

![Image text](C:\Users\Administrator.PC-20190621JALE\Downloads\webwxgetmsgimg.jpg)

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
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *p2 = nullptr;
        ListNode *p1 = head;
        while(p1 != nullptr) {
            ListNode *cur = p1->next;
            p1->next = p2;
            p2 = p1;
            p1 = cur;
        }
        return p2;
    }
};
```

