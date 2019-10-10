class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return root and sum(
            ([root.val],
             *map(self.preorderTraversal, [root.left, root.right])), []) or []


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        r, stack = [], root and [root] or []
        while stack:
            root = stack.pop()
            r.append(root.val)
            stack += root.right and [root.right] or []
            stack += root.left and [root.left] or []
        return r