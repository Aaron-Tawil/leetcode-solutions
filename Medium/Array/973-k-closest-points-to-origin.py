import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            norm = point[0]**2 + point[1]**2
            heapq.heappush(heap,(-norm,point)) #max heap
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [point for _, point in heap]
        # option 2 
        return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0] + p[1]*p[1])

        