from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            in_degree[a]+=1
        
        q = deque()
        for course in range(numCourses):
            if not in_degree[course]:
                q.append(course)
        
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for course in adj[curr]:
                in_degree[course]-=1
                if in_degree[course]==0:
                    q.append(course)
        
        return res if len(res)==numCourses else []