class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归方法
# 在用递归时，我们关心的是：
# 1.返回值：交换完成的子链表
# 2.调用单元：设需要交换的两个点为 head 和 next，head 连接后面交换完成的子链表，next 连接 head，完成交换
# 3.终止条件：head 为空指针或者 next 为空指针，也就是当前无节点或者只有一个节点，无法进行交换
def swapPairs(self, head: LinkNode):
    if head is None or head.next is None:
        return head
    rear = head.next
    head.next = self.swapPairs(rear.next)
    rear.next = head
    return rear
