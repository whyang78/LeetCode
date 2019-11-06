# 用两个栈来实现
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        if self.stack1 is None:
            self.stack1.append(x)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def empty(self):
        return self.stack1 == []


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.empty())
    obj.pop()
    print(obj.peek())
