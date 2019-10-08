//方法一：另存一个链表
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) return head;

        ListNode dummy(-1);
        ListNode *result=&dummy;
        int temp=head->val+1; //只要与起始值不一样就可以
        for(ListNode *p=head;p;p=p->next)
        {
            if(p->val!=temp)
            {
                result->next=p;
                result=p;
                temp=p->val;
            }                
        }
        result->next=NULL;
        return dummy.next;
    }
};

//方法二：双指针法 在原链表上迭代运算
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) return head;

        for(ListNode *pre=head,*cur=head->next;cur;cur=pre->next)
        {
            if(pre->val==cur->val)
            {
                pre->next=cur->next;
                delete cur;
            }
            else
            {
                pre=cur;
            }
        }
        return head;
    }
};