import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(k):
            return sum([math.ceil(p/k) for p in piles]) <=h
        
        low,hi = 1, max(piles)

        while low < hi:
            mid = (low+hi)//2
            if canFinish(mid):
                hi = mid
            else:
                low = mid+1
        
        
        return low