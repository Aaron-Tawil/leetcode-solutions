class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for coin in coins: #to avoid duplicates it is important to first interate coins 
            for amn in range(1,amount+1):
                if amn-coin>=0:
                    dp[amn]+=dp[amn-coin]


        return dp[amount]