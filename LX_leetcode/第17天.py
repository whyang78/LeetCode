class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n=len(A)
        i=0
        j=1
        res=[0]*n
        for a in A:
            if a%2==0:
                res[i]=a
                i+=2
            else:
                res[j]=a
                j+=2
        return res


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a = sum(A)
        b = sum(B)
        diff = (a-b)/2
        setb =set(B)
        for i in A:
            if (i - diff) in setb:
                return [i,int(i-diff)]
