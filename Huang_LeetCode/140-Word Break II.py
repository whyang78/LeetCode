from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [
                    s[i:j] + (tail and ' ' + tail)
                    for j in range(i + 1,
                                   len(s) + 1) if s[i:j] in wordDict
                    for tail in sentences(j)
                ]
            return memo[i]

        return sentences(0)


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
sol = Solution()
sol.wordBreak(s, wordDict)
