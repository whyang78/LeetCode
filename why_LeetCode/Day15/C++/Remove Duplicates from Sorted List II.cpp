//方法一：迭代法
//时间复杂度 O(N) 空间复杂度 O(1)
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(-1);
        dummy.next=head;

        ListNode *pre=&dummy,*cur=head;
        while(cur)
        {
            bool flag=false;
            while(cur->next && cur->val==cur->next->val)
            {
                flag=true;
                ListNode *temp=cur;
                cur=cur->next;
                delete temp;
            }

            if(flag)
            {
                ListNode *temp=cur;
                cur=cur->next;
                delete temp;
                continue;
            }

            pre->next=cur;
            pre=cur;
            cur=cur->next;
        }
        pre->next=cur;
        return dummy.next;
    }
};


//方法二：双指针法
//时间复杂度 O(N) 空间复杂度 O(1)
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(-1);
        dummy.next=head;

        ListNode *pre=&dummy,*cur=head;
        while(cur)
        {
            if(cur->next==NULL || cur->val!=cur->next->val)
            {
                if(pre->next==cur)
                {
                    pre=cur;
                }
                else
                {
                    pre->next=cur->next;
                }
            }
            cur=cur->next;
        }
        pre->next=cur;
        return dummy.next;

    }
};