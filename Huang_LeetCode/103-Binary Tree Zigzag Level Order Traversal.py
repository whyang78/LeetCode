class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        ans = [k if i % 2 == 0 else k[::-1] for i, k in enumerate(ans)]
        return ans