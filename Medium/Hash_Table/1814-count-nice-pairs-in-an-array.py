from collections import Counter
from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Helper to get the difference
        def get_diff(n):
            return n - int(str(n)[::-1])
        
        # 1. Calculate all differences and count their frequencies
        # Counter is a specialized defaultdict(int)
        freqs = Counter(get_diff(n) for n in nums)
        
        # 2. Sum up the combinations: n * (n-1) // 2
        total = 0
        for count in freqs.values():
            total += (count * (count - 1)) // 2
            
        return total % MOD
        # second way - my original
        def rev(num):
            return int(str(num)[::-1])
        
        dic = defaultdict(int)
        count = 0
        for num in nums:
            val = num-rev(num)
            if val in dic:
                count = (count + dic[val])%MOD
            dic[val]+=1
        

        return count