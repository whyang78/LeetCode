class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(self, head: LinkNode, val):
    cur = head
    pre = head
    while head is not None and head.val == val:
        head = head.next
    if head is None:
        return
    while cur:
        if cur.val != val:
            pre = cur
        else:
            pre.next = cur.next
        cur = cur.next
    return head
