# Problem: 22 – generate parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/generate-parentheses/description

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        buf = []

        def backtrack(o,c):
            if o==0 and c ==0:
                res.append(''.join(buf))
                return
            if c>o and c>0:
                buf.append(')')
                backtrack(o,c-1)
                buf.pop()
            if o>0:
                buf.append('(')
                backtrack(o-1,c)
                buf.pop()
    
        backtrack(n,n)
        return res

    # def generate_parentheses(n: int) -> list[str]:
    #     res = []
    #     def backtrack(s: str, open_count: int, close_count: int):
    #         if len(s) == 2 * n:
    #             res.append(s)
    #             return
    #         if open_count < n:
    #             backtrack(s + '(', open_count + 1, close_count)
    #         if close_count < open_count:
    #             backtrack(s + ')', open_count, close_count + 1)

    #     backtrack('', 0, 0)
    #     return res

