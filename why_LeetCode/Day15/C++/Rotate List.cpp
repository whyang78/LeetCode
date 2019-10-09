//��ʱ k��Ե��
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL || k==0)
            return head;
        
        ListNode dummy(-1);
        dummy.next=head;

        ListNode *fast=&dummy,*slow=&dummy;
        for(int i=1;i<=k+1;i++)
        {
            fast=fast->next==NULL?head:fast->next;
        }

        while(fast)
        {
            slow=slow->next;
            fast=fast->next;
        }

        ListNode *cur=&dummy;
        while(slow->next)
        {
            ListNode *temp=slow->next;
            slow->next=slow->next->next;
            temp->next=cur->next;
            cur->next=temp;
            cur=temp; 
          
        }
        return dummy.next;
        
    }
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL || k==0)
            return head;
        
        int len=1;
        ListNode *p=head;
        while(p->next)
        {
            len++;
            p=p->next;
        }
        k=len-k%len;

        p->next=head; //��β����
        for(int i=0;i<k;i++)
        {
            p=p->next;
        }
        head=p->next; //�µ�ͷ���
        p->next=NULL; //�Ͽ���
        return head;       
    }
};