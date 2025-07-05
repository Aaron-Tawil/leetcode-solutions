# Problem: 131 – palindrome partitioning
# Difficulty: Medium
# Link: https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def backtrack(start,part):
            if start == n:
                res.append(part[:])
                return
            for end in range(start+1,n+1):
                prefix  = s[start:end]
                if prefix == prefix[::-1]: #is palindrome
                    part.append(prefix)
                    backtrack(end,part)
                    part.pop()
        backtrack(0,[])
        return res
        