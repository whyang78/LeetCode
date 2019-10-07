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
    ListNode* addTwoNumbers(ListNode* a, ListNode* b) {
        long i = 1, j = 1;
        int a_num = a->val, b_num = b->val;
        while (a->next || b->next) {
            if (a->next) {
                i *= 10;
                a = a->next;
                a_num += i * a->val;
            }
            if (b->next) {
                j *= 10;
                b = b->next;
                b_num += j * b->val;
            }  
        }
        int c = a_num + b_num;
        ListNode* p = new ListNode(-1);
        ListNode* q = p;
        while (c) {
            int t = c % 10;
            c = c / 10;
            p->next = new ListNode(t);  //β�巨
            p = p->next;
        }
        if (!q->next)
            q->next = new ListNode(0);
        return q->next;
    }
};
