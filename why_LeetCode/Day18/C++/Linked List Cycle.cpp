'''
�������뵽�ķ����ǣ���һ����ϣ��unordered. map<int, bool> visited, ��¼ÿ��Ԫ����
�񱻷��ʹ���-������ĳ��Ԫ�ر��ظ����ʣ�˵�����ڻ����ռ临�Ӷ�O(n),ʱ�临�Ӷ�O(N)��
��õķ�����ʱ�临�Ӷ�O(n)�� �ռ临�Ӷ�0(1)�ġ���������ָ�룬һ����һ����, 
���ָ��ÿ��������������ָ��ÿ����-���������ָ�����ָ����������˵���л���

'''


//����һ��set����
//ʱ�临�Ӷȣ�O(N) �ռ临�Ӷȣ�O(N)
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

//��������˫ָ�뷨
//ʱ�临�Ӷȣ�O(N) �ռ临�Ӷȣ�O(1)
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