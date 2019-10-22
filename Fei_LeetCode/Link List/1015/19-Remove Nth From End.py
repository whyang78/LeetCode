class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 两次遍历，第一次遍历先找到要删除的值并计数
# 第二次遍历找到该值的前一个
def removeNthFromEnd(self, head: LinkNode, n: int):
    cur = head
    pre = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    remove_index = count - n
    # 删除的是头元素时
    if remove_index == 0:
        return head.next
    while remove_index-1 > 0:
        remove_index -= 1
        pre = pre.next
    pre.next = pre.next.next
    return head


# 方法二 快慢指针
