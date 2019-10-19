class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = p = ListNode(0)
        for k in lists:
            while k:
                self.nodes.append(k.val)
                k = k.next
        for x in sorted(self.nodes):
            p.next = ListNode(x)
            p = p.next
        return head.next