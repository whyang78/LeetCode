class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一 辅助列表 + 快慢指针
def isPalindrome(self, head: LinkNode):
    st = []
    while head:
        st.append(head.val)
        head = head.next
    front = 0
    rear = len(st)-1
    while front < rear:
        if st[front] != st[rear]:
            return False
        front += 1
        rear -= 1
    return True


# 快慢指针 + 翻转
def isPalindrome1(self, head: LinkNode) -> bool:
    fast = slow = head
    # 快慢指针，快指针到达尾部，慢指针到达中间
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # 奇数长，fast指针在最后一个，slow在最中间，slow需要往后过一个
        # 偶数长，fast为空，slow指针中点过一个
        if fast:
            slow = slow.next
        pre = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
