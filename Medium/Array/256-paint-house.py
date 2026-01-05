class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #dp[i][0] = min(dp[i-1][1],dp[i-1][2])+costs[i][0]
        # DP with memory efficiency

        houses = len(costs)
        colors = 3
        prev = costs[0]
        for i in range(1,houses):
            curr = [0,0,0]
            for color in range(colors):
                curr[color] = min(prev[(color+1)%3],prev[(color+2)%3])+costs[i][color]
            prev = curr
        
        return min(prev)