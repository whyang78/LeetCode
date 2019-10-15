//�ҵ��м�ڵ㣬�Ͽ����Ѻ��ص�����reverseһ�£��ٺϲ�����������
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
        pre->next=NULL;//�ֳ�ǰ��������
        slow=reverse(slow);//��벿�ַ�ת

        //�ϲ�������
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
