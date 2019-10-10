class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for k, v in enumerate(tokens):
            if v in '+-*/':
                b, a = stack.pop(), stack.pop()
                v = eval('a' + v + 'b')
            stack.append(int(v))
        return stack.pop()


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t, f = tokens.pop(), self.evalRPN
        if t in '+-*/':
            b, a = f(tokens), f(tokens)
            t = eval('a' + t + 'b')
        return int(t)