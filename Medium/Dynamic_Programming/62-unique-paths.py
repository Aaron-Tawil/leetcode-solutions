# Problem: 62 – unique paths
# Difficulty: Medium
# Link: https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # total steps = (m-1) + (n-1)
        # we need to choose (m-1) downward steps
        return math.comb(m + n - 2, m - 1)
        # combinatorics (m-1)+(n-1) choose m-1
        # ensure we loop over the smaller of (m-1) and (n-1)
        k, total = min(m-1, n-1), m+n-2
        res = 1
        for i in range(1, k+1):
            res = res * (total - k + i) // i
        return res

        # dp = [[1]*n for _ in range(m)]
        # for row in range(1,m):
        #     for col in range(1,n):
        #         dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        # return dp[m-1][n-1]
        