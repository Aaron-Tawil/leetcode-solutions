# Problem: 703 – kth largest element in a stream
# Difficulty: Easy
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

import heapq
class KthLargest:
     
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = nums[:k]
        heapq.heapify(self.heap)

        for n in nums[k:]:
            if n > self.heap[0]:
                heapq.heapreplace(self.heap,n)
    

    def add(self, val: int) -> int:
        if len(self.heap)< self.k:
            heapq.heappush(self.heap,val)
        elif val>self.heap[0]:
            heapq.heapreplace(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)