/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// 时间复杂度 O(m+n) 空间复杂度O(1)
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(-1);//头结点
        ListNode* pre=&head;
        int c=0;
        for(ListNode *pa=l1,*pb=l2; pa!=NULL||pb!=NULL;
            pa=pa==NULL?NULL:pa->next,pb=pb==NULL?NULL:pb->next,pre=pre->next)
            {
                int a=pa==NULL?0:pa->val;
                int b=pb==NULL?0:pb->val;
                int val=(a+b+c)%10;
                c=(a+b+c)/10;

                pre->next=new ListNode(val);
            }
        if(c>0)
            pre->next=new ListNode(c);
        return head.next;
    }
};
