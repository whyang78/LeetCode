//方法一：头插法 一遍遍历
/*
第一步是将结点3放到结点1的后面，第二步将结点4放到结点1的后面。
这是很有规律的操作，那么我们就说一个就行了，比如刚开始，pre指向结点1，cur指向结点2，
然后我们建立一个临时的结点t，指向结点3（注意我们用临时变量保存某个结点就是为了首先断开该结点和前面结点之间的联系，
这可以当作一个规律记下来），然后我们断开结点2和结点3，将结点2的next连到结点4上，也就是 cur->next = t->next，
再把结点3连到结点1的后面结点（即结点2）的前面，即 t->next = pre->next，最后再将原来的结点1和结点2的连接断开，
将结点1连到结点3，即 pre->next = t。这样我们就完成了将结点3取出，加入结点1的后方。
第二步将结点4取出，加入结点1的后方，也是同样的操作，
*/
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode dummy(-1);//头结点
        dummy.next=head;
        ListNode *p=&dummy;

        for(int i=0;i<m-1;i++)
            p=p->next;
        ListNode *cur=p->next;
        for(int i=m;i<n;i++)
        {
            ListNode *temp=cur->next;
            cur->next=temp->next;
            temp->next=p->next;
            p->next=temp;
        }
        return dummy.next;

    }
};

//方法二：两边遍历
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *p=head;
        stack<int> st;

        int i=1;
        while(p && i<=n && n>=m)
        {
            if(i>=m)
            {
                st.push(p->val);
            }
            i++;
            p=p->next;
        }

        p=head;
        i=1;
        while(p && i<=n && n>=m)
        {
            if(i>=m)
            {
                p->val=st.top();
                st.pop();
            }
            i++;
            p=p->next;
        }
        return head;

    }
};