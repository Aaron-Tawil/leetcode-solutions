# Problem: 97 – interleaving string
# Difficulty: Medium
# Link: https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = dp[i-1][j] and s3[i+j]==s1[i]  or dp[i][j-1] and s3[j+i]==s2[j]

        #optimized 1dp
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m,n = len(s1), len(s2)
        if m + n != len(s3):
            return False



        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            if s2[j-1]==s3[j-1]:
                dp[j] = True
            else:
                break

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1]) # prev row or prev col

        return dp[n] 

        # normal 2dp
        # dp = [[False]*(n+1) for _ in range(m+1)]

        # dp[0][0] = True
        # #fill base case for s1
        # for row in range(m):
        #     if s1[row]==s3[row]:
        #         dp[row+1][0] = True
        #     else:
        #         break
        
        # #fill base case for s2
        # for col in range(n): 
        #     if s2[col]==s3[col]:
        #         dp[0][col+1] = True
        #     else:
        #         break
        
        # for r in range(1,m+1):
        #     for c in range(1,n+1):
        #         dp[r][c] = (dp[r-1][c] and s3[r+c-1]==s1[r-1])  or (dp[r][c-1] and s3[r+c-1]==s2[c-1])
        
        # return dp[m][n]

        