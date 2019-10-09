class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        b =''
        result = []
        for i in range(len(A)):
            b+=str(A[i])
        num = int(b)+K
        return [int(i) for i in str(num)]



class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum1 = 0
        results = []
        for j in A:
            if j%2 ==0:
                sum1 += j
        for val,ind in queries:
            pre = A[ind]
            if pre % 2 ==0:
                sum1 -= pre
            A[ind] += val
            if A[ind] % 2 ==0:
                sum1 +=A[ind]
            results.append(sum1)
        return results

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        import operator
        cost_diff = {}
        results = []
        N = len(costs)
        n = int(N/2)
        for i in range(N):
            cost_diff[i] = costs[i][1] - costs[i][0]
        a = sorted(cost_diff.items(), key=operator.itemgetter(1))
        for i in range(N):
            b = a[i][0]
            results.append(b)
        cost = 0
        for i in range(n):
            result = results[i]
            cost += costs[result][1]
        for i in range(n,N):
            result = results[i]
            cost += costs[result][0]
        return cost  
