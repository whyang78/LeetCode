class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        r = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right
        return r