class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'IV': 3,
            'V': 5,
            'IX': 8,
            'X': 10,
            'XL': 30,
            'L': 50,
            'XC': 80,
            'C': 100,
            'CD': 300,
            'D': 500,
            'CM': 800,
            'M': 1000
        }
        r = d[s[0]]
        for i in range(1, len(s)):
            r += d.get(s[i - 1:i + 1], d[s[i]])
        return r