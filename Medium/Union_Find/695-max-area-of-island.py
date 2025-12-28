from collections import deque
class Solution:
    #dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi=  0
        rows,cols = len(grid), len(grid[0])

        def dfs(r,c):
            if not(0<=r<rows) or not(0<=c<cols) or grid[r][c]==0:
                return 0 
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxi = max(maxi,dfs(r,c))
                
        return maxi
    #bfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        maxi=  0
        rows,cols = len(grid), len(grid[0])

        def bfs(r,c):
            size = 0
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            
            while q:
                cr,cc = q.popleft()
                size+=1
                for dir in dirs:
                    dr,dc = dir
                    nr,nc = cr+dr,cc+dc
                    if 0<=nr< rows and 0<=nc< cols and grid[nr][nc]==1:
                        grid[nr][nc] = 0
                        q.append((nr,nc))        
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxi = max(maxi,bfs(r,c))
                
        return maxi

    