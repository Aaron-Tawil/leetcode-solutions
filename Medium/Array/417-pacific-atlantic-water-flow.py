from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]

        def visited_set_bfs(starts):
            q = deque(starts)
            visited = set(starts)

            while q:
                cr ,cc = q.popleft()
                for dr,dc in dirs:
                    nr,nc = cr+dr , cc+dc
                    if 0<=nr<m and 0<=nc<n and heights[nr][nc]>=heights[cr][cc] and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            
            return visited

        
        starts_pacific = [(0,c) for c in range(n) ] + [(r,0) for r in range(m)]
        starts_atlantic = [(m-1,c) for c in range(n) ] + [(r,n-1) for r in range(m)]

        visited_pacific = visited_set_bfs(starts_pacific)
        visited_atlantic = visited_set_bfs(starts_atlantic)

        return [[r, c] for r, c in visited_pacific & visited_atlantic]
        