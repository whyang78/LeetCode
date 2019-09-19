class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = str1
        for i in range(1,len(str1)):
            if str1.count(str1[:i])*i == len(str1):
                s1 = str1[:i]
                break
        c1 = str1.count(s1)
        c2 = str2.count(s1)
        for n in range(min(c1,c2),0,-1):
            if c1%n ==0 and c2%n ==0:
                return n*s1
        return ''




class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(' ')
        results = []
        for i,word in enumerate(text):
            if i < len(text)-2:
                if word == first and text[i+1] == second:
                    results.append(text[i+2])
        return results
