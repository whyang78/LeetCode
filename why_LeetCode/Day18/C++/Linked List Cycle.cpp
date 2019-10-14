'''
最容易想到的方法是，用一个哈希表unordered. map<int, bool> visited, 记录每个元素是
否被访问过，-旦出现某个元素被重复访问，说明存在环。空间复杂度O(n),时间复杂度O(N)。
最好的方法是时间复杂度O(n)， 空间复杂度0(1)的。设置两个指针，一个快一个慢, 
快的指针每次走两步，慢的指针每次走-步，如果快指针和慢指针相遇，则说明有环。

'''


//方法一：set集合
//时间复杂度：O(N) 空间复杂度：O(N)
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // if(head==NULL || head->next==NULL)
        //     return false;
        
        set<ListNode*> s;
        ListNode *p=head;
        while(p)
        {
            if(s.find(p)!=s.end())
            {
                return true;
            }
            s.insert(p);
            p=p->next;
        }
        return false;
    }
};

//方法二：双指针法
//时间复杂度：O(N) 空间复杂度：O(1)
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *fast=head,*slow=head;
        while(fast && fast->next)
        {
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast)
            {
                return true;
            }    
        }
        return false;
    }
};