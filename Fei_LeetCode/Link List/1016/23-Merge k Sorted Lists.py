class LinkNode(object):
    def __init__(self, elem):
        self.val = elem
        self.next = None


# 暴利法，遍历所有链表放在一个数组中，排序后，再次遍历得到一个新的链表
def mergeKLists(self, lists: list[LinkNode]):
    self.node = []
    # 定义两个节点
    head = cur = LinkNode(0)
    for l in lists:
        while l:
            self.node.append(l.val)
            l = l.next
    for x in sorted(self.node):
        cur.next = LinkNode(x)
        cur = cur.next
    return head.next


# 分治法
def mergeKLists1(self, lists: list[LinkNode]):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = self.merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists

def merge2Lists(self, l1, l2):
    head = point = LinkNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
    if not l1:
        point.next = l2
    else:
        point.next = l1
    return head.next
