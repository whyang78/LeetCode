//方法一：递归
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head==NULL ||  head->next==NULL || k<2)
            return head;
        
        ListNode *end=head;
        for(int i=0;i<k;i++)
        {
            if(end==NULL)
                return head;
            end=end->next;//最终指向k+1个
        }

        ListNode *new_end=reverseKGroup(end,k);
        ListNode *cur=head,*pre=new_end;
        while(cur!=end)
        {
            ListNode *temp=cur->next;
            cur->next=pre;
            pre=cur;
            cur=temp;
        }
        return pre;
    }
};

//方法二：迭代
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head==NULL ||  head->next==NULL || k<2)
            return head;
        
        ListNode dummy(-1);
        dummy.next=head;
        for(ListNode *pre=&dummy,*end=head;end;end=pre->next)
        {
            for(int i=1;i<k && end;i++)
            {
                end=end->next;
            }
            if(end==NULL)
            {
                break;
            }
            pre=reverse(pre,pre->next,end);
        }
        return dummy.next;
    }

private:
    ListNode *reverse(ListNode *pre,ListNode *begin,ListNode *end)
    {
        ListNode *end_next=end->next;
        for(ListNode *p=begin,*cur=begin->next,*next=cur->next;
            cur!=end_next;
            p=cur,cur=next,next=next?next->next:NULL)
            {
                cur->next=p;
            }
        begin->next=end_next;
        pre->next=end;
        return begin;  
    }
};