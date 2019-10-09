class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode leftdummy(-1);
        ListNode rightdummy(-1);

        ListNode *left=&leftdummy;
        ListNode *right=&rightdummy;
        for(ListNode *p=head;p;p=p->next)
        {
            if(p->val<x)
            {
                left->next=p;
                left=p;
            }
            else
            {
                right->next=p;
                right=p;
            }
        }
        left->next=rightdummy.next;
        right->next=NULL;

        return leftdummy.next;
    }
};