class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty())
            return NULL;
        
        ListNode *result=lists[0];
        for(int i=1;i<lists.size();i++)
        {
            result=mergeTwoLists(result,lists[i]);
        }
        return result;
    }
private:
    ListNode* mergeTwoLists(ListNode* l1,ListNode* l2)
    {
        ListNode dummy(-1);
        for(ListNode* p=&dummy;l1!=NULL||l2!=NULL;p=p->next)
        {
            int val1=l1==NULL?INT_MAX:l1->val;
            int val2=l2==NULL?INT_MAX:l2->val;
            if(val1<=val2)
            {
                p->next=l1;
                l1=l1->next;
            }
            else
            {
                p->next=l2;
                l2=l2->next;
            }
        }
        return dummy.next;
    }
};