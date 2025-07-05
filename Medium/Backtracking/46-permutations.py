# Problem: 46 – permutations
# Difficulty: Medium
# Link: https://leetcode.com/problems/permutations/description/

from itertools import permutations 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] *n
        path =[]
        res = []
        def backtrack():
            if len(path) == n:
                res.append(path.copy())
                return
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack()

                    path.pop()
                    used[i] = False

        backtrack()
        return res    
        # return list(permutations(nums))