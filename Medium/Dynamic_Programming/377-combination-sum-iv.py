# resembles change coin problem
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0]*(target+1)
        dp[0] = 1

        for amn in range(1,target+1):
            for num in nums:
                if amn-num>=0:
                    dp[amn]+=dp[amn-num]   
        
        return dp[target]