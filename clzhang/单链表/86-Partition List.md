## 86  Partition List（[分隔链表](https://leetcode-cn.com/problems/Partition-List/)）

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

**示例:**

```
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
```

## 两个空节点，分别将小于x和大于等于x的节点连起来，最后将这两个再串起来。

## Code

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
    ListNode* partition(ListNode* head, int x) {
        ListNode dummy1(-1), dummy2(-1);
        ListNode *lo = &dummy1, *hi = &dummy2;
        while (head != nullptr) {
            if (head->val < x) {
                lo->next = head;
                lo = lo->next;
            }
            else {
                hi->next = head;
                hi = hi->next;
            }
            head = head->next;
        }
        lo->next = dummy2.next;
        hi->next = nullptr;
        return dummy1.next;
    }
};
```

