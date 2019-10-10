## 19 Remove Nth Node From End of List （[删除链表的倒数第N个节点](https://leetcode-cn.com/problems/Remove-Nth-Node-From-End-of-List/)）

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

**示例：**

```
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
```

## 快指针比慢指针快N个，当快指针指向最后一个节点时，慢指针的下一个节点为倒数N个节点，将慢指针的next指向next->next即可。

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
	ListNode *removeNthFromEnd(ListNode *head, int n) {
		if (head == nullptr) return head;
		ListNode dummy(-1);
        dummy.next = head;
		ListNode *left = &dummy, *right = &dummy;
		for (int i = 0; i < n; i++) {
			right = right->next;
            // cout << right->val;
		}
		while (right->next != nullptr) {
			left = left->next;
			right = right->next;
            // cout << 2;
		}
		left->next = left->next->next;
		return dummy.next;
	}
};
```

