class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleList:
    def initial(self, sl):
        pre = ListNode(0)
        n = 0
        head = 1
        while n != -1:
            n = int(input())
            if n == -1:
                if head == 1:
                    sl = None
            else:
                if head == 1:
                    sl.val = n
                    sl.next = None
                    pre = sl
                    head = 0
                else:
                    p = ListNode(n)
                    pre.next = p
                    pre = p

    def initial1(self, sl):
        num = [int(n) for n in input().split()]
        if len(num) == 0:
            sl = None
        else:
            sl.val = num[0]
            pre = ListNode(0)
            pre = sl
            for i in range(1, len(num)):
                p = ListNode(num[i])
                pre.next = p
                pre = p


class Solution:
    def mergeTwoLists(self, L1: ListNode, L2: ListNode) -> ListNode:
        if L1 is None:
            return L2
        if L2 is None:
            return L1
        if L1.val <= L2.val:
            L1.next = self.mergeTwoLists(L1.next, L2)
            return L1
        else:
            L2.next = self.mergeTwoLists(L1, L2.next)
            return L2


if __name__ == '__main__':
    b = Solution()
    c = SingleList()
    l1 = ListNode(0)
    l2 = ListNode(0)
    lm = ListNode(0)
    # print("请输入升序链表l1(以回车隔开，输入-1结束):")
    # c.initial(l1)
    # print("请输入升序链表l2(以回车隔开，输入-1结束):")
    # c.initial(l2)
    print("请输入升序链表l1(以空格隔开，输入回车结束):", end="")
    c.initial1(l1)
    print("请输入升序链表l2(以空格隔开，输入回车结束):", end="")
    c.initial1(l2)
    lm = b.mergeTwoLists(l1, l2)
    while lm:
        print(lm.val, end=" ")
        lm = lm.next
