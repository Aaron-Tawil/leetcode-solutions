# Problem: 1631 – path with minimum effort
# Difficulty: Medium
# Link: https://leetcode.com/problems/path-with-minimum-effort/

import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights) , len(heights[0])
        h = []
        minef = [[float('inf')]*n for _ in range(m)]
        minef[0][0] = 0
        hq.heappush(h,(0,0,0)) # effort, r,c
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]


        while h:
            ce, cr, cc = hq.heappop(h)
            if cr==m-1 and cc== n-1:
                return ce
            if ce > minef[cr][cc]:
                continue    

            for dr, dc in dirs:
                nr,nc = dr+cr, dc+cc
                if 0 <= nr < m and 0 <= nc < n:
                    ne =max(ce, abs(heights[cr][cc] - heights[nr][nc]))
                    if ne< minef[nr][nc]:
                        minef[nr][nc] = ne
                        hq.heappush(h,(ne,nr,nc))


        return 0 #unreachable