# Problem: 789 – escape the ghosts
# Difficulty: Medium
# Link: https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distp = abs(target[0])+abs(target[1])
        for xg,yg in ghosts:
            distg = abs(target[0]-xg)+abs(target[1]-yg)
            if distg<=distp:
                return False
        return True