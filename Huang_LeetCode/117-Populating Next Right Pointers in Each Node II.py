class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and (root.left or root.right):
            if root.left and root.right:
                root.left.next = root.right
            node = root.right or root.left
            head = root.next
            while head and not (head.left or head.right):
                head = head.next
            node.next = head and (head.left or head.right)

            self.connect(root.right)
            self.connect(root.left)

        return root