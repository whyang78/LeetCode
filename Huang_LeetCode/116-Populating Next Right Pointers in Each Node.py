class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root