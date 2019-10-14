class LinkList(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoSortedLists(self, l1: LinkList, l2: LinkList):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = self.mergeTwoSortedLists(l2, l1.next)
        return l1
    else:
        l2.next = self.mergeTwoSortedLists(l1, l2.next)
        return l2
