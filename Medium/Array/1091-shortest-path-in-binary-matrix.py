from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        q = deque([[0,0]])
        grid[0][0]=1
        dist = 0
        while q:
            dist+=1
            for _ in range(len(q)):
                cr,cc = q.popleft()
                if cr==n-1 and cc==n-1:
                    return dist
                for dr,dc in dirs:
                    nr,nc = cr+dr,cc+dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                        grid[nr][nc]=1
                        q.append([nr,nc])
                    
        return -1