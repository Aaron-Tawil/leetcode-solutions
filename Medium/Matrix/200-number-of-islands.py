# Problem: 200 – number of islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-islands/description/


from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        res = 0
        st = [] # for DFS
        q = deque() # for BFS
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def exploreDFS(i,j):
            st.append((i,j))
            while st:
                rc,cc = st.pop()
                for dr,dc in dirs:
                    r,c = dr+rc,dc+cc
                    if 0<=r<m and 0<=c<n  and grid[r][c] =='1':
                        grid[r][c]='#'
                        st.append((r,c))
            

        def exploreBFS(i,j):
            q.append((i,j))
            while q:
                rc,cc = q.popleft()
                for dr,dc in dirs:
                    r,c = dr+rc,dc+cc
                    if 0<=r<m and 0<=c<n  and grid[r][c] =='1':
                        grid[r][c]='#'
                        q.append((r,c))
                

        for row in range(m):
            for col in range(n):
                if grid[row][col]=='1':
                    res+=1
                    grid[row][col]='#'
                    exploreBFS(row,col)
                    # exploreDFS(row,col)
        return res
        