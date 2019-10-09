# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(-1)
        pre=head
        c=0
        while c or l1 or l2:
            c,val=divmod(c+(l1.val if l1 else 0) + (l2.val if l2 else 0),10)
            pre.next=ListNode(val)
            pre=pre.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return head.next