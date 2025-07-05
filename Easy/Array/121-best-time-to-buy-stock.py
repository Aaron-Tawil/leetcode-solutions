# Problem: 121 - best time to buy and sell a stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                profit = prices[i] - min_val
                if profit > max_profit:
                    max_profit = profit
            
        return max_profit