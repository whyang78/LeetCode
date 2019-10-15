class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: LinkList):
    result = set()
    p = head
    while p is not None:
        if p in result:
            return True
        else:
            result.add(p)
            p = p.next
    return False
