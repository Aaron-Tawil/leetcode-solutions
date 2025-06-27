# Problem: 78 – subsets
# Difficulty: Medium
# Link: https://leetcode.com/problems/subsets/description/


from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        sub = []

        def backtrack(start):
            res.append(sub.copy())
            for i in range(start,n):
                sub.append(nums[i])
                backtrack(i+1)
                sub.pop()

        backtrack(0)
        return res

        # return [
        #     list(c)
        #     for r in range(len(nums) + 1)
        #     for c in combinations(nums, r)
        # ]
        # def backtrack(i):
        #     if i == n:
        #         res.append(sub.copy())       # record only at leaves
        #         return
        #     backtrack(i+1)                        # SKIP nums[i]
        #     sub.append(nums[i])
        #     backtrack(i+1)                        # INCLUDE nums[i]
        #     sub.pop()
