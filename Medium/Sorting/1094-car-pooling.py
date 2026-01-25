class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #we have constant time range
        diffs = [0]*1001

        maxtime = 0
        for num_pass,s,e in trips:
            diffs[s] += num_pass
            diffs[e] -= num_pass
            maxtime = max(maxtime,s) # for smart early exit
        count = 0
        for time in range(maxtime+1):
            count+=diffs[time]
            if count>capacity:
                return False
        return True



        