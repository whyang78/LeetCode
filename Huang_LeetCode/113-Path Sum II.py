class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        stack = []
        if not root:
            return []

        def help(root, sum, tmp):
            if not root:
                return []
            if not root.left and not root.right and sum - root.val == 0:
                tmp += [root.val]
                stack.append(tmp)
            sum -= root.val
            help(root.left, sum, tmp + [root.val])
            help(root.right, sum, tmp + [root.val])

        help(root, sum, [])
        return stack