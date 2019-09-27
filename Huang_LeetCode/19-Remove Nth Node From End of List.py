class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        for i in range(n):
            q = q.next
        if not q:
            return head.next
        while q.next:
            q = q.next
            p = p.next
        p.next = p.next.next
        return head