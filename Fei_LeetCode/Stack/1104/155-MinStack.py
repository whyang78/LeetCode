class MinStack(object):
    def __init__(self):
        self.__list = []

    def push(self, x: int):
        self.__list.append(x)

    def pop(self):
        return self.__list.pop()

    def top(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def getMin(self):
        return min(self.__list)

# 上面用min()方法来做的话时间复杂度是O（n），构建辅助栈来做的话时间是0（1）
# 用空间来换时间
class MinStack1(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    print(obj.getMin())
    print(obj.top())
