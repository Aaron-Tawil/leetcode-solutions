# Problem: 17 - Letter Combinations of a Phone Number
# Difficulty: Medium
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs",'8': "tuv", '9': "wxyz"
        }

        res = []
        buf = []

        def backtrack(i):
            if i == len(digits):
                res.append(''.join(buf))


            else: 
                for c in mapping[digits[i]]:
                    buf.append(c)
                    backtrack(i+1)
                    buf.pop()

        backtrack(0)
        return res