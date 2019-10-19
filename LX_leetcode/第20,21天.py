class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_list = sorted(list(set(s)),key = s.index)
        res = []
        for i in s_list:
            if s.count(i)==1:
                res.append(i)
                break
        if len(res)==0:
            return -1
        else:
            return s.index(res[0])


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 ={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        return sorted(dict1.items(),key = lambda item:item[1])[0][0]
