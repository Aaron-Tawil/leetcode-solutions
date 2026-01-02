class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp[i] = max(dp[i-1]+nums[i],nums[i])
        prev=float('-inf')
        mx = prev
        for num in nums:
            prev= max(prev+num,num)
            mx = max(mx,prev)
        return mx
        