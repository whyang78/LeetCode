class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right)
        else:
            return p is q