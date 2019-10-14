//����һ��˫ָ�뷨
//�����������ڴ�����a,����r������ʱ��fastָ������2s,slowָ������s��
//2s-s=nr(n>=1)      s=nr
//�����������յ��ﻷ��ڵ㣺a+nr(�ȵ��ﻷ��ڵ㣬Ȼ���ƻ����ܶ����Իص�����ڵ�)
//����slowָ������a�����ɵ��ﻷ��ڵ�
//��ͷ�������slow2ָ�룬��slow��ͬ���������տ϶����ڻ���ڴ�����(slow2ָ��໷��ڴ�Ϊa)��
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




//��������set����
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
