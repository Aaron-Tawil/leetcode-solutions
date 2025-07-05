# Problem: 1004 – max consecutive ones iii
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/


        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 0,0        
        max_ones = k
        zeros = 0

        while r<n:
            if nums[r]==0:
                if zeros<k: # we can flip and continue
                    zeros+=1
                else: # we need to advance l to the next 0
                    while l<=r and nums[l]!=0:
                        l+=1
                    l+=1 # skip the zero
            max_ones = max(max_ones,r-l+1)
            r+=1
            
        return max_ones




# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         l=r=0    
#         for r in range(len(nums)):
#             if nums[r] == 0:
#                 k-=1
#             if k<0:
#                 if nums[l] == 0:
#                     k+=1
#                 l+=1
#         return r-l+1