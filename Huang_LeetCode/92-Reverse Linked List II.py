class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummyNode = ListNode(-1)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next