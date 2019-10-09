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
        if (!head) return 0;
        for (ListNode *p = head, *q = head->next; q; q = p->next) {
            if (p->val == q->val) {
                p->next = q->next;
                delete q;
            } else {
                p = q;
            }
        }
        return head;
    }
};
