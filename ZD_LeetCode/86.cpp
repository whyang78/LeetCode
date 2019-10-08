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
    ListNode* partition(ListNode* head, int x) {
        ListNode* R = new ListNode(-1);
        ListNode* L = new ListNode(-1);
        ListNode* res = R;
        ListNode* tmp = L;
        for (ListNode* p = head; p; p = p->next) {
            if (p->val < x) {
                R->next = new ListNode(p->val);
                R = R->next;
            }
            else {
                L->next = new ListNode(p->val);
                L = L->next;
            }
        }
        R->next = tmp->next;
        return res->next; 
    }
};
