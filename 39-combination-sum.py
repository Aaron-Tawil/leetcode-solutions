# Problem: 39 – combination sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        comb = []
        def backtrack(target,start):
            if 0 ==target:
                res.append(comb.copy())
                return
            elif 0>target:
                return
            for i in range(start,n):
                if target< candidates[i]:
                    break
                comb.append(candidates[i])
                backtrack(target-candidates[i],i)
                comb.pop()
        backtrack(target,0)
        return res