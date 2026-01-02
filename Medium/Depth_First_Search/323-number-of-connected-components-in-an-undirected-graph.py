from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #bfs
        # adj = [[]for i in range(n)]
        # for a,b in edges:
        #     adj[a].append(b)
        #     adj[b].append(a)
        
        # counter = 0
        # visited = [False]*n
        # for node in range(n):
        #     if not visited[node]:
        #         q = deque([node])
        #         visited[node] = True
        #         counter+=1
        #         while q:
        #             curr_node = q.popleft()
        #             for u in adj[curr_node]:
        #                 if not visited[u]:
        #                     q.append(u)
        #                     visited[u]=True
                    
        # return counter
        #union find
        uf = UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        return uf.sets

class UnionFind:
    def __init__(self,n):
        self.parent = [ i for i in range(n)]
        self.sets = n 
    
    def union(self,v,u):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u!=root_v:
            self.parent[root_u] = root_v
            self.sets-=1

    def find(self,i):
        if self.parent[i]==i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
