class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []

        self.__dfs(candidates, size, 0, [], target, res)
        return res

    def __dfs(self, candidates, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])
            return
        for index in range(start, size):
            if candidates[index] > residue:
                break
            # 剪枝的前提是数组升序排序
            if index > start and candidates[index - 1] == candidates[index]:
                continue

            path.append(candidates[index])
            # 传入index+1,当前元素不能被重复使用
            self.__dfs(
                candidates, size, index + 1, path, residue - candidates[index], res
            )
            path.pop()
