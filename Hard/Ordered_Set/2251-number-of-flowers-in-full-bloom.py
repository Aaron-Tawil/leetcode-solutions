import bisect
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = []
        end = []
        for s,e in flowers:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        res = []
        for time in people:
            started = bisect.bisect_right(start,time) #return the number of starters before time inclusive
            end_before = bisect.bisect_left(end,time)
            res.append(started-end_before)
        
        return res
        