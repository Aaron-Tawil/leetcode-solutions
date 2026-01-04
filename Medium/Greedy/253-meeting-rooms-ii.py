"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        time = []
        for inter in intervals:
            time.append((inter.start,1)) # 1 represent start
            time.append((inter.end,0)) # 0 for end

        time.sort()
        active_meets = 0
        res = 0
        for t,typ in time:
            if typ==1:
                active_meets+=1
            if typ==0:
                active_meets-=1
            res = max(res,active_meets)
        return res

        