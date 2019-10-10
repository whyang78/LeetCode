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
        ListNode* R = new ListNode(-1);
        ListNode* T = R;
        int carry = 0;
        while (a || b) {
            int ai = a == 0 ? 0 : a->val;
            int bi = b == 0 ? 0 : b->val;
            int val = (ai + bi + carry) % 10;
            carry = (ai + bi + carry) / 10;
            a = a == 0 ? 0 : a->next;
            b = b == 0 ? 0 : b->next;
            T->next = new ListNode(val);
            T = T->next;
        }
        if (carry > 0)
            T->next = new ListNode(carry);
        return R->next;
    }
};
