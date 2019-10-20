# 刚开始没读懂题意，一直很奇怪怎么没传进head，看了解析后才发现是被固定思维所限制
# 一般从链表中删除节点最常见的做法是修改之前的节点使其指向下一个节点，但这题是无法知道它的前一个节点
# 这题的做法则应该是将要删除节点的值替换成后一个节点，再把后一个节点删除

# 前提：删除的节点不是末尾节点

class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
