//交换指针
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL) return head;

        ListNode dummy(-1);
        dummy.next=head;
        
        for(ListNode *pre=&dummy,*cur=pre->next;cur && cur->next;cur=pre->next)
        {
            ListNode *temp=cur->next;
            pre->next=temp;
            cur->next=temp->next;
            temp->next=cur;
            
            pre=pre->next->next;
        }

        return dummy.next;

    }
};

//交换值
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL) return head;

        ListNode *p=head;
        while(p&&p->next)
        {
            swap(p->val,p->next->val);
            p=p->next->next;
        }
        return head;

    }
};