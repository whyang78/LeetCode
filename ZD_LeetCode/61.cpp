    /**
     * Definition for singly-linked list.
     * struct ListNode {
     *     int val;
     *     ListNode *next;
     *     ListNode(int x) : val(x), next(NULL) {}
     * };
     */
    class Solution {
    public:
        ListNode* rotateRight(ListNode* head, int k) {
            if (!head) return 0;
            int c = 1;
            ListNode* p = head;
            while (p->next) {
                ++c;
                p = p->next;
            }   
            p->next = head;
            k = c - k % c;
            for (int i = 0; i < k; ++i) {
                p = p->next;
            }
            head = p->next;
            p->next = 0;
            return head;
        }
    };
