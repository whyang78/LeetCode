//找到中间节点，断开，把后半截单链表reverse一下，再合并两个单链表。
class Solution {
public:
    void reorderList(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return ;
        
        ListNode *pre,*slow=head,*fast=head;
        while(fast && fast->next)
        {
            pre=slow;
            slow=slow->next;
            fast=fast->next->next;
        }
        pre->next=NULL;//分成前后两部分
        slow=reverse(slow);//后半部分反转

        //合并两部分
        ListNode *p=head;
        while(p->next)
        {
            ListNode  *temp=p->next;
            p->next=slow;
            slow=slow->next;
            p->next->next=temp;
            p=temp;
        }
        p->next=slow;
    }
private:
    ListNode* reverse(ListNode* head)
    {
        if(head==NULL || head->next==NULL)
            return head;

        ListNode *pre=head;
        for(ListNode *cur=head->next,*next=cur->next;
            cur;
            pre=cur,cur=next,next=next?next->next:NULL)
            {
                cur->next=pre;
            }
        head->next=NULL;
        return pre;
    }
};
