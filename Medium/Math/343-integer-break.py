class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        
        # dp[i] = max(dp[i],dp[i-num]*num, num* (i-num)) for num in range 1 to i-1
        # base case dp[1] = 1

        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],max(dp[i-j],i-j)*j)
        
        return dp[n]