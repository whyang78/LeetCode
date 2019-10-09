#### 2 Add Two Numbers （两数相加）

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例：**

```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

## Code

```C++
	//list中两数相加
	ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
		ListNode dummy(-1);	//空节点
		ListNode *res = &dummy;	//指向空节点
		ListNode *pa = l1, *pb = l2;
		int flag = 0;
		while (pa != nullptr || pb != nullptr) {
			int a = (pa == nullptr ? 0 : pa->val);
			int b = (pb == nullptr ? 0 : pb->val);
			int value = a + b + flag;
			flag = value / 10;
			value %= 10;
			res->next = new ListNode(value);
			res = res->next;
			pa = (pa == nullptr ? nullptr : pa->next);
			pb = (pb == nullptr ? nullptr : pb->next);
		}
		if (flag) res->next = new ListNode(flag);
		return dummy.next;
	}
```

