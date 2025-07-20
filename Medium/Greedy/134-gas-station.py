class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost)>sum(gas):
            return -1
        
        # the insight is that if we pass the condition it is guarnteed there is a solution
        start = tank = 0
        n = len(gas)
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank<0:
                start = i+1
                tank = 0

        return start 

        