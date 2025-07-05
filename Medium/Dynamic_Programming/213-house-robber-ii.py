# Problem: 213 – house robber ii
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        prev2, prev1 = nums[0] , max(nums[0],nums[1])
        if len(nums)==2: return prev1
        
        for i in range(2,len(nums)-1):
           prev2, prev1 = prev1 , max(prev1,prev2+nums[i])

        option1 = prev1
        # check option 2
        prev2, prev1 = nums[1] , max(nums[1],nums[2])
        
        for i in range(3,len(nums)):
           prev2, prev1 = prev1 , max(prev1,prev2+nums[i])
        option2 = prev1

        return max(option1,option2) 
        