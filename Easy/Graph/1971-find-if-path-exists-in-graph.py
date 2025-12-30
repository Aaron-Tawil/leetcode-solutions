from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        return uf.find(source)==uf.find(destination)

class UnionFind:
    def __init__(self, n):
        # How should we initialize the parent list?
        self.parent = [i for i in range(n)]
    
    def find(self,i):
        if self.parent[i]==i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # We connect the root of u to the root of v
            self.parent[root_u] = root_v


#dfs
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False]*n
       
        
        
        #dfs using own stack
        st = [source]
        visited[source]=True
        while st:
            v = st.pop()
            if v==destination:
                return True
            for k in adj[v]:
                if not visited[k]:
                    st.append(k)
                    visited[v]=True
        
        return False
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False]*n
        #  bfs
        q = deque([source])
        visited = [False]*n
        visited[source]= True
        while q:
            v = q.popleft()
            for k in adj[v]:
                if k==destination:
                    return True
                if not visited[k]:
                    q.append(k)
                    visited[k]=True
        return False