
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_end = res[-1][1]
            
            # If overlap (current start <= last end)
            if current_start <= last_end:
                # Merge: update the end of the last added interval
                res[-1][1] = max(last_end, current_end)
            else:
                # No overlap: just add the new interval
                res.append([current_start, current_end])
                
        return res
        
        #sweep time
        # time  = []
        # for s,e in intervals:
        #     time.append((s,-1))
        #     time.append((e,0))

        # time.sort() #start is sorted before end due the -1 vs 0

        # res = []
        # count = 0
        # start = 0
        # for t ,ty in time:
        #     if count==0:
        #         start = t
        #     if ty==-1:
        #         count+=1
        #     if ty==0:
        #         count-=1
        #     if count==0:
        #         res.append([start,t])

        # return res 