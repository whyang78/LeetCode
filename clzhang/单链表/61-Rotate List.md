61 Rotate List（[旋转链表](https://leetcode-cn.com/problems/Rotate-List/)）

给定一个链表，旋转链表，将链表每个节点向右移动 *k* 个位置，其中 *k* 是非负数。

**示例 1:**

```
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
```

**示例 2:**

```
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
```

### 可以得到，是将末尾的k个节点移动至链表开始位置。

### 先遍历一遍得到链表长度，并将链表首尾相连，再把原来的倒数第k个和k+1个节点断开即可。

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
	ListNode *rotateRight(ListNode *head, int k) {
		ListNode *p = head;
		if (p == nullptr) return p;
		int length = 1;
		while (p->next != nullptr) {
			length++;
			p = p->next;
		}
		p->next = head;
		k %= length;	//K可能大于length
		for (int i = 0; i < length - k; i++) {
			p = p->next;
		}
        ListNode *res = p->next;
		p->next = nullptr;
		return res;
	}
};
```







