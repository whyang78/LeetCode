//方法一：双指针法
//设起点至环入口处距离a,环长r。相遇时，fast指针走了2s,slow指针走了s。
//2s-s=nr(n>=1)      s=nr
//从起点出发最终到达环入口点：a+nr(先到达环入口点，然后绕环几周都可以回到环入口点)
//所以slow指针再走a距离便可到达环入口点
//在头结点设置slow2指针，与slow相同步伐，最终肯定会在环入口处相遇(slow2指针距环入口处为a)。
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {     
        ListNode *fast=head,*slow=head;
        while(fast && fast->next)
        {
            fast=fast->next->next;
            slow=slow->next;
            if(fast==slow)
            {
                ListNode *slow2=head;
                while(slow2!=slow)
                {
                    slow2=slow2->next;
                    slow=slow->next;
                }
                return slow2;
            }
        }
        return NULL;
    }
};




//方法二：set集合
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {     
        set<ListNode*> s;
        ListNode *p=head;
        while(p)
        {
            if(s.find(p)!=s.end())
            {
                return p;
            }
            s.insert(p);
            p=p->next;
        }
        return NULL;
    }
};
