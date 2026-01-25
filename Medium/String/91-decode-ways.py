class Solution:
    def numDecodings(self, s: str) -> int:
        #dp[i] represents the number of ways for s[:i]
        n = len(s)
        # dp = [0]*(n+1)
        if not s or s[0]=='0':
            return 0
        prev2 = 1 # one posibilty for empty 
        prev1 = 1 # for first digit
        
        for i in range(1,n):
            curr = 0
            if s[i]!='0':
                curr+=prev1
            two_digits = int(s[i-1:i+1])
            if 10<=two_digits<=26:
                curr+=prev2
            if curr==0:
                return 0
            prev2 = prev1
            prev1 = curr
        return prev1

        