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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode R(-1);
        R.next = head;
        ListNode *p = &R, *q = p->next, *z = q->next;
        while (z) {
            p->next = z;
            q->next = z->next;  
            z->next = q;
            p = q;
            q = q->next;
            z = q == 0 ? 0 : q->next;   
        }
        return R.next;
    }
};
