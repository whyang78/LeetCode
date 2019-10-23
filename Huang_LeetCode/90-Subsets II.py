class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        c = Counter(nums)
        res = [[]]
        for i, v in c.items():
            temp = res.copy()
            for j in res:
                temp.extend(j + [i] * (k + 1) for k in range(v))
            res = temp
        return res