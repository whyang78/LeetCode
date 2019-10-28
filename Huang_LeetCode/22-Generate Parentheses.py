class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(S="", left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                generate(S + "(", left + 1, right)
            if right < left:
                generate(S + ")", left, right + 1)

        generate()
        return ans
