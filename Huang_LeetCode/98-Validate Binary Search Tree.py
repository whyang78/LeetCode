class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        self.inOrder(root, output)

        return all([a > b for a, b in zip(output[1:], output)])

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)