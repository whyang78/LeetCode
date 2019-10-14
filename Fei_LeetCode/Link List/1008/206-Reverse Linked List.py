class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(self, head: ListNode):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev





