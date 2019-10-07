#### 92 Reverse Linked List II  （反转链表 II）

反转从位置 *m* 到 *n* 的链表。请使用一趟扫描完成反转。

**说明:**
1 ≤ *m* ≤ *n* ≤ 链表长度。

**示例:**

```
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
```

## Code

将需要翻转区域的数存下来，再反着赋值给原链表。时间$\mathcal{O}(n)$，空间：最坏$\mathcal{O}(n)$。

```C++
class Solution {
public:
	ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode *res = head;
        vector<int> tmp;
        for (int i = 0; i < m - 1; i++) {
            head = head->next;
        }
        ListNode *p = head;
        //将需要翻转的数存下来
        for (int i = m; i <= n; i++) {
            tmp.push_back(head->val);
            head = head->next;
        }
        //逆序更新
        for (int i = m; i <= n; i++) {
            p->val = tmp[n - i];
            p = p->next;
        }
        return res;
	}
};
```

