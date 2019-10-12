class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A=A.split(' ')
        B=B.split(' ')
        C = set(A+B)
        result = []
        for i in C:
            if (A.count(i)==1 and B.count(i) ==0) or (A.count(i)==0 and B.count(i) ==1) :
                result.append(i)
        return result
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        t = 1
        if max(A) == A[0]:
            for i in range(n-1):
                if A[i] >= A[i+1]:
                    t *=1
                else:
                    t *=0
        elif min(A) == A[0]:
            for i in range(n-1):
                if A[i+1] >= A[i]:
                    t *=1
                else:
                    t *=0
        else:
            t *=0
        return bool(t)
