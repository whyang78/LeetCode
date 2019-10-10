//方法一：两次遍历 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1);
        dummy.next=head;
        ListNode *p=head;

        int length=0;
        while(p)
        {
            length++;
            p=p->next;
        }

        length-=n;
        p=&dummy;
        while(length>0)
        {
            p=p->next;
            length--;
        }
        p->next=p->next->next;
        return dummy.next;
    }
};

//一次遍历
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1);
        dummy.next=head;
        ListNode *before=&dummy;
        ListNode *after=&dummy;

        for(int i=1;i<=n+1;i++)
        {
            after=after->next;
        }

        while(after!=NULL)
        {
            after=after->next;
            before=before->next;
        }
        before->next=before->next->next;
        return dummy.next;
    }
};