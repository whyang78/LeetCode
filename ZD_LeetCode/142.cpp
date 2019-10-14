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
    ListNode *detectCycle(ListNode *head) {
        ListNode *low = head, *fast = head;
        while (fast && fast->next) {
            low = low->next;
            fast = fast->next->next;
            if (low == fast) {
                ListNode *low2 = head;
                while (low2 != low) {
                    low = low->next;
                    low2 = low2->next;
                }
                return low;
            }
        }
        return 0;
    }
};
