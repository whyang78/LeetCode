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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode R(-1);
        R.next = head;
        ListNode *p = &R, *q =  &R;
        for (int i = 0; i < n; ++i) 
            p = p->next;
        while(p->next) {
            p = p->next;
            q = q->next;
        }
        ListNode *t = q->next;
        q->next = t->next;
        delete t;
        return R.next;
    }
};
