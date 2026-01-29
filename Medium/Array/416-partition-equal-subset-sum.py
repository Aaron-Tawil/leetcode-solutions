class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        # subset sum problem / Knapsack problem
        target = s//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target,num-1,-1):  
                if dp[i-num]:
                    dp[i] = True
                if dp[target]:
                    return True
        return dp[target]