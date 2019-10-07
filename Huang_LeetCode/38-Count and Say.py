class Solution:
    def countAndSay(self, n: int) -> str:
        return '1' * (n is 1) or re.sub(
            r'(.)\1*', lambda m: str(len(m.group())) + m.group(1),
            self.countAndSay(n - 1))