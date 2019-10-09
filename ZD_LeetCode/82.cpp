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
        ListNode* T = new ListNode(-1);
        ListNode* R = T;
        T->next = head;
        while (T->next) {
            bool b = 0;
            while (T->next->next && T->next->val == T->next->next->val) {
                b = 1;
                ListNode* p = T->next;
                T->next = p->next;
                delete p;
            }
            if (b) {
                ListNode* p = T->next;
                T->next = p->next;
                delete p;
            } else {
                T = T->next;
            }
        }
        return R->next;
    }
};	
