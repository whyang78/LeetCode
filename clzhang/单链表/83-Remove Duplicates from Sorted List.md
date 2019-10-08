## 83 Remove Duplicates from Sorted List（[删除排序链表中的重复元素](https://leetcode-cn.com/problems/Remove-Duplicates-from-Sorted-List/)）

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

**示例 1:**

```
输入: 1->1->2
输出: 1->2
```


**示例 2:**

```
输入: 1->1->2->3->3
输出: 1->2->3
```

有序的，直接遍历，看下一个节点的值，与当前节点值是否相同，相同就删掉下一个节点，指向下下一个，继续判断。

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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return head;
		
		ListNode *res = head;
		ListNode *dummy = res;
		ListNode *head1 = res->next;

		while (head1 != nullptr) {
			int value = res->val;
			if (value != head1->val) {
				res->next = head1;
				res = res->next;
			}
			head1 = head1->next;
		}
		res->next = nullptr;
		return dummy;
    }
};
```

