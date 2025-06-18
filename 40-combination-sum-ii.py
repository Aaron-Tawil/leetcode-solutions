# Problem: 40 – combination sum II
# Difficulty: Medium
# Link: https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res =[]
        comb =[]
        n = len(candidates)

        def backtrack(start,target):
            if target==0:
                res.append(comb[:])
                return   
            for i in range(start,n):
                if i>start and candidates[i]==candidates[i-1] or candidates[i]>target:
                    continue 
                comb.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                comb.pop()
        
        backtrack(0,target)
        return res