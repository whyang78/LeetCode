class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return
        node_arr = []
        while head:
            node_arr.append(head.val)
            head = head.next

        def buildBST(nums):
            if len(nums) == 0:
                return
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = buildBST(nums[:mid])
            root.right = buildBST(nums[mid + 1:])
            return root

        return buildBST(node_arr)