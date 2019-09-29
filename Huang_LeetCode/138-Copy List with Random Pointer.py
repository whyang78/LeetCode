class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d, node = {None: None}, head
        while node:
            d[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            d[node].next = d[node.next]
            d[node].random = d[node.random]
            node = node.next
        return d[head]