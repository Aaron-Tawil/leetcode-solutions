import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))

        
        #Dijkstra
        
        visited = set()
        max_delay = 0
        shortest_dist = {}

        heap = []
        heapq.heappush(heap,(0,k))
        shortest_dist[k] = 0

        while len(visited) < n and heap:
            curr_time , curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            max_delay = curr_time # we pop in increasing order, the last is the max delay
            visited.add(curr_node)

            for nei, w in adj[curr_node]:
                if shortest_dist.get(nei, float("inf")) > w+curr_time and nei not in visited:
                    heapq.heappush(heap,(w+curr_time,nei))
                    shortest_dist[nei] = w+curr_time

        return -1 if len(visited)!=n else max_delay