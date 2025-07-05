# Problem: 621 – task scheduler
# Difficulty: Medium
# Link: https://leetcode.com/problems/task-scheduler/description/

from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        # classic “fill in blocks of size n+1” formula
        max_freq = freqs.most_common(1)[0][1] # the number of blocks
        count_maxs =  sum(1 for task in freqs if freqs[task]==max_freq) # for the last block

        return  max(len(tasks), (max_freq -1)*(n+1)+count_maxs) 