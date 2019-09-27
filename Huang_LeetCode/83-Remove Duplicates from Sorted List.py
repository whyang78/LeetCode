class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        while prev:
            while prev.next and prev.val == prev.next.val:
                prev.next = prev.next.next
            prev = prev.next
        return head