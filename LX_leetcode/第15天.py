class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A
