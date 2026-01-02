class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Convert to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # 2. Check if 'num' is the start of a sequence
            # (If num-1 exists, this isn't the start)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 3. Build the sequence upward
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

        # "union find" version or free style
        if not nums:
            return 0
        
        dic = {}
        res = 0
        for num in nums:
            if num in dic:
                continue
            mini,maxi = num,num
            if num-1 in dic:
                mini = dic[num-1][0]
            if num+1 in dic:
                maxi = dic[num+1][1]
                dic[num+1][0]= mini
            if num-1 in dic:
                dic[num-1][1]=maxi
            dic[num] = [mini,maxi]
            dic[mini][1] = maxi
            dic[maxi][0] = mini
            res = max(res,maxi-mini+1)
    
        return res
        