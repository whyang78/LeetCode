class LinkNode(object):
    def __init__(self, elem):
        self.val = elem
        self.next = None

# 递归
def removeDuplicates(self, head: LinkNode):
    if head is None:
        return
    if head.next is not None and head.val == head.next.val:
        while head is not None and head.next is not None and head.val == head.next.val:
            head = head.next
        return self.removeDuplicates(head.next)
    else:
        head.next = self.removeDuplicates(head.next)
    return head
