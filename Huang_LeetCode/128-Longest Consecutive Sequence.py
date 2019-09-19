class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        used = {x: False for x in nums}
        longest = 0
        for i in used:
            if used[i] == False:
                curr, lenright = i + 1, 0
                while curr in used:
                    lenright += 1
                    used[curr] = True
                    curr += 1
                curr, lenleft = i - 1, 0
                while curr in used:
                    lenleft += 1
                    used[curr] = True
                    curr -= 1
                longest = max(longest, lenleft + 1 + lenright)
        return longest