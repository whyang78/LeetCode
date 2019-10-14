## 142 Linked List Cycle II（[环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)）

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

**示例 1：**

```
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
```

### 用一个表，来记录节点是否访问过，如果再一次访问某个节点，说明有环，返回这个节点，否则null。

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
    ListNode *detectCycle(ListNode *head) {
        ListNode *p = head;
        set<ListNode*> map;
        while (p != nullptr) {
            if (map.find(p) != map.end()) {
                return p;
            }
            else{
                map.insert(p);
                p = p->next;
            }
        }
        return NULL;
    }
};
```

### 设入环之前的链表长度为a， 环长为b，快慢指针相遇节点距离环入口处为y，此时慢指针走了a+n1\*b+y，快指针走了2(a+n1\*b+y)，快指针比慢指针应当多走环长的整数倍，因此2(a+n1\*b+y)-(a+n1\*b+y) = n2\*b，即，a=(n2-n1)\*b-y。此时另设一指针3从起点每次走一步，慢指针从相遇点继续也每次走一步，当指针3走a步到环入口时，满指针走了a=(n2-n1)\*b-y步也到达环入口，慢指针和指针3在环入口相遇了，返回该节点。

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
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                ListNode *slow2 = head;
                while (slow2 != slow) {
                    slow2 = slow2->next;
                    slow = slow->next;
                }
                return slow;
            }
        }
        return nullptr;
    }
};
```

