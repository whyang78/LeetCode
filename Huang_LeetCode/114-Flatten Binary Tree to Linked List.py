class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root is not None:
            if root.left is not None:
                pre_rigth = root.left
                while pre_rigth.right is not None:
                    pre_rigth = pre_rigth.right
                pre_rigth.right = root.right
                root.right = root.left
                root.left = None
            root = root.right