class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy = ListNode(-1)
        right_dummy = ListNode(-1)

        left_cur = left_dummy
        right_cur = right_dummy
        cur = head
        while cur:
            if cur.val < x:
                left_cur.next = cur
                left_cur = cur
            else:
                right_cur.next = cur
                right_cur = cur
            cur = cur.next
        left_cur.next = right_dummy.next
        right_cur.next = None
        return left_dummy.next