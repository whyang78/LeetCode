class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        len = 1
        p = head
        while p.next:
            len += 1
            p = p.next
        k = len - k % len
        # 首尾相连
        p.next = head
        step = 0
        while step < k:
            p = p.next
            step += 1
        head = p.next
        p.next = None
        return head