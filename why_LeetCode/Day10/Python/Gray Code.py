class Solution:
    def grayCode(self, n: int) -> List[int]:
        result=[]
        result.append(0);
        for i in range(n):
            hightest=1<<i;
            for j in range(len(result)-1,-1,-1):
                result.append(result[j]|hightest)
        return result;