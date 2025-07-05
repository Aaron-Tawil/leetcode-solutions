# Problem: 300 – Longest Increasing Subsequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-increasing-subsequence/

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # optimal nlogn using binary search on array lis[i] - the smallest num ending a subseq of leangth i
        n = len(nums)
        lis = [nums[0]]

        for i in range(1,n):
            # I need to insert nums[i] to the next of the item less than it 
            place = bisect.bisect_left(lis,nums[i])
            if place == len(lis):
                lis.append(nums[i])
            else:
                lis[place] = nums[i]
        return len(lis)

    def lengthOfLISNaive(self, nums: List[int]) -> int:
        #naive DP
        # let dp[i] be the longest subseq ending with nums[i]
        n = len(nums)
        dp = [-1]*len(nums)
        dp[0] = 1 
        for i in range(1,n):
            max_sub = 1
            for j in range(0,i):
                if nums[j] < nums[i] and dp[j] >= max_sub:
                    max_sub = dp[j] + 1
            dp[i] = max_sub
        return max(dp)


        