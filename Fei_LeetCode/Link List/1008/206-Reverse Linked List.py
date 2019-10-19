class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(self, head: ListNode):
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev




