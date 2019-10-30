'''
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next =None
    #1.用辅助栈存储
    def Solution1(listNode):
        stack = []
        result_array=[]
        node_p = listNode
        while node_p:
            stack.append(node_p.val)
            node_p = node_p.next
        while stack:
            result_array.append(stack.pop(-1))
        return result_array
    #2.本身栈调用
    result_array =[]
    def Solution2(listNode):
        if listNode:
            Solution2(listNode.next)
            result_array.append(listNode.val)
        return result_array

