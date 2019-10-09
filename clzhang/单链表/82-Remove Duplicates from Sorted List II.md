82 Remove Duplicates from Sorted List II （[删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/Remove-Duplicates-from-Sorted-List-II/)）

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 *没有重复出现* 的数字。

**示例 1:**

```
输入: 1->2->3->3->4->4->5
输出: 1->2->5
```

**示例 2:**

```
输入: 1->1->1->2->3
输出: 2->3
```

连续往后判断两个数，不相等，则第一个数只出现一次，将第一个数记录下来，这样，继续判断下下一个和下下下一个；若后面两个相等，再看后面第三个，第四个...，直到找到不相等地数，指针往后移动至相等的最后一个数，继续下一次判断，后面两个数。。。

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
	ListNode *deleteDuplicates(ListNode *head) {
		if (head == nullptr || head->next == nullptr) return head;
		ListNode* preHead = new ListNode(0);
		preHead->next = head;
		ListNode dummy(-1);
		ListNode *res = &dummy;
		while (preHead->next != nullptr) {
			if (preHead->next->next == nullptr) {
				res->next = preHead->next;
				res = res->next;
				break;
			}
			else if (preHead->next->val == preHead->next->next->val) {
				int value = preHead->next->val;
				preHead = preHead->next->next;
				while (preHead->next != nullptr && preHead->next->val == value) {
					preHead = preHead->next;
				}
			}
			else {
				res->next = preHead->next;
				res = res->next;
				preHead = preHead->next;
			}
		}
		res->next = nullptr;
		return dummy.next;
	}
};


// class Solution {
// public:
// ListNode* deleteDuplicates(ListNode* head) {
//         ListNode* preHead = new ListNode(0);
//         preHead->next = head;

//         ListNode* cur = preHead;
//         int delVal;
//         while(cur->next != NULL){
//             if (cur->next->next != NULL && cur->next->val == cur->next->next->val) {
//                 delVal = cur->next->val;
//                 while(cur->next != NULL && cur->next->val == delVal){
//                     ListNode* delNode = cur->next;
//                     cur->next = delNode->next;
//                     delete delNode;
//                 }
//             } else {
//                 cur = cur->next;
//             }
//         }
//         ListNode* newHead = preHead->next;
//         delete preHead;
//         return newHead;
//     }

// };
```

