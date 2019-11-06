import collections

# 单队列
class MyStack(object):
    def __init__(self):
        """
        使用collections模块实现了特定目标的容器
        以提供Python标准内建容器 dict、list、set、tuple 的替代选择。
        Counter：字典的子类，提供了可哈希对象的计数功能
        defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供了默认值
        OrderedDict：字典的子类，保留了他们被添加的顺序
        namedtuple：创建命名元组子类的工厂函数
        deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)
        ChainMap：类似字典的容器类，将多个映射集合到一个视图里面
        """
        self.stack = collections.deque()

    # 从右侧操作
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        for i in range(len(self.stack)-1):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self):
        temp = self.stack.pop()
        self.stack.append(temp)
        return temp

    def empty(self):
        return not self.stack
