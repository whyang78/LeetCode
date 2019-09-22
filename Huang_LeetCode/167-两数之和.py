class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
        while numbers[first] + numbers[last] != target:
            if numbers[first] + numbers[last] > target:
                last -= 1
            else:
                first += 1
        return [first + 1, last + 1]
