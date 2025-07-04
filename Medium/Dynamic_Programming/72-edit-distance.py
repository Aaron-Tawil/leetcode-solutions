# Problem: 72 – edit distance
# Difficulty: Medium
# Link: https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # let dp[i][j] be the min operation to convert word1[:i] to word2[:j]
        # base case first row and column - easy
        

        m,n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        #first row
        for i in range(n+1):
            dp[0][i] = i # insert
        #first col
        for i in range(m+1):
            dp[i][0] = i #delete

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        
        
        return dp[m][n]