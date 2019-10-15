class LinkList(object):
    def __init__(self, x):
        self.val = x

# 方法一 哈希表
def getIntersectionNode(self, headA, headB):
    hashA = {}
    while headA:
        hashA[headA] = 1
        headA = headA.next
    while headB:
        if hashA.get(headB) is not None:
            return headB
        headB = headB.next

# 双指针
def getIntersectionNode1(self, headA, headB):
    p, q = headA, headB
    while p != q:  # 到达相交点是会提前跳出，不然到最后p和q都是None
        p = p.next if p else headB  # 当A链表到尽头就接上B的表头
        q = q.next if q else headA
    return p