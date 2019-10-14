class Solution:
    def __init__(self):
        self.res = []

    def recoverTree(self, root):
        self.mid(root)
        node1 = None
        node2 = None
        for i in range(len(self.res) - 1):
            if self.res[i].val > self.res[i + 1].val and node1 == None:
                node1 = self.res[i]
                node2 = self.res[i + 1]
            elif self.res[i].val > self.res[i + 1].val and node1 != None:
                node2 = self.res[i + 1]

        node1.val, node2.val = node2.val, node1.val

    def mid(self, root):
        if root is not None:
            self.mid(root.left)
            self.res.append(root)
            self.mid(root.right)
