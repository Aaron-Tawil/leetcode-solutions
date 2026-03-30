class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        remove = 0

        last_end = float("-inf")
        
        #Greedy by End Time
        for start,end in intervals:
            if start < last_end:
                remove+=1
            else:
                last_end = end


        return remove
        