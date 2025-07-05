# Problem: 139 – word break
# Difficulty: Medium
# Link: https://leetcode.com/problems/word-break/description/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] true if s[:i+1] is wordBreak
        wordSet = set(wordDict)


        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            # if s[:i+1] in wordDict:
            #     dp[i]=True
            #     continue 
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True
                    break
        return dp[-1]        