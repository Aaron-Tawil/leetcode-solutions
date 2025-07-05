# Problem: 322 – coin change
# Difficulty: Medium
# Link: https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP[i] min coins for amount i
        # dp[k] = 1 for k in coins otherwise inf
        # dp[i] = min(dp[i-k]) for all k in coins

        dp = [float('inf')] * (amount+1)
        dp[0] = 0 
        for k in coins:
            if k<=amount:
                dp[k] = 1
        
        for am in range(amount+1):  
            for k in coins:
                if 0<=am-k:
                    dp[am] = min(dp[am],dp[am-k]+1)
        
        return -1 if dp[amount]==float('inf') else dp[amount]