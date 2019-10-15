## 143 Reorder List（[重排链表](https://leetcode-cn.com/problems/reorder-list/)）

给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

**示例 1:**

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
**示例 2:**

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

- ### 1

> 将后半段反转，插入到前半段之间（奇数时，前半段比后半段长1）

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
    void reorderList(ListNode* head) {
        if(head==NULL || head->next == NULL)
            return;
        //快慢指针分出两段
        ListNode *slow = head,*fast = head;
        while(fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        //后端反转
        ListNode *needReverser = slow->next;
        slow->next = NULL;
        needReverser = reverse(needReverser);

        while (needReverser != nullptr) {
            
            ListNode* cur = head->next;
            ListNode* cur2 = needReverser;
            needReverser = needReverser->next;
            head->next = cur2;
            head = head->next;
            head->next = cur;
            head = head->next;
            // needReverser = needReverser->next;
        }
        
    }
private:
    ListNode *reverse(ListNode *head){

        ListNode *p1 = nullptr;
        ListNode *p2 = head;
        ListNode *p3 = p2;
        
        while(p2){
            p3 = p2->next;
            p2->next = p1;
            p1 = p2;
            p2 = p3;            
        }
        
        return p1;
    }

    
};
```

- ### 递归

> L1->LN->剩下的递归；终止条件为长度小于等于2，返回。

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
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;
        ListNode *res = head;
        ListNode *tail = head->next;
        
        ListNode *p1 = head;
        while (p1->next->next) {
            p1 = p1->next;
        }
        res->next = p1->next;
        p1->next = nullptr;
        res = res->next;
        res->next = tail;
        
        reorderList(tail);
        
    }
};
```

