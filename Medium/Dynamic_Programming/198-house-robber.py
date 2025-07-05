# Problem: 198 – house robber
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        # let rob[i] be the max you can get until cell
        #rob[i] = max(rob[i-1],rob[i-2]+nums[i])
        #base rob[0] = nums[0], rob[1]=max(nums[0],nums[1])
        
        if not nums: return 0
        if len(nums)==1:
            return nums[0]
        prev2, prev1 = nums[0] , max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
           prev2, prev1 = prev1 , max(prev1,prev2+nums[i])

        return prev1 
        

        