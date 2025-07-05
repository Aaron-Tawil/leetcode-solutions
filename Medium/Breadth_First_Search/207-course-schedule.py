# Problem: 207 – course schedule
# Difficulty: Medium
# Link: https://leetcode.com/problems/course-schedule/description/


from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #check for cycles
        gr = defaultdict(list)
        in_deg = [0] * numCourses
        for a,b in prerequisites:
            gr[b].append(a)
            in_deg[a]+=1
        
        taken = 0
        q = deque()
        for c in range(numCourses):
            if in_deg[c] ==0:
                q.append(c)
        
        while q:
            preq = q.popleft()
            taken+=1
            for c in gr[preq]:
                in_deg[c]-=1
                if in_deg[c]==0:
                    q.append(c)
            

        return taken==numCourses

        