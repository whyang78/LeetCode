class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(self, head: LinkNode):
    # cur = head
    # st = []
    # while cur:
    #     st.append(cur.val)
    #     cur = cur.next
    # length = len(st)
    # middle_index = int(length / 2)
    # middle_val = st[middle_index]
    # while cur:
    #     if cur.val == middle_val:
    #         head = cur
    #     else:
    #         cur = cur.next
    #  return head
    A = [head]
    while A[-1].next:
        A.append(A[-1].next)
    return A[len(A) // 2]
