from collections import Counter
class Solution:

    #counter then the k most common using a max heap?
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        #heap
        #return [t[0] for t in counter.most_common(k)]

        #bucket sort
        # 2. Create buckets where index is frequency
        # We need n+1  buckets to handle frequencies from 1 to n (to hadle n)
        buckets = [[] for _ in range(len(nums)+1)]
        
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        # 3. Collect the top k elements by iterating backwards
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        