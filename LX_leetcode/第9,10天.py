class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x!= s2[i]:
                return s2[:i]
        return s1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res  = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val < l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next
