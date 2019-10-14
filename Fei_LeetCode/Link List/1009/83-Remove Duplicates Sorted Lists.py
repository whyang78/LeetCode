class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeDuplicatesLists(self, head: LinkList):
    front = head
    while front is not None:
        rear = front.next

        while rear is not None and front.val == rear.val:
            rear = rear.next
        front.next = rear
        front = front.next
    return head
